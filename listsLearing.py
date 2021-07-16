def going_throu_lists():
    names = ["jane", "john", "timmy", "holly"]
    names[1] = "jonhy"
    print(names)
    print(names[2:])


def matrix_indexing():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in matrix:
        for item in row:
            print(item)


def index_methods():
    numbers = [34, 2, 2, 1, 2, 3, 5, 3, 4, 5, 6]
    list_new = []
    for x in numbers:
        if x not in list_new:
            list_new.append(x)

    print(list_new)


def number_spelling():
    numbers_text = ["zero", "one", "two", "three", "four",
                    "five", "six", "seven", "eight", "nine"]

    input_number = raw_input("Phone: ")

    for item in input_number:
        print(numbers_text[int(item)])


number_spelling()
