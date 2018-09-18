from collections import Counter

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
        return book_titles, book_descriptions


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


titles, descriptions = read_input("input/input00.txt")
print(process_titles(titles))
