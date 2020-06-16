import tkinter;
from tkinter import *;
from tkinter import font;

forma = tkinter.Tk()
forma.minsize(width=500,height=500)
forma.maxsize(width=500,height=500)
forma.configure(bd=1, bg='#E1E2E1');

naslovFrame= Frame(forma, bd=1, width=500, height=500);
naslovFont=font.Font(family="Verdana", size=50);
naslov=Label(naslovFrame, bd=1,text='Admin login', font=naslovFont)

poljaFont=font.Font(family="Verdana", size=20);

naslov.pack()
naslovFrame.pack();

naslovFrame.place(relx=0.5, rely=0.2, anchor=CENTER)

unosPodataka=Frame(forma, bd=1, width=500, height=100);

usernamePolje=tkinter.Entry(unosPodataka,bd=0, bg='white',font=poljaFont);
usernamePolje.pack(pady=10,anchor=CENTER);

passwordPolje=tkinter.Entry(unosPodataka,bd=0, bg='white',font=poljaFont);
passwordPolje.pack(pady=10,anchor=CENTER);

submitButton=tkinter.Button(unosPodataka, bd=0, bg='#aa00ff', fg='white', font=poljaFont, text='PRIJAVA', width=19);
submitButton.pack(pady=10,anchor=CENTER);

# usernamePolje.place(relx=0.15,rely=0.2);
# passwordPolje.place(relx=0.15,rely=0.6);
# submitButton.place(relx=0.15,rely=0.8);

unosPodataka.pack(side=BOTTOM,anchor=S);

unosPodataka.place(relx=0.5, rely=0.5, anchor=CENTER);




forma.mainloop();