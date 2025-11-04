# ------ Libraries -------- #
import pandas as pd
import tkinter as tk
import random

# ------- Constants ------- #

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT= ("Arial", 40, "italic")
VOCAB_FONT= ("Arial", 60, "bold")
FRONT_LANGUAGE = "French"
BACK_LANGUAGE = "English"

df = pd.read_csv('./data/french_words.csv')
FRENCH_WORDS = dict(zip(df['French'], df['English']))

# --------- Create Button Functions -------- #
known_words = []
missed_words = []
front_is_shown = True
french_word = random.choice(list(FRENCH_WORDS.keys()))
english_word = FRENCH_WORDS[french_word]


def choose_words():
    global french_word,english_word,known_words
    french_word = random.choice(list(FRENCH_WORDS.keys()))
    english_word = FRENCH_WORDS[french_word]
    if french_word in known_words:
        choose_words()

def new_card():
    global job1,job2,known_words,missed_words,FRENCH_WORDS
    window.after_cancel(job1)
    window.after_cancel(job2)
    choose_words()
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(language, text=FRONT_LANGUAGE)
    canvas.itemconfig(vocab, text=french_word)
    words_to_learn = [{"French":key, "English": value} for key,value in FRENCH_WORDS.items() if key not in known_words]
#TODO: come back later and fix  the saving of words. This just  creates a new file rather than appending or removing learned words
    new_df = pd.DataFrame([words_to_learn])
    new_df.to_csv('./data/french_words_to_learn.csv', index=False)
    def forced_miss():
        global job1, job2
        job1 = window.after(10000, wrong)
        job2 = window.after(10000, new_card)
    forced_miss()

def correct():
    global known_words, english_word, french_word
    known_words.append({french_word: english_word})
    choose_words()
    new_card()
    print(known_words)

def wrong():
    global missed_words,english_word,french_word
    missed_words.append({french_word: english_word})
    choose_words()
    new_card()
    print(missed_words)


def flip():
    global front_is_shown
    if front_is_shown:
        canvas.itemconfig(card, image=back_image)
        canvas.itemconfig(language, text=BACK_LANGUAGE)
        canvas.itemconfig(vocab, text=english_word)
        front_is_shown = False
    else:
        canvas.itemconfig(card, image=front_image)
        canvas.itemconfig(language, text=FRONT_LANGUAGE)
        canvas.itemconfig(vocab,text=french_word)
        front_is_shown = True

# --------  Create  GUI -------- #


window = tk.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR,padx=50, pady=50)

job1 = window.after(10000, wrong)
job2 = window.after(10000, new_card)

# ---------- Create Images ready for tkinter ------------ #
check_image = tk.PhotoImage(file="./images/right.png")
check_button = tk.Button(image=check_image,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=correct)
check_button.grid(column=0, row=3)

x_image = tk.PhotoImage(file="./images/wrong.png")
x_button = tk.Button(image=x_image,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=wrong)
x_button.grid(column=2, row=3)

flip_button = tk.Button(text="FLIP",highlightthickness=0,command=flip,height=5,width=10,font=("Arial",25,"bold"),highlightbackground=BACKGROUND_COLOR)
flip_button.grid(column=1, row=3)

front_image = tk.PhotoImage(file="./images/card_front.png")
back_image = tk.PhotoImage(file="./images/card_back.png")

# ---------- Create Canvas ---------- #
canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR,highlightthickness=0)
card = canvas.create_image(400,263, image=front_image)
language = canvas.create_text(400,150, text=FRONT_LANGUAGE, font=LANGUAGE_FONT, fill="black")
vocab = canvas.create_text(400,263,text=french_word,font=VOCAB_FONT, fill="black")
canvas.grid(column=0, row=0,columnspan=3)


window.mainloop()