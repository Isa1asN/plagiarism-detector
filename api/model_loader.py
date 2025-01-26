from gensim.models.doc2vec import Doc2Vec

def load_model(model_path):
    return Doc2Vec.load(model_path)

def load_stopwords(stopwords_path):
    with open(stopwords_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()
