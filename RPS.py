
import tkinter
import random
from tkinter import Button, Image, Label, StringVar, font
from tkinter.constants import TOP
from typing import Text
from PIL import Image, ImageTk


#creating window

root= tkinter.Tk()
root.geometry("400x600+500+50")
root.title("Rock Paper Scissors")
root.resizable(False,False)

#styling 
root.configure(bg="#baa5ad")


#options of the game

options=["rock","paper","scissors"]



#widgets 

headtitle = tkinter.Label(text="Welcome to Rock Paper Scissors", bg="#baa5ad", fg="#4f1a2e", font=("Verdana",15,'bold')) 
headtitle.pack()

introduction= tkinter.Label(text="Do you wanna play ? ", bg="#baa5ad", fg="black", font=("consolas",10))
introduction.place(rely=0.1, relx=0.33)

response_label=tkinter.Label(root,text="", bg="#baa5ad", fg="black", font=("consolas",10,'bold'))
response_label.place(rely=0.3, relx=0.4)

#yes button command

def confirmation():
    response_label.config(text='Good luck !')
    rock_btn.place(rely=0.4, relx=0.05)
    paper_btn.place(rely=0.4, relx=0.38)
    scissors_btn.place(rely=0.4, relx=0.7)


yes_btn = tkinter.Button(root,text="Yes", width=8, height=1, bg="#20020d", fg="white" ,command=confirmation, font=("Verdana",10,'bold'))
yes_btn.place(relx=0.12,rely=0.2)


no_btn = tkinter.Button(root,text="No", width=8, height=1, bg="#20020d", fg="white", command=root.destroy, font=("Verdana",10,'bold'))
no_btn.place(rely=0.2, relx=0.7)



#game algorithm

def make_choice(value):
    computer_choice= options[random.randrange(3)]

    if value=="rock":
        if computer_choice =="rock":
            result_label.config(text='Computer picked rock.Its a tie')
            reaction_label.config(image=tie)
        elif computer_choice =="paper":
            result_label.config(text="Computer picked paper.You lose")
            reaction_label.config(image=lose)
        else:
            result_label.config(text="Computer picked scissors.You win")
            reaction_label.config(image=win)
    elif value=="paper":
        if computer_choice =="rock":
            result_label.config(text='Computer picked rock.You win')
            reaction_label.config(image=win)
        elif computer_choice =="paper":
            result_label.config(text='Computer picked paper.Its a tie')
            reaction_label.config(image=tie)

        else:
            result_label.config(text='Computer picked scissors.You lose')
            reaction_label.config(image=lose)
    else:
        if computer_choice =="rock":
            result_label.config(text='Computer picked rock.You lose')
            reaction_label.config(image=lose)
        elif computer_choice =="paper":
            result_label.config(text='Computer picked paper.You win')
            reaction_label.config(image=win)
        else:
            result_label.config(text='Computer picked scisssors.Its a tie')
            reaction_label.config(image=tie)
    
    reaction_label.place(relx=0.35,rely=0.75)


#images for buttons

rock= ImageTk.PhotoImage(Image.open("rock.png"))
paper= ImageTk.PhotoImage(Image.open("paper.png"))
scissors= ImageTk.PhotoImage(Image.open("scissors.png"))


#reaction images


tie= ImageTk.PhotoImage(Image.open("tie.jpg"))
win= ImageTk.PhotoImage(Image.open("win.jpg"))
lose=ImageTk.PhotoImage(Image.open("smug.png"))


#buttons for choices 

rock_btn=tkinter.Button( width=100, height=100,image=rock,compound=TOP, command= lambda *args: make_choice("rock"))
rock_btn.pack_forget()
paper_btn=tkinter.Button( width=100, height=100,image=paper,compound=TOP, command= lambda *args: make_choice("paper"))
paper_btn.pack_forget()
scissors_btn=tkinter.Button( width=100, height=100,image=scissors,compound=TOP, command= lambda *args: make_choice("scissors"))
scissors_btn.pack_forget()

#win or lose or tie comment 
result_label=tkinter.Label(text="",bg="#baa5ad", fg="black", font=("Verdana",10,'underline'))
result_label.place(relx=0.2, rely=0.65)

#reaction to result 
reaction_label=tkinter.Label(width=100,height=100)
reaction_label.pack_forget()



#maintaining window open

root.mainloop()
