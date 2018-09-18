from collections import Counter
from scipy import spatial

import numpy as np
import math
from nltk import RegexpTokenizer
from nltk.corpus import stopwords


def read_input(filepath):
    """
    Using that function the input file is processed to distinguish the titles with the descriptions
    :param filepath: input file path
    :return:
    """
    with open(filepath, encoding="utf8", errors="ignore") as input:
        lines = input.readlines()
        book_number = int(lines[0].strip('\n'))
        book_titles = lines[1:book_number + 1]
        book_descriptions = lines[book_number + 2:]
        return book_titles, book_descriptions, book_number


def process_titles(titles):
    """
    Using that function you will be able to pre process the titles to unigrams and strip "noise"
    :param titles: list of book titles
    :return:
    """
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(stopwords.words('english'))
    unigrams = []
    bows = []
    find_features = []
    tokenized = [tokenizer.tokenize(title) for title in titles]
    for tokens in tokenized:
        title_unigrams = [word.lower() for word in tokens if
                          word not in stop_words and word not in ['Paperback', 'Hardcover']]
        title_bow = Counter(title_unigrams)
        find_features += list(title_bow.keys())
        unigrams.append(title_unigrams)
        bows.append(title_bow)
    features = list(set(find_features))
    return features, unigrams, bows


def process_descriptions(descriptions):
    """
    Using that function we process descriptions to define unigrams, bows and list of features
    :param descriptions:
    :return:
    """
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(stopwords.words('english'))
    unigrams = []
    bows = []
    find_features = []
    tokenized = [tokenizer.tokenize(desc) for desc in descriptions]
    for tokens in tokenized:
        desc_unigrams = [word.lower() for word in tokens if
                         word not in stop_words and not word.isdigit()]
        desc_bow = Counter(desc_unigrams)
        find_features += list(desc_bow.keys())
        unigrams.append(desc_unigrams)
        bows.append(desc_bow)
    desc_features = list(set(find_features))
    return desc_features, unigrams, bows


def build_feature_matrix(list_of_bags, features):
    """
    Using that function you are able to build the feature matrix.
    :param list_of_bags: list of text bows
    :return: feature matrix
    """
    feature_matrix = np.zeros((len(list_of_bags), len(features)))
    for i in range(0, feature_matrix.shape[0]):
        current_bow = list_of_bags[i]
        for j in range(0, feature_matrix.shape[1]):
            if features[j] in current_bow.keys():
                feature_matrix[i, j] = current_bow[features[j]]
            else:
                feature_matrix[i, j] = 0
    return feature_matrix


def calculate_tfidf(list_of_bags, features):
    """
    Using that function we are able to calculate the tfidf feature matrix.
    :param feature_matrix: tf feature matrix
    :return: tfidf feature matrix
    """
    feature_matrix = build_feature_matrix(list_of_bags, features)
    for j in range(0, feature_matrix.shape[1]):
        term_df = np.count_nonzero(feature_matrix[:, j])
        for i in range(0, feature_matrix.shape[0]):
            temp_eq = math.log((1 + feature_matrix.shape[0]) / (1 + term_df)) + 1
            feature_matrix[i, j] = feature_matrix[i, j] * temp_eq
    return feature_matrix


def _similarity(titles_matrix, desc_matrix):
    """
    The followign matrix calculates the
    :param tfidif_matrix:
    :return:
    """
    proposed_books = []
    for i in range(0, desc_matrix.shape[0]):
        description = desc_matrix[i, :]
        similarity = 0
        book = 0
        for j in range(0, titles_matrix.shape[0]):
            title = titles_matrix[j, :]
            current_sim = 1 - spatial.distance.cosine(description, title)
            if current_sim > similarity:
                similarity = current_sim
                book = j + 1
        proposed_books.append(book)
    return proposed_books


def evaluate(output_file, predicted):
    """
    Using that function we evaluate our predictions
    :param output_file: output file
    :return:
    """
    with open(output_file, encoding="utf8", errors="ignore")  as file:
        lines = file.readlines()
        books = [int(ind.strip("\n")) for ind in lines]
        counter = 0
        for i in range(len(books)):
            if books[i] == predicted[i]:
                counter += 1
        percentage = counter / len(books)
        return percentage
