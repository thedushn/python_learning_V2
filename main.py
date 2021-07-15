# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


condition = True
started = False
print ("input commands")
while True:
    state = raw_input()
    state = state.lower()
    if state == "start":
        if started:
            print("already on")
        else:
            started = True
            print("started")
    elif state == "stop":
        if not started:
            print("already off")
        else:
            started = False
            print("stopped")
    elif state == "quit":
        break
    elif state == "help":
        print("start\nstop\nquit\n")
    else:
        print("bad input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
