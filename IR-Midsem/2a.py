from nltk.tokenize import word_tokenize
from nltk import FreqDist
import math
from sklearn.feature_extraction.text import TfidfVectorizer

documents = ["I enjoy watching movies when it's cold outside",
             "Toy Story is the best animation movie ever",
             "Watching horror movies alone at night is really scary",
             "He loves films filled with suspense and unexpected plot twists ",
             "This is one of the most overrated movies I've ever seen"]

tokens = sum([word_tokenize(document) for document in documents], [])
words_frequency = FreqDist(tokens)
words_frequency.plot(30, cumulative=False)


def normalized_term_frequency(word, document):
    raw_frequency = document.count(word)
    if raw_frequency == 0:
        return 0
    return 1 + math.log(raw_frequency)


def docs_contain_word(word, list_of_documents):
    counter = 0
    for document in list_of_documents:
        if word in document:
            counter += 1

    return counter


def get_vocabulary(documents):
    vocabulary = set([word for document in documents for word in document])

    return vocabulary


def inverse_document_frequency(documents, vocabulary):
    idf = {}

    for word in vocabulary:
        contains_word = docs_contain_word(word, documents)
        idf[word] = 1 + math.log(len(documents) / (contains_word))

    return idf


def tf_idf(search_keys, dataframe, label):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_weights_matrix = tfidf_vectorizer.fit_transform(dataframe.loc[:, label])
    search_query_weights = tfidf_vectorizer.transform([search_keys])

    return search_query_weights, tfidf_weights_matrix
