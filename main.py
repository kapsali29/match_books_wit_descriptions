from process import read_input, process_titles, process_descriptions, calculate_tfidf, _similarity, evaluate

titles, descriptions, book_num = read_input("input/input01.txt")
features_titles, title_unigrams, title_bows = process_titles(titles)
features_desc, desc_unigrams, desc_bows = process_descriptions(descriptions)
total_features = features_titles + features_desc
total_bows = title_bows + desc_bows
_tfidf_matrix = calculate_tfidf(total_bows, total_features)
titles_matrix = _tfidf_matrix[0:book_num, :]
desc_matrix = _tfidf_matrix[book_num:, :]
predicted = _similarity(titles_matrix, desc_matrix)
print(evaluate("output/output01.txt", predicted))
