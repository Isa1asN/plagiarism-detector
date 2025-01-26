from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from model_loader import load_model, load_stopwords
from pre_process import preprocess, preprocess_document
from similarity import get_similarity_with_indices
from utils import clip_with_context
from html import escape

model = load_model("../models/doc2vec_am.bin")
stopwords = load_stopwords("../amstopwords.txt")

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/compare", response_class=HTMLResponse)
async def compare(request: Request, doc1: str = Form(...), doc2: str = Form(...)):
    scores = get_similarity_with_indices(doc1, doc2, model, stopwords, "።", preprocess=preprocess)
    scores.sort(reverse=True)

    highlighted_doc1 = escape(doc1).replace('\n', '<br>')
    highlighted_doc2 = escape(doc2).replace('\n', '<br>')

    colors = ['#FFE6E6', '#FFD6D6', '#FFC6C6', '#FFB6B6', '#FFA6A6', '#FF9696', '#FF8686', '#FF7676']
    hover_colors = ['#FF726F', '#FF6260', '#FF5251', '#FF4242', '#FF3333', '#FF2424', '#FF1515', '#FF0606']

    processed_spans_1 = set()
    processed_spans_2 = set()

    for idx, (similarity, indices_0, indices_1) in enumerate(scores):
        if similarity < 0.65:
            continue
            
        span1_key = f"{indices_0[0]}-{indices_0[1]}"
        span2_key = f"{indices_1[0]}-{indices_1[1]}"
        
        if span1_key not in processed_spans_1:
            part1 = clip_with_context(doc1, indices_0, context_size=0)
            color_idx = min(int((1 - similarity) * len(colors)), len(colors) - 1)
            
            highlight_class = f"similarity-{idx}"
            style = f"background-color: {colors[color_idx]};"
            hover_style = f"background-color: {hover_colors[color_idx]};"
            
            highlight_span = (
                f'<span class="hovertext highlight {highlight_class}" '
                f'style="{style}" '
                f'data-hover="Similarity: {similarity:.2f}" '
                f'data-hover-style="{hover_style}">{part1}</span>'
            )
            highlighted_doc1 = highlighted_doc1.replace(part1, highlight_span)
            processed_spans_1.add(span1_key)

        if span2_key not in processed_spans_2:
            part2 = clip_with_context(doc2, indices_1, context_size=0)
            color_idx = min(int((1 - similarity) * len(colors)), len(colors) - 1)
            
            highlight_class = f"similarity-{idx}"
            style = f"background-color: {colors[color_idx]};"
            hover_style = f"background-color: {hover_colors[color_idx]};"
            
            highlight_span = (
                f'<span class="hovertext highlight {highlight_class}" '
                f'style="{style}" '
                f'data-hover="Similarity: {similarity:.2f}" '
                f'data-hover-style="{hover_style}">{part2}</span>'
            )
            highlighted_doc2 = highlighted_doc2.replace(part2, highlight_span)
            processed_spans_2.add(span2_key)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "highlighted_doc1": highlighted_doc1,
            "highlighted_doc2": highlighted_doc2,
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)