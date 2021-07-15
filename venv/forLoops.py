
def loop_in_range():
    for item in range(0,10,2):
        print(item)

def total_prices():
    prices =[10,20,30]
    total = 0
    for item in prices:
        total+=item

    print (total)

def matrix_fun():
    matrix_str= "({},{})"
    for x in range(3):
        for y in range(3):
     #   print("("+str(x)+","+str(y)+")")
            print(matrix_str.format(x,y))



def print_number_of_x():
    number = [5,2,5,2,2]
    for item in number:
        print("x"*item)

def print_number_of_x_other():
    number = [1,1,1,1,6]
    for item in number:
        output = ""
        for count in range(item):
            output+="x"
        print(output)

def largest_num_in_list():
    big_list = [5,3,5,7,9,1]
    max_num = 0
    for item in big_list:
        if max_num<item:
            max_num=item

    print(max_num)


def largest_num_in_list_other():
    big_list = [2,3,5,7,9,10]
    max_num = 0
    for item in big_list:
        if max_num<item:
            max_num=item
    print(max_num)
