from random import *
# def paper():
#     if x == 0:
#         print("your choice :-paper")
#         print("my choice :- rock\n you win")
#     elif x == 1:
#         print("your choice :-paper")
#         print("my choice :- paper\n game draw")
#     elif x == 2:
#         print("your choice :-paper")
#         print("my choice :- scissor\n you lost")
#
# def scissor():
#     if x == 0:
#         print("your choice :-scissor")
#         print("my choice :- rock\n you lost")
#     elif x == 1:
#         print("your choice :-scissor")
#         print("my choice :- paper\n you win")
#     elif x == 2:
#         print("your choice :-scissor")
#         print("my choice :- scissor\n game draw")


rock=0
paper=1
scissor=2

n=1

play=input("do you want to play y/n:")
if play=="y":
    for i in range (0,3):

        print("\t\t\tROUND :-",n)
        n+=1
        a = input("A.ROCK\nB.PAPER\nC.SCISSORS\n:-")
        if a == "a":
            x = (randrange(0, 3))
            if x == 0:
                print("your choice :-rock")
                print("my choice :- rock\n\t\t game draw\n")
            elif x == 1:
                print("your choice :-rock")
                print("my choice :- paper\n\t\t you lost\n")
            elif x == 2:
                print("your choice :-rock")
                print("my choice :- scissors\n\t\t you won\n")

        elif a == "b":
            y = (randrange(0, 3))
            if y == 0:
                print("your choice :-paper")
                print("my choice :- rock\n\t\t you won\n")
            elif y == 1:
                print("your choice :-paper")
                print("my choice :- paper\n\t\t game draw\n")
            elif y == 2:
                print("your choice :-paper")
                print("my choice :- scissors\n\t\t you lost\n")
            # paper()

        elif a == "c":
            z = (randrange(0, 3))
            if z == 0:
                print("your choice :-scissors")
                print("my choice :- rock\n\t\t you lost\n")
            elif z == 1:
                print("your choice :-scissors")
                print("my choice :- paper\n\t\t you won\n")
            elif z == 2:
                print("your choice :-scissors")
                print("my choice :- scissors\n\t\t game draw\n")

            # scissor()
    # b=input("do you want to play again y/n:")
    # if b=="y":
    #     continue
    # else:
    #     break




elif play=="n":
    print("thank you for giving your time!!!")
