import webbrowser
from tkinter import *


def open_url():
    webbrowser.open('www.google.com.br')


if __name__ == '__main__':
    root = Tk()

    root.title = 'Open Browser'
    root.geometry('300x200')

    opener = Button(
        root,
        text='Open Google',
        command=open_url
    ).pack(pady=20)

    root.mainloop()