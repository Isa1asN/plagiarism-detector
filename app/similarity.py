from scipy.spatial import distance
import re

def get_similarity(doc_0, doc_1, model, stopwords, sentence_delimiter="።", preprocess=None):
    """
    Compute the similarity between two documents based on sentence embeddings using Doc2Vec.
    
    Args:
        doc_0 (str): First document as a string.
        doc_1 (str): Second document as a string.
        model (Doc2Vec): Pre-trained Doc2Vec model.
        sentence_delimiter (str): Delimiter to split sentences (default is "።").
    
    Returns:
        list: A list of similarity scores and sentence locations.
    """
    def process_sentences(document):
        # Split into sentences using the specified delimiter
        sentences = document.split(sentence_delimiter)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        # Preprocess and infer vectors
        vectors = []
        for sentence in sentences:
            prep_sentence = preprocess(sentence, stopwords)
            tokens = prep_sentence.split()
            
            if tokens:  # Ensure tokens are not empty
                vector = model.infer_vector(tokens)
                vectors.append((vector, sentence))
        
        return vectors

    vectors_0 = process_sentences(doc_0)
    vectors_1 = process_sentences(doc_1)
    
    # Compute cosine similarity between all sentence vectors
    values = []
    for v0, sentence_0 in vectors_0:
        for v1, sentence_1 in vectors_1:
            similarity = 1 - distance.cosine(v0, v1)
            values.append((similarity, sentence_0, sentence_1))
    
    return values


def get_similarity_with_indices(doc_0, doc_1, model, stopwords, sentence_delimiter="።", preprocess=None):
    """
    Compute the similarity between two documents based on sentence embeddings using Doc2Vec,
    and return cosine similarity with start and end indices.
    
    Args:
        doc_0 (str): First document as a string.
        doc_1 (str): Second document as a string.
        model (Doc2Vec): Pre-trained Doc2Vec model.
        sentence_delimiter (str): Delimiter to split sentences (default is "።").
    
    Returns:
        list: A list of similarity scores and sentence indices.
    """
    def process_sentences_with_indices(document):
        sentences = document.split(sentence_delimiter)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        vectors_with_indices = []
        for sentence in sentences:
            # Preprocess the sentence
            prep_sen = preprocess(sentence, stopwords)
            tokens = prep_sen.split()
            if tokens:
                vector = model.infer_vector(tokens)
                # Find sentence start and end indices
                for match in re.finditer(re.escape(sentence), document):
                    start, end = match.start(), match.end()
                    vectors_with_indices.append((vector, start, end, sentence))
        return vectors_with_indices

    vectors_0 = process_sentences_with_indices(doc_0)
    vectors_1 = process_sentences_with_indices(doc_1)
    
    values = []
    for v0, start_0, end_0, sentence_0 in vectors_0:
        for v1, start_1, end_1, sentence_1 in vectors_1:
            similarity = 1 - distance.cosine(v0, v1)
            values.append((similarity, (start_0, end_0), (start_1, end_1)))
    
    return values