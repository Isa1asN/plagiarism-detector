# Plagiarism Detection for Amharic text

This project implements a plagiarism detection system for the Amharic language using the **Doc2Vec** model. It provides a pipeline for data preprocessing, model training, and similarity computation, which serves as the foundation for a FastAPI server.

## Workflow

### 1. **Data Preprocessing**
   - Raw text is cleaned and normalized to prepare it for training and inference.
   - Stopwords are removed, and unnecessary characters are filtered out.
   - Text data is tokenized and transformed into a format suitable for the **Doc2Vec** model.

### 2. **Model Training**
   - The **Doc2Vec** model is trained on the preprocessed text data using Gensim.
   - Trained embeddings are saved for use in inference tasks.
   - The training process involves tuning hyperparameters and building robust document vectors.

### 3. **Similarity Computation**
   - The trained **Doc2Vec** model is used to calculate document similarities.
   - Cosine similarity is computed between the vectors of input documents.
   - The system identifies plagiarized sections by comparing sentences or text segments.