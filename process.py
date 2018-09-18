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


read_input("input/input00.txt")
