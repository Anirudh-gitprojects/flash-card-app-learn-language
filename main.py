BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import time
data=pandas.read_csv("spanish.csv")
Spanish=data.Spanish.to_list()
new_lang_dict={data_row['Spanish']:data_row['English'] for (index,data_row) in data.iterrows()}
new_list_Spanish=[x for x,y in new_lang_dict.items()]
new_list_english=[y for x,y in new_lang_dict.items()]
count=0
not_correct = []

def show_Spanish():
    print(new_list_english)
    if len(new_list_Spanish)==0:
        canvas.itemconfig(a, text="Spanish")
        canvas.itemconfig(b, text="Bravo! Completado Satisfactoriamente", font=("Ariel", 30, "bold"))
        window.after(3000, show_eng)
    else:
        global count
        canvas.itemconfig(image2, image=my_img)
        canvas.itemconfig(a,text="Spanish")
        canvas.itemconfig(b,text=f'"{new_list_Spanish[count]}"')
        window.after(3000,show_eng)

def show_eng():
    if len(new_list_english)==0:
        canvas.itemconfig(image2, image=my_img2)
        canvas.itemconfig(a, text="English")
        canvas.itemconfig(b, text="Congrats!Completed Successfully", font=("Ariel", 30, "italic"))
        button_correct.destroy()
        button_wrong.destroy()
        button3 = Button(image=button3_image, highlightthickness=0, command=start_again,background=BACKGROUND_COLOR)
        button3.grid(row=2, column=0)
        button2=Button(image=button4_image,highlightthickness=0,command=window.destroy,background=BACKGROUND_COLOR)
        button2.grid(row=2, column=1)

    else:
        global count
        canvas.itemconfig(image2, image=my_img2)
        canvas.itemconfig(a, text="English")
        canvas.itemconfig(b, text=f'{new_list_english[count]}')

def start_again():
    pass
def on_click_true():
    if len(new_list_Spanish)==0:
        show_Spanish()
    else:
        global count
        new_list_Spanish.pop(count)
        new_list_english.pop(count)
        count=0
        show_Spanish()

def on_click_false():
        if len(new_list_Spanish)!=0:
            global count
            new_list_english.append(new_list_english[count])
            new_list_Spanish.append(new_list_Spanish[count])
            new_list_Spanish.pop(count)
            new_list_english.pop(count)
            count=0
            show_Spanish()
        else:
            canvas.itemconfig(a, text="Bravo")
            canvas.itemconfig(b, text="CONGRATS!Completed Successfully", font=("Ariel", 30, "bold"))

#def show_incorrect():
   # global count
   # count=0
   # canvas.itemconfig(a,text="Spanish")
   # canvas.itemconfig(b,text=new_list_Spanish[count])
    #window.after(3000,show_eng)

window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50)
window.config(background=BACKGROUND_COLOR)
my_img=PhotoImage(file="card_front.png")
my_img2=PhotoImage(file="card_back.png")
canvas=Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
image2=canvas.create_image(400,280,image=my_img)
canvas.grid(row=1,columnspan=2)
button1_img=PhotoImage(file="right.png")
button2_img=PhotoImage(file="wrong.png")
button3_image = PhotoImage(file="a1.png")
button4_image=PhotoImage(file="b1.png")
button_correct=Button(image=button1_img,highlightthickness=0,command=on_click_true)
button_correct.grid(row=2,column=0)
button_wrong=Button(image=button2_img,highlightthickness=0,command=on_click_false)
button_wrong.grid(row=2,column=1)
a = canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"), tags=1)
b = canvas.create_text(400, 263, text='"que"', font=("Ariel", 60, "bold"))
show_Spanish()

window.mainloop()