import socket;
import threading;
import os;

def RetrFile(name, sock):
    filename=sock.recv(1024).decode();
    if os.path.isfile(''+filename):
        sock.send(("EXISTS "+str(os.path.getsize(filename))).encode());
        userResponse=sock.recv(1024).decode();
        if userResponse[:2]=='OK':
            with open(filename,'rb') as f:
                bytesToSend=f.read();
                sock.send(bytesToSend);
                while bytesToSend!="":
                    bytesToSend=f.read();
                    sock.send(bytesToSend);
            f.close();
    else:
        sock.send("ERR".encode());
    sock.close();

def Main():
    host='127.0.0.1';
    port=5000;

    s=socket.socket();
    s.bind((host,port));

    s.listen(5);

    print("Server Started");
    global poruka;
    poruka='Cao';

    while True:
        for entry in os.listdir(''):
            if os.path.isfile(os.path.join('fajlovi', entry)):
                print(entry)
        c, addr=s.accept();
        print("Client connected ip:<"+str(addr)+">");
        print(poruka);
        c.send("cao".encode());

        t=threading.Thread(target=RetrFile, args=("retrThread",c));
        t.start();
    s.close();

if __name__=='__main__':
    Main();