import json
import os
import socket
import threading
import tkinter;
from datetime import datetime
from tkinter import *;
from tkinter import font, messagebox;
import functools
from numpy import long
from pip._vendor.distlib.compat import raw_input

class Greska(Exception):
    def __init__(self):
        L=['Proveriti ', 'da ', 'li je server aktivan']
        poruka=functools.reduce((lambda x,y:x+y),L)
        print(poruka)
        messagebox.showinfo('Greska',poruka)

direktorijum='skinuto';
porukaSaServera=""

forma = tkinter.Tk()
listaFajlovaFrame=Frame(forma, bd=1, width=500, height=200);
listaFajlova=Listbox(listaFajlovaFrame, bd=1,width=56);
listaPreuzetihFrame=Frame(forma, bd=1, width=341);
listaPreuzetih = Listbox(listaPreuzetihFrame, bd=1, bg='white', width=56, height=10);
#filename="";
recnikIzbrisanih=dict();
obrisaniFajlovi=list();

def preuzmi():
    host = '127.0.0.1';
    port = 5000;
    global s;
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    #s.connect((host, port));
    try:
        s.connect((host,port))
        print('Cao')
    except Greska():
        pass
    global filename;
    filename=str(listaFajlova.get(ACTIVE));
    if(filename!=''):
        s.send(filename.encode())
        data=s.recv(1024).decode();
        rastavljenPodatak=data.split("EXISTS");
        filesize=rastavljenPodatak[1];
        print(filesize)
        if os.path.exists(direktorijum+'/'):
            f=open(os.path.join(direktorijum,filename),'wb')
            data=s.recv(1024)
            totalRecv=len(data)
            f.write(data)
            while totalRecv<int(filesize):
                data=s.recv(1024)
                totalRecv+=len(data)
                f.write(data)
        i=0;
        listaPreuzetih.delete(0, END)
        if os.path.exists(os.path.join(direktorijum+'/')):
            for entry in os.listdir(direktorijum):
                if os.path.isfile(os.path.join(direktorijum, entry)):
                    listaPreuzetih.insert(i, entry);
                    i = i + 1;
        else:
            messagebox.showinfo('Poruka','Nema foldera')
            os.mkdir(direktorijum);
            f = open(os.path.join(direktorijum, "new_" + filename), 'wb')
            data = s.recv(1024)
            totalRecv = len(data)
            f.write(data)
            while totalRecv < int(filesize):
                data = s.recv(1024)
                totalRecv += len(data)
                f.write(data)
            for entry in os.listdir(direktorijum):
                listaPreuzetih.delete(0,END);
                if os.path.isfile(os.path.join(direktorijum, entry)):
                    listaPreuzetih.insert(i, entry);
                    i = i + 1;
        messagebox.showinfo('Obavestenje','Preuzimanje zavrseno')
    else:
        messagebox.showinfo('Obavestenje','Morate izabrati fajl za skidanje')


    s.close();


def prikazi():
        host = '127.0.0.1';
        port = 5000;
        global s;
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        try:
            s.connect((host, port));
            s.send("prikazi".encode())
            poruka = s.recv(1024).decode();
        except Greska():
            pass



        global g;
        g=poruka;
        porukaSaServera=g.split("$");
        fajlovi=list(filter(lambda x: len(x)<15, porukaSaServera))
        print(porukaSaServera)
        print(fajlovi)
        prikazFajlova=list();
        prikazFajlova.clear()
        for i in range(len(fajlovi)):
            if fajlovi[i]!='':
                prikazFajlova.insert(i,fajlovi[i])

        if (len(prikazFajlova)!= 0):
            listaFajlova.delete(0,END)
            for i in range(len(prikazFajlova)):
                if(prikazFajlova[i]!=''):
                    listaFajlova.insert(i,prikazFajlova[i])

        else:
            print('Nema se nista prikazati')
        s.close();
        porukaSaServera=""
        g=""
        poruka=""
        fajlovi.clear()
        prikazFajlova.clear();
        print(listaFajlova.size())
        print(len(prikazFajlova))
        print(len(fajlovi))
def Obrisi():
    if listaPreuzetih.size()!=0:
        izabrani=listaPreuzetih.get(ACTIVE);
        if(os.path.exists((os.path.join(direktorijum+'/')))):
            if(izabrani!=''):
                os.remove(direktorijum+'/'+str(izabrani));
                listaPreuzetih.delete(ACTIVE)
                recnikIzbrisanih = {
                    "imeFajla": izabrani
                }
                obrisaniFajlovi.append(recnikIzbrisanih)
                if (os.path.exists(os.path.join(direktorijum,'podaci.json')) == 0):
                    fp = open(os.path.join(direktorijum,'podaci.json'), 'w')
                    json.dump(recnikIzbrisanih, fp)
                    fp.close();
                else:
                    fp = open(os.path.join(direktorijum,'podaci.json'), 'a+')
                    json.dump(recnikIzbrisanih, fp)
                    fp.close();
                n_torka = tuple(obrisaniFajlovi)
                print(n_torka)
                messagebox.showinfo('Poruka','Obrisano')
            else:
                messagebox.showinfo('Poruka','Izabrani fajl je obrisan nedavno')
        else:
            messagebox.showinfo('Poruka','Folder ne postoji');
    else:
        messagebox.showinfo('Poruka','Morate odabrati fajl')

    izabrani="";

def grafika():

    forma.minsize(width=500,height=800)
    forma.maxsize(width=500,height=800)
    forma.configure(bd=1, bg='#E1E2E1');

    imeFrame= Frame(forma, bd=1, bg='red', width=500, height=500);
    imeFont=font.Font(family="Verdana", size=20);
    ime=Label(imeFrame, bd=1,text='Klijent login', font=imeFont)

    poljaFont=font.Font(family="Verdana", size=20);

    ime.pack()
    imeFrame.pack();

    imeFrame.place(relx=0.82, rely=0.05, anchor=CENTER)

    naslovListeFrame=Frame(forma, bd=1, width=500, height=500);
    naslovListe=Label(naslovListeFrame, bd=1, text='Lista dostupnih', font=imeFont);

    naslovListe.pack();
    naslovListeFrame.pack();

    naslovListeFrame.place(relx=0.34,rely=0.1)

    items = [1, 2, 3, 4, 5]
    def sqr(x):
        return x ** 2
    nekiMap=list(map(sqr, items))
    print(nekiMap)

    global listaFajlova;

    listaFajlova.pack();
    prikaziButton = Button(listaFajlovaFrame, bd=1, bg='#00bfa5', fg='white', text='Prikazi', width=23, height=5, command=prikazi);
    prikaziButton.pack(side=LEFT);
    dodajButton=Button(listaFajlovaFrame, bd=1, bg='#00bfa5', fg='white', text='Preuzmi', width=23, height=5, command=preuzmi);
    dodajButton.pack();
    listaFajlovaFrame.pack();

    listaFajlovaFrame.place(relx=0.15,rely=0.2);

    naslovOnlineFrame=Frame(forma,bd=1, width=341)
    naslovOnline=Label(naslovOnlineFrame, bd=1,text='Lista preuzetih', font=imeFont);
    naslovOnline.pack();
    naslovOnlineFrame.pack();

    naslovOnlineFrame.place(relx=0.34,rely=0.55);

    global listaPreuzetih;

    listaPreuzetih.pack();
    obrisiButton=Button(listaPreuzetihFrame,bd=1,bg='#d50000', fg='white', text='Obrisi', width=47, height=5, command=Obrisi);
    obrisiButton.pack(side=LEFT);
    listaPreuzetihFrame.pack();


    listaPreuzetihFrame.place(relx=0.15,rely=0.65);
    i=0;



    if os.path.exists(os.path.join(direktorijum+'/')):
        for entry in os.listdir(direktorijum):
            if os.path.isfile(os.path.join(direktorijum, entry)):
                listaPreuzetih.insert(i,entry);
                i=i+1;

    forma.mainloop();

if __name__=='__main__':
    grafika();

