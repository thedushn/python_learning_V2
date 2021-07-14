# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


condition = True
car_on_off = False
print ("input commands")
while condition:
    state = raw_input()
    state = state.lower()
    if state == "start":
        if car_on_off:
            print("already on")
        else:
            car_on_off = True
            print("started")
    elif state == "stop":
        if not car_on_off:
            print("already off")
        else:
            car_on_off = False
            print("stopped")
    elif state == "quit":
        condition = False
    elif state == "help":
        print("start\nstop\nquit\n")
    else:
        print("bad input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
