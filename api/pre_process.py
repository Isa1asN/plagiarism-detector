import re

def preprocess(sentence, stopwords):
    def remove_stopwords_from_sentence(sentence, stopwords):
        words = sentence.split()
        filtered_words = [word for word in words if word not in stopwords]
        return " ".join(filtered_words)
    
    sentence = remove_stopwords_from_sentence(sentence, stopwords)

    def remove_characters(sentence):
        s = re.sub(r'[^\w\s]', ' ', sentence)
        s = re.sub(r'\s+', ' ', s).strip()
        return s
    
    sentence = remove_characters(sentence)
    
    return sentence

def preprocess_document(document, stopwords):
    sentences = document.split("።")
    preprocessed_sentences = [preprocess(sentence, stopwords) for sentence in sentences if sentence.strip()]
    preprocessed_document = " ".join(preprocessed_sentences)
    return preprocessed_document