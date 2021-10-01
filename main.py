from tkinter import *
from tkinter import filedialog
import txtopp
import time
import encrypt_temp



def main():
    
    root = Tk()
    root.title('Encrypter')
    root.geometry('500x500')
    root.iconbitmap('icon/icon.ico')


    frame2 = LabelFrame(root, text='Command Centre', fg='white', bg='#212120')
    frame2.place(relheight=1, relwidth=1, relx=0, rely=0)

    textbox = Text(frame2, bg='#212120', bd=2, fg='white', font=("Times New Roman", 11, 'bold'), insertbackground='white')
    textbox.pack(expand=1, fill=BOTH)

    
    def enter(e=None):

        val = textbox.get('1.0', END)
        if val == 'decode file\n':

            filename = filedialog.askopenfilename(title='Upload File', defaultextension=(
                ("TXT Files", '*.txt'),
                ("DAT Files", '*.dat')), filetypes=(
                ("TXT Files", '*.txt'),
                ("DAT Files", '*.dat')))

            inval = txtopp.read_string(file=filename)
            textbox.insert(END, txtopp.read_string('files/decode note.txt'))
            outval = encrypt_temp.decode(inval)

            f = open(filename, 'w')
            f.write('')
            f.close()
            txtopp.add_object(file=filename, separator='\n', object=outval)



        elif val == 'encode file\n':
            filename = filedialog.askopenfilename(title='Upload File', defaultextension=(
                ("TXT Files", '*.txt'),
                ("DAT Files", '*.dat')), filetypes=(
                ("TXT Files", '*.txt'),
                ("DAT Files", '*.dat')))

            inval = txtopp.read_string(file=filename)
            textbox.insert(END, txtopp.read_string('files/encode note.txt'))
            outval = encrypt_temp.encode(inval)

            f = open(filename, 'w')
            f.write('')
            f.close()
            txtopp.add_object(file=filename, separator='\n', object=outval)

    def encode(e=None):
        textbox.delete('1.0', END)
        textbox.insert(END, 'encode file')
        enter()

    def decode(e=None):
        textbox.delete('1.0', END)
        textbox.insert(END, 'decode file')
        enter()


    textbox.bind('<Return>', enter)


    #--------------MENU-------------------------
    menu = Menu(root)
    root.config(menu=menu)
    file = Menu(menu, tearoff=0)
    menu.add_cascade(label='Codes', menu=file)
    file.add_command(label='Encode File', command=encode)
    file.add_command(label='Decode File', command=decode)

    root.bind('<Control-e>', encode)
    root.bind('<Control-d>', decode)


def sub(e=None):
    if entry.get() == password:
        win.destroy()
        main()




win = Tk()
win.title('Encrypter')
win.geometry('300x100')
win.iconbitmap('icon/icon.ico')

password='123'

Label(win, text='Password: ').grid(row=0, column=0)

entry = Entry(win, width=25, font=("Arial", 12), show='*')
entry.grid(row=0, column=1, pady=5)


entry.bind('<Return>', sub)


mainloop()