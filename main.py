from tkinter import *
from word_manager import WordManager

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

wm = WordManager()

data = {}


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_image)
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=data["EN"], fill="white")


def next_card():
    global data, flip_timer
    window.after_cancel(flip_timer)
    data = wm.get_word()
    canvas.itemconfig(canvas_img, image=card_front_image)
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=data["FR"], fill="black")
    flip_timer = window.after(3000, flip_card)


def right_button():
    wm.learn_word(word_fr=data["FR"], word_en=data["EN"])
    next_card()


def left_button():
    # time_reset()
    next_card()


flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_image)
title_txt = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=left_button)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=right_button)
check_button.grid(row=1, column=1)

save_button = Button(text="Save", command=wm.save_data)
save_button.grid(row=2, column=2)

next_card()
window.mainloop()
