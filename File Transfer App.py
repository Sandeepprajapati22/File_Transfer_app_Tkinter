from tkinter import*
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root=Tk()
root.title("Share Anywhere")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

def send():
    window=Toplevel(root)
    window.title("send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='select Image File',
                                            filetypes=(('file_type','*.txt'),('all files','*.*')))

    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections...........')
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transitted successfully..")

    #icon
    image_icon1=PhotoImage(file="Images/send.png")
    window.iconphoto(False,image_icon1)

    sbackground = Image.open("Images/sender.png")
    sbackground = sbackground.resize((450, 250))
    sbackground = ImageTk.PhotoImage(sbackground)
    Label(window, image=sbackground).place(x=0, y=0)

    mbackground = Image.open("Images/ID.png")
    mbackground = mbackground.resize((250, 150))
    mbackground = ImageTk.PhotoImage(mbackground)
    Label(window, image=mbackground, bg="#f4fdfe").place(x=100, y=260)

    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg='white',fg='black').place(x=140,y=290)
          
    Button(window,text="+ Select file",width=10,height=1,font="arial 14 bold",bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font="arial 14 bold",bg="#000",fg="#fff",command=sender).place(x=300,y=150)

    window.mainloop()

def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID=SenderID.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print('File has been received successfully')
        

    #icon
    image_icon1=PhotoImage(file="Images/receive.png")
    main.iconphoto(False,image_icon1)

    Hbackground=Image.open("Images/receiver.png")
    Hbackground=Hbackground.resize((450,250))
    Hbackground=ImageTk.PhotoImage(Hbackground)
    Label(main,image=Hbackground,bg="#f4fdfe").place(x=0,y=0)
    
    logo=Image.open("Images/profile.png")
    logo=logo.resize((100,100))
    logo=ImageTk.PhotoImage(logo)
    Label(main,image=logo,bg="#f4fdfe").place(x=175,y=270)

    Label(main,text="Receive",font=("arial",20,"bold"),bg="#f4fdfe",fg="black").place(x=170,y=375)

    Label(main,text="Input Sender ID",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=410)
    SenderID=Entry(main,width=25,fg="black",border=2,bg="white",font=("arial",15))
    SenderID.place(x=20,y=435)
    SenderID.focus()

    Label(main,text="filename for the incoming file:",font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=475)
    incoming_file=Entry(main,width=25,fg="black",border=2,bg="white",font=("arial",15))
    incoming_file.place(x=20,y=500)

    arrow_img = Image.open("Images/arrow.png")
    arrow_img = arrow_img.resize((30, 30))
    imageicon = ImageTk.PhotoImage(arrow_img)
    rr = Button(main,text="Receive",image=imageicon,compound=LEFT,bg="#39c790",fg="black",font=("arial", 12, "bold"),bd=0,padx=8,pady=5,command=receiver)
    rr.place(x=290, y=490)                    
    
                         
    main.mainloop()

#icon
image_icon=PhotoImage(file="Images/shareit.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=("Acumin Variable Concept",20,"bold"),bg="#f4fdfe").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)


send_img = Image.open("Images/send.png")
send_img = send_img.resize((100,100))
send_image = ImageTk.PhotoImage(send_img)
send = Button(root,image=send_image,bg="#f4fdfe",bd=0,command=send)
send.place(x=50,y=100)

receive_img = Image.open("Images/receive.png")
receive_img = receive_img.resize((100,100))
receive_image = ImageTk.PhotoImage(receive_img)
receive = Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)

#Label
Label(root,text="send",font=("Acumin variable Concept",17,"bold"),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=("Acumin variable Concept",17,"bold"),bg="#f4fdfe").place(x=300,y=200)

background = Image.open("Images/background.png")
background = background.resize((450,260))
background = ImageTk.PhotoImage(background)

Label(root,image=background).place(x=0,y=300)

root.mainloop()






'''#With the help of this tool we can send and receive file. It is  simple, best and easy to use.
For sender , 1.)open app and click on send  2.) then browse file  3.) click on send 
For receiver  1.) open app and click on receive  2.) then type Sender ID  3.)  input incoming filename for file.
Also Both system should be connected on same network.'''

