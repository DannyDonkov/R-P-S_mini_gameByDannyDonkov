from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Rock Paper Scissor")
window.configure(background="black")

# import the images
image_rock1 = ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock2.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("papper2.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor2.png"))

# set the labels
label_player = Label(window, image=image_rock2)
label_computer = Label(window, image=image_rock1)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

computer_score = Label(window, text=0, font=('arial', 60, "bold"), fg="blue")
player_score = Label(window, text=0, font=('arial', 60, "bold"), fg="blue")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

player_indicator = Label(window, font=("arial", 40, "bold"), text="PLAYER", bg="red", fg="purple")
computer_indicator = Label(window, font=("arial", 40, "bold"), text="COMPUTER", bg="red", fg="purple")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)

final_message = Label(window, font=("arial", 40, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2)


def updatemessage(a):
    final_message['text'] = a


def computer_update():
    final = int(computer_score['text'])
    final += 1
    computer_score['text'] = str(final)


def player_update():
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)


def winner_check(p, c):
    if p == c:
        updatemessage("It's a tie")
    elif p == "rock":
        if c == "paper":
            updatemessage("Computer Wins!")
            computer_update()
        else:
            updatemessage("Player Wins!")
            player_update()
    elif p == "paper":
        if c == "scissor":
            updatemessage("Computer Wins!")
            computer_update()
        else:
            updatemessage("Player Wins!")
            player_update()
    elif p == "scissor":
        if c == "rock":
            updatemessage("Computer Wins!")
            computer_update()
        else:
            updatemessage("Player Wins!")
            player_update()
    else:
        pass


to_select = ["rock", "paper", "scissor"]


def choice_update(a,):
    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)

    if a == "rock":
        label_player.configure(image=image_rock2)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)

    winner_check(a, choice_computer)


# buttons configuration
Button(window, width=18, height=4, text="Rock", font=("ariel", 20, "bold"),
       bg="orange", fg="green", command=lambda: choice_update("rock")).grid(row=2, column=1)
Button(window, width=18, height=4, text="Paper", font=("ariel", 20, "bold"),
       bg="orange", fg="white", command=lambda: choice_update("paper")).grid(row=2, column=2)
Button(window, width=18, height=4, text="Scissor", font=("ariel", 20, "bold"),
       bg="orange", fg="red", command=lambda: choice_update("scissor")).grid(row=2, column=3)
window.mainloop()
