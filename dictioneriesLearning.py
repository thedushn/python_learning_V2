def template_dictionary():
    customer = {
        "name": "John",
        "age": 30,
        "verified": True
    }
    print(customer["name"])


def print_numbers_to_words():
    number_dictionary = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"

    }
    number = raw_input("phone: ")
    output_string = ""
    for item in number:
        output_string += number_dictionary.get(item) + " "

    print (output_string)


def split_string():
    message = raw_input("input with spaces: ")

    for item in message.split(" "):
        print (item)


split_string()
