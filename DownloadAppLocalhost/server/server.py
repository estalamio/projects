import functools
import tkinter;
from tkinter import *;
from tkinter import font, messagebox;
import os;
import pymysql;
from datetime import datetime
import threading
import socket
import pickle

global listaFajlovaZaKorisnika
listaFajlovaZaKorisnika=list();

class Greska(BaseException):
    def __init__(self):
        L=['Fajl ', 'ne ', 'postoji vise']
        poruka=functools.reduce((lambda x,y:x+y),L)
        print(poruka)
        messagebox.showinfo('Greska',poruka)

class Baza(Exception):
    def __init__(self):
        L=['Morate ', 'podignuti ', 'MySQL server']
        poruka=functools.reduce((lambda x,y:x+y),L)
        print(poruka)
        messagebox.showinfo('Greska',poruka)


def Obrisi():
    izabrani = listaFajlova.get(ACTIVE)
    if(str(izabrani)==''):
        messagebox.showinfo('Obavestenje','Morate odabrati stavku iz liste')
    else:
        try:
            db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="fp_baza")
            cursor = db.cursor();
        except Baza():
            pass
        try:
            os.remove('fajlovi/' + izabrani);
            listaFajlova.delete(ACTIVE)

        except Greska():
            pass



        trenutno = datetime.now()
        current_time = trenutno.strftime("%H:%M:%S")
        upit = "INSERT INTO INFORMACIJE(imeFajla, datum,vreme) VALUES('%s','%s','%s')" % (
        listaFajlova.get(ACTIVE), trenutno, current_time);
        cursor.execute(upit);
        db.commit();
        db.close();
        messagebox.showinfo('Obavestenje','Obrisano')

def izgled():
    forma = tkinter.Tk()
    forma.minsize(width=500,height=700)
    forma.maxsize(width=500,height=700)
    forma.configure(bd=1, bg='#E1E2E1');

    imeFrame= Frame(forma, bd=1, bg='red', width=500, height=500);
    imeFont=font.Font(family="Verdana", size=20);
    ime=Label(imeFrame, bd=1,text='Admin login', font=imeFont)

    poljaFont=font.Font(family="Verdana", size=20);

    ime.pack()
    imeFrame.pack();

    imeFrame.place(relx=0.82, rely=0.05, anchor=CENTER)

    naslovListeFrame=Frame(forma, bd=1, width=500, height=500);
    naslovListe=Label(naslovListeFrame, bd=1, text='Lista fajlova', font=imeFont);

    naslovListe.pack();
    naslovListeFrame.pack();

    naslovListeFrame.place(relx=0.34,rely=0.1)

    listaFajlovaFrame=Frame(forma, bd=1, width=500, height=200);

# dodajButton=Button(listaFajlovaFrame, bd=1, bg='#00bfa5', fg='white', text='Dodaj', width=10, height=5);
# dodajButton.pack(side=LEFT, padx=10);

    global listaFajlova
    listaFajlova=Listbox(listaFajlovaFrame, bd=1,selectmode=SINGLE);
    listaFajlova.pack(side=LEFT, padx=10);

    obrisiButton=Button(listaFajlovaFrame,bd=1,bg='#d50000', fg='white', text='Obrisi', width=10, height=5, command=Obrisi);
    obrisiButton.pack(side=LEFT, padx=10);

    listaFajlovaFrame.pack(side=LEFT);

    listaFajlovaFrame.place(relx=0.15,rely=0.2);


    i=0;

    listaFajlovaZaKorisnika = list();
    for entry in os.listdir('fajlovi'):
        if os.path.isfile(os.path.join('fajlovi', entry)):
            listaFajlova.insert(i,entry);
            listaFajlovaZaKorisnika.insert(i,entry);
            i=i+1;
    global poruka;
    poruka="";
    for i in range(len(listaFajlovaZaKorisnika)):
        poruka+= "$"+listaFajlovaZaKorisnika[i];
    threading.Thread(target=Main).start()
    forma.mainloop();


def RetrFile(name, sock):
    filename=sock.recv(1024).decode();
    if filename=='prikazi':
        stringZaSlanje="";
        i=0;
        for entry in os.listdir('fajlovi'):
            if os.path.isfile(os.path.join('fajlovi', entry)):
                listaFajlovaZaKorisnika.insert(i,entry)
                i=i+1

        for i in range(len(listaFajlovaZaKorisnika)):
            stringZaSlanje+="$"+listaFajlovaZaKorisnika[i];
        sock.send(stringZaSlanje.encode());
        stringZaSlanje=""
    else:
        with open(os.path.join('fajlovi',filename),'rb') as f:
            bytesToSend=f.read(1024);
            sock.send(("EXISTS"+str(os.path.getsize(os.path.join('fajlovi',filename)))).encode())
            sock.send(bytesToSend);
            while bytesToSend!="":
                bytesToSend=f.read(1024);
                sock.send(bytesToSend);
    sock.close;
    listaFajlovaZaKorisnika.clear();
    stringZaSlanje="";


    # if os.path.isfile(filename):
    #     sock.send(("EXISTS "+str(os.path.getsize(filename))).encode());
    #     userResponse=sock.recv(1024).decode();
    #     if userResponse[:2]=='OK':
    #         with open(filename,'rb') as f:
    #             bytesToSend=f.read();
    #             sock.send(bytesToSend);
    #             while bytesToSend!="":
    #                 bytesToSend=f.read();
    #                 sock.send(bytesToSend);
    #         f.close();
    # else:
    #     sock.send("ERR".encode())

def Main():
    host='127.0.0.1';
    port=5000;

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    s.bind((host,port));

    s.listen(5);

    print("Server Started");
    # stringZaSlanje="";
    # for i in range(len(listaFajlovaZaKorisnika)):
    #     stringZaSlanje+="$"+listaFajlovaZaKorisnika[i];

    while True:

        c, addr=s.accept();
        print("Client connected ip:<"+str(addr)+">");
        t=threading.Thread(target=RetrFile, args=("retrThread", c));
        t.start();
    s.close();

if __name__=='__main__':
    izgled();




