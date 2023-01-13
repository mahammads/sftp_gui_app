from tkinter import *  
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from sftp_module import SftpModule
from PIL import ImageTk, Image

base = Tk()  
base.geometry("450x400")  
base.title("SFTP")  

title = Label(base, text="SFTP DATA TRANSFER", width=30,font=("bold",12),fg='brown',bg ='white')   
title.place(x=80,y=10) 
file_name = ''
folder_name = ''

def browse_file():
    global file_name
    file = filedialog.askopenfilename()
    file_name = file
    lbl_file_name = Label(base, text=file_name, width=60, font=("arial",8),fg='blue',borderwidth=2, relief="raised",justify= LEFT)  
    lbl_file_name.place(x=40,y=200)

def browse_folder():
    global file_name
    folder = filedialog.askdirectory()
    folder_name = folder
    lbl_file_name = Label(base, text=folder_name, width=60, font=("arial",8),fg='blue',borderwidth=2, relief="raised",justify= LEFT)  
    lbl_file_name.place(x=40,y=200)

def sftp_upload():
    myclick()
    pass

def sftp_download():
    pass

def show():
   p = pswd_entry.get()
   Label(base, text= str(p)).place(x=330, y=100)

image=Image.open('password_icon.jpg')
img=image.resize((15, 15))
pw_img = ImageTk.PhotoImage(img)

Button(base, text="",image=pw_img,command=show).place(x=310,y=100)

horizontal =Frame(base, bg='black', height=1,width=440)
horizontal.place(x=5, y=300)

sftp_host= Label(base, text="Hostname:", width=10, font=("arial",10))  
sftp_host.place(x=80, y=50)  
host_entry= Entry(base,width=20)  
host_entry.place(x=180, y=50)  

sftp_user= Label(base, text="Username:", width=10, font=("arial",10))  
sftp_user.place(x=80, y=75)  
user_entry= Entry(base,width=20)  
user_entry.place(x=180, y=75)  

sftp_pswd= Label(base, text="Password:", width=10, font=("arial",10))  
sftp_pswd.place(x=80, y=100)  
pswd_entry= Entry(base,width=20,show="*")  
pswd_entry.place(x=180, y=100)  

sftp_port= Label(base, text="Port:", width=10, font=("arial",10))  
sftp_port.place(x=80, y=125)  
port_entry= Entry(base,width=20)  
port_entry.place(x=180, y=125)  

local_file= Label(base, text="Local File/Folder", width=15, font=("arial",10))  
local_file.place(x=40, y=200)  
local_entry= Entry(base,width=40)  
local_entry.place(x=180, y=200) 

sftp_file= Label(base, text="Remote File/Folder", width=15, font=("arial",9))  
sftp_file.place(x=40, y=170)  
file_entry= Entry(base,width=40)  
file_entry.place(x=180, y=170)  


def myclick():
    print(file_name)
    host_name = host_entry.get()
    user_name = user_entry.get()
    password = pswd_entry.get()
    port = port_entry.get()

    print(host_name)
    print(user_name)
    print(password)  
    print(port)  
    try:
        obj = SftpModule(host_name,user_name,password,int(port))
    except ValueError as e:
        # raise e
        error_lbl = Label(base, text="Error: Values missing in input field", width=40,font=("arial",10))
        error_lbl.place(x=50, y=310) 

 
Button(base, text='Browse File', width=12,font=("arial",9),command = lambda:browse_file(), fg='white',bg ='brown').place(x=110,y=240)
lbl_or= Label(base, text="or", width=2, font=("arial",10))  
lbl_or.place(x=205, y=240)  
Button(base, text='Browse Folder', width=12,font=("arial",9),command = lambda:browse_folder(), fg='white',bg ='brown').place(x=225,y=240) 



Button(base, text="Upload", command= sftp_upload, width=12,bg="brown",fg='white').place(x=40,y=320)
Button(base, text="Download", command= sftp_download, width=12,bg="brown",fg='white').place(x=150,y=320)
Button(base, text="Delete", command= sftp_download, width=12,bg="brown",fg='white').place(x=260,y=320)

base.mainloop()  