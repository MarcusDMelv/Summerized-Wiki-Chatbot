import wikipedia
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
# import window support
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

"""
#TEXTBASED aiWIKI 
search_phase = input("Type in a search phrase")
output_sentences = input("How many sentences would you like to output?")
output_phase = wikipedia.summary(search_phase, sentences=output_sentences)
print(output_phase)
"""

# GUI
window = tk.Tk()
# title
window.title("Riley the AI")
# size full screen
window.geometry('750x700')

# better GUI
style = ttk.Style(window)

# color gui
window.configure(bg='orange')

# icon images
# trash icon
trashIcon = PhotoImage(file="trash.png")
# size image
trash = trashIcon.subsample(3, 3)

# speaker icon
speakIcon = PhotoImage(file="riley.png")
# size image
speaker = speakIcon.subsample(2, 2)

# text icon
textIcon = PhotoImage(file="print.png")
# size image
text = textIcon.subsample(3, 3)

# copy icon
copyIcon = PhotoImage(file="copy.png")
# size image
copy1 = copyIcon.subsample(3, 3)

# image of Riley
aiIcon = PhotoImage(file="ai.png")
# size image
ai1 = aiIcon.subsample(1, 1)
# actual image
ai = Label(window, image=ai1, padx=5, pady=5, bg="orange")
ai.grid(column=1, row=0)

# label image
searchIcon = PhotoImage(file="searchLabel.png")
# sizing
search_label = searchIcon.subsample(2, 2)

# text image
textIcon = PhotoImage(file="textLabel.png")
# sizing image
text_label = textIcon.subsample(2, 2)


# ai is created
def ai_creator():
    # the text that you converted to audio uncomment
    # file input audio
    myText = open("ai.txt", "r").read().replace("\n", " ")
    # language
    language = 'en'
    # Playing the converted file
    speak.Speak(myText)


# erase input
    # entry_sentences.delete('1.0', END)
def erase():
    # entries
    entry.delete('1.0', END)
    output_display.delete('1.0', END)
    print("About to erase output:")
    print("About to Erase input:")
    erase()


# search wiki function
def wiki_output():
    # entries
    search_phrase = entry.get('1.0', tk.END)
    #
    output_phrase = wikipedia.summary(search_phrase, sentences=2)
    #
    # open file / write in file
    file = open("ai.txt", "w")
    # ai writes output in a file
    file.write('your topic is interesting. ')
    file.write(output_phrase)
    file.write(' I am Riley thank you')
    # closes file
    file.close()
    # ai speaks
    ai_creator()

    # output text


def output_text():
    # entries
    search_phrase = entry.get('1.0', tk.END)
    output_phrase = wikipedia.summary(search_phrase, sentences=100)
    output_display.insert(tk.END, output_phrase)
    # causes many loops if I uncomment output_text()
    # output_text


def copy():
    search_phrase = entry.get('1.0', tk.END)
    output_phrase = wikipedia.summary(search_phrase, sentences=100)
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(output_phrase)
    r.update()
    copy()

    print("About to print speech:")
    print(output_phrase)


# a label widget is created for what topic to search
label_text_to_summarize1 = Label(window, image=search_label, padx=5, pady=5, bg='orange')
# label was placed using .grid
label_text_to_summarize1.grid(row=0, column=0)

# user input for topic
entry = ScrolledText(window,
                     height=0)  # location of the scrolled text widget using .grid entry.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
# location of the scrolled text widget using .grid
entry.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

# button created to activate ai
button_run = Button(window, image=speaker, command=wiki_output, width=65, height=80, bg='white', fg='#fff')
# button is placed and sized using .grid
button_run.grid(row=5, column=0, padx=5, pady=6)

# button created to erase
button_run1 = Button(window, text="Erase Input", image=trash, command=erase, width=65, height=80, bg='white', fg='#fff')
# button is placed and sized using .grid
button_run1.grid(row=5, column=1, padx=5, pady=5)

# button created to copy output
button_run2 = Button(window, image=copy1, command=copy, width=65, height=80, bg='white', fg='#fff')
# button is placed and sized using .grid
button_run2.grid(row=6, column=1, padx=5, pady=5)

# button created to output text
button_run2 = Button(window, image=text, command=output_text, width=65, height=80, bg='white', fg='#fff')
# button is placed and sized using .grid
button_run2.grid(row=6, column=0, padx=5, pady=5)

# a label widget is created for the window with text 'Enter text to Summarize'
label_text_to_summarize3 = Label(window, image=text_label, padx=5, pady=5, bg='orange')
# label was placed using .grid
label_text_to_summarize3.grid(row=7, column=0)

# output AI WIKI results
output_display = ScrolledText(window, wrap=WORD, height=9, width=90)
# output_display is placed using .grid
output_display.grid(row=8, column=0, columnspan=5, padx=5, pady=5)

# needed for GUI
window.mainloop()
