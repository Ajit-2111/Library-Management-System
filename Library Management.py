from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os
from tkinter import messagebox, ttk
import datetime as dt
from time import strftime



def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


def entry():
    import os
    f_p = r"./attendance.csv"
    # check if file is available in the file system
    if not os.path.isfile(f_p):
        with open(f_p, "a") as f:
            f.write('date,regno,entry,exit')
            print('Empty text file was just created at {}.'.format(f_p))
            f.write(f"\n{date:%d/%m/%Y},{regid.get()},{strftime('%H:%M:%S')}")
            messagebox.showinfo("showinfo", f"{regid.get()} entered at {strftime('%H:%M:%S')}")
            regid.delete(0, END)
    else:
        with open(f_p, "a") as f:
            f.write(f"\n{date:%d/%m/%Y},{regid.get()},{strftime('%H:%M:%S')}")
            messagebox.showinfo("showinfo", f"{regid.get()} entered at {strftime('%H:%M:%S')}")
            regid.delete(0, END)


def exit():
    import pandas as pd
    try:
        df = pd.read_csv("./attendance.csv")
        df.loc[(df['regno'] == int(regid.get())) & (df['date'] == f"{date:%d/%m/%Y}"), 'exit'] = strftime('%H:%M:%S')
        df.to_csv("./attendance.csv", encoding='utf-8', index=False)
        messagebox.showinfo("showinfo", f"{regid.get()} left at {strftime('%H:%M:%S')}")
        regid.delete(0, END)
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")


def attendance():
    global regid, lbl, date
    # Create an instance of tkinter
    try:
        win.destroy
    except :
        pass

    win = Toplevel()
    win.title("Attendance Monitoring")
    win.geometry("700x500")
    style = ttk.Style(win)
    style.configure('My.TEntry', padding=(10, 2, 2, 0))

    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()

    # put image in a label and place label as background
    imgTemp = Image.open("image2 - Edited.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(win, image=img)
    label.pack(side='top', fill=Y, expand=True)

    headingFrame1 = Frame(win, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.02, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Attendance Monitoring", bg='black', fg='white',
                         font=('Roboto', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    date = dt.datetime.now()
    # Create Label to display the Date
    label = Label(win, text=f"{date:%A, %B %d, %Y}", font=('Roboto', 18, 'bold'), bg='black', fg='white', borderwidth=7,
                  relief="raised")
    # label.pack(pady=20)
    label.place(relx=0.15, rely=0.18, relwidth=0.7, relheight=0.1)

    lbl = Label(win, font=('Roboto', 18, 'bold'), background='purple', foreground='white')
    # lbl.pack(anchor='center')
    lbl.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.1)

    time()

    # Canvas1 = Canvas(win)

    labelFrame = Frame(win, bg='black', highlightbackground="#42413f", highlightthickness=4)
    labelFrame.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.2)

    lb1 = Label(labelFrame, text="Registration No : ", bg='black', fg='white', font=('Roboto', 13))
    lb1.place(relx=0.05, rely=0.3, relheight=0.45)

    regid = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    regid.place(relx=0.35, rely=0.3, relwidth=0.62, relheight=0.40)

    enterBtn = Button(win, text="Entry", bg='#4CAF50', fg='black', activebackground='#39853c', command=entry,
                      borderwidth=7, relief="raised", font=('Roboto', 13))
    enterBtn.place(relx=0.2, rely=0.68, relwidth=0.18, relheight=0.12)

    exitBtn = Button(win, text="Exit", bg='#f44336', fg='black', activebackground='#a82c23', command=exit,
                     borderwidth=7, relief="raised", font=('Roboto', 13))
    exitBtn.place(relx=0.6, rely=0.68, relwidth=0.18, relheight=0.12)

    quitBtn = Button(win, text="Quit", bg='#f7f1e3', fg='black', command=win.destroy, borderwidth=7, relief="raised",
                     font=('Roboto', 13))
    quitBtn.place(relx=0.4, rely=0.85, relwidth=0.18, relheight=0.08)

    win.mainloop()



def search(tree, text):
    for child in tree.get_children():
        if text in tree.item(child)["values"] or tree.item(child)["values"] == ['', '', '', '']:
            pass
        else:
            tree.delete(child)


def reset(newWindow, root, bookTable):
    newWindow.destroy()
    openNewWindow(root, bookTable)


def openNewWindow(root, bookTable):
    print(bookTable)
    newWindow = Toplevel(root)
    width = newWindow.winfo_screenwidth()
    height = newWindow.winfo_screenheight()

    # put image in a label and place label as background
    imgTemp = Image.open("image2 - Edited.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)
    label = Label(newWindow, image=img)
    label.pack(side='top', fill=Y, expand=True)

    style = ttk.Style(newWindow)
    style.configure('My.TEntry', padding=(10, 2, 2, 0))
    style.theme_use('clam')
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Roboto', 11), rowheight=30)
    style.configure("mystyle.Treeview.Heading", font=('Roboto', 13, 'bold'))
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
    newWindow.title(bookTable)
    newWindow.minsize(width=400, height=400)
    newWindow.geometry("600x500")

    headingFrame1 = Frame(newWindow, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.09, rely=0.1, relwidth=0.85, relheight=0.13)

    headingLabel = Label(headingFrame1, text='All Books' if bookTable == 'books' else bookTable.replace('_',
                                                                                                        " ").capitalize() + ' Books',
                         bg='black', fg='white', font=('Roboto', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    tree_frame = Frame(newWindow)
    tree_frame.place(relx=0.5, rely=0.5, relwidth=0.9, height=250, anchor=CENTER)
    tree_frame.configure(bg="white")
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, style="mystyle.Treeview")

    my_tree.place(relx=0, relwidth=0.97)
    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('BID', 'Title', 'Author', 'Status')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('BID', width=120)
    my_tree.column('Title', width=120)
    my_tree.column('Author', width=120)
    my_tree.column('Status', width=120)

    my_tree.heading('#0', text='')
    my_tree.heading('BID', text='BID')
    my_tree.heading('Title', text='Title')
    my_tree.heading('Author', text='Author')
    my_tree.heading('Status', text='Status')

    getBooks = "select * from " + bookTable
    booklist = []
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            booklist.append(i)
    except:
        messagebox.showinfo("Failed to fetch files from database")
    count = 0
    for i in booklist:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(i[0], i[1], i[2], i[3]), tags=('odd',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(i[0], i[1], i[2], i[3]), tags=('even',))
        count += 1
    my_tree.insert(parent='', index='end', text='', values=('', '', '', ''))
    my_tree.insert(parent='', index='end', text='', values=('', '', '', ''))
    my_tree.insert(parent='', index='end', text='', values=('', '', '', ''))

    searchlbl = Label(newWindow, text="  Search Query :  ", bg='black', fg='white', font=('Roboto', 11))
    searchlbl.place(relx=0.05, rely=0.8, relheight=0.08)

    searchinp = ttk.Entry(newWindow, style='My.TEntry', font=('Roboto', 11))
    searchinp.place(relx=0.28, rely=0.8, relwidth=0.4, relheight=0.08)

    searchBtn = Button(newWindow, text="Search", bg='#f7f1e3', fg='black',
                       command=lambda: search(my_tree, searchinp.get()), borderwidth=7, relief="raised",
                       font=('Roboto', 13))
    searchBtn.place(relx=0.7, rely=0.8, relwidth=0.12, relheight=0.08)

    searchResetBtn = Button(newWindow, text="Reset", bg='#f7f1e3', fg='black',
                            command=lambda: reset(newWindow, root, bookTable), borderwidth=7, relief="raised",
                            font=('Roboto', 13))
    searchResetBtn.place(relx=0.83, rely=0.8, relwidth=0.12, relheight=0.08)

    quitBtn = Button(newWindow, text="Quit", bg='#f7f1e3', fg='black', command=newWindow.destroy, borderwidth=7,
                     relief="raised", font=('Roboto', 13))
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    newWindow.mainloop()


def View():
    deptlist = ["COMPUTER SCIENCE ENGINEERING", "ELECTRICAL ENGINEERING", "ELECTRONICS ENGINEERING",
                "ELECTRONICS AND TELECOMMUNICATION", "INFORMATION TECHNOLOGY", "MECHANICAL ENGINEERING",
                'CHEMICAL ENGINEERING', 'FIRST YEAR ENGINEERING', 'MASTER OF COMPUTER APPLICATION']
    root = Toplevel()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("650x500")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # put image in a label and place label as background
    imgTemp = Image.open("image2 - Edited.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(root, image=img)
    label.pack(side='top', fill=Y, expand=True)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="  View Books", bg='black', fg='white', font=('Roboto', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root, text="COMPUTER SCIENCE ENGINEERING", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'COMPUTER_SCIENCE_ENGINEERING'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn1.place(relx=0.2, rely=0.23, relwidth=0.6, relheight=0.065)

    btn2 = Button(root, text="ELECTRICAL ENGINEERING", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'ELECTRICAL_ENGINEERING'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn2.place(relx=0.2, rely=0.30, relwidth=0.6, relheight=0.065)

    btn3 = Button(root, text="ELECTRONICS ENGINEERING", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'ELECTRONICS_ENGINEERING'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn3.place(relx=0.2, rely=0.37, relwidth=0.6, relheight=0.065)

    btn4 = Button(root, text="ELECTRONICS AND TELECOMMUNICATION", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'ELECTRONICS_AND_TELECOMMUNICATION'), borderwidth=7,
                  relief="raised", font=('Roboto', 11))
    btn4.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.065)

    btn5 = Button(root, text="INFORMATION TECHNOLOGY", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'INFORMATION_TECHNOLOGY'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn5.place(relx=0.2, rely=0.51, relwidth=0.6, relheight=0.065)

    btn6 = Button(root, text="MECHANICAL ENGINEERING", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'MECHANICAL_ENGINEERING'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn6.place(relx=0.2, rely=0.58, relwidth=0.6, relheight=0.065)

    btn7 = Button(root, text="CHEMICAL ENGINEERING", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'CHEMICAL_ENGINEERING'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn7.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.065)

    btn8 = Button(root, text="FIRST YEAR ENGINEERING", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'FIRST_YEAR_ENGINEERING'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn8.place(relx=0.2, rely=0.72, relwidth=0.6, relheight=0.065)

    btn9 = Button(root, text="MASTER OF COMPUTER APPLICATION", bg='black', fg='white',
                  command=lambda: openNewWindow(root, 'MASTER_OF_COMPUTER_APPLICATION'), borderwidth=7, relief="raised",
                  font=('Roboto', 11))
    btn9.place(relx=0.2, rely=0.79, relwidth=0.6, relheight=0.065)

    btn10 = Button(root, text="All Books", bg='black', fg='white', command=lambda: openNewWindow(root, 'books'),
                   borderwidth=7, relief="raised", font=('Roboto', 11))
    btn10.place(relx=0.2, rely=0.86, relwidth=0.6, relheight=0.065)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy, borderwidth=7, relief="raised",
                     font=('Roboto', 13))
    quitBtn.place(relx=0.42, rely=0.925, relwidth=0.18, relheight=0.07)

    root.mainloop()


def deptReturn(bid, deptbookTable):
    checkAvail = "update " + deptbookTable + " set status = 'avail' where bid = '" + bid + "'"
    cur.execute(checkAvail)
    con.commit()


def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    bid = bookInfo1.get()
    deptbookTable = menu.get().replace(' ', '_')

    extractBid = "select bid from " + issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "delete from " + issueTable + " where bid = '" + bid + "'"

    updateStatus = "update " + bookTable + " set status = 'avail' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            deptReturn(bid, deptbookTable)
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()
    root.destroy()


def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1, menu

    root = Toplevel()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    style = ttk.Style(root)
    style.configure('My.TEntry', padding=(10, 2, 2, 0))
    # put image in a label and place label as background
    imgTemp = Image.open("image2 - Edited.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(root, image=img)
    label.pack(side='top', fill=Y, expand=True)

    # Canvas1 = Canvas(root)
    #
    # Canvas1.config(bg="#006B38")
    # Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Roboto', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black', highlightbackground="#42413f", highlightthickness=4)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Roboto', 11))
    lb1.place(relx=0.05, rely=0.15, relheight=0.12)

    bookInfo1 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    bookInfo1.place(relx=0.3, rely=0.15, relwidth=0.62, relheight=0.12)
    import tkinter.font as tkFont
    robo11 = tkFont.Font(family='Roboto', size=11)
    lb5 = Label(labelFrame, text="Department : ", bg='black', fg='white', font=('Roboto', 11))
    lb5.place(relx=0.05, rely=0.4, relheight=0.12)
    menu = StringVar(labelFrame)
    menu.set("Select Department")

    drop = OptionMenu(labelFrame, menu, "COMPUTER SCIENCE ENGINEERING", "ELECTRICAL ENGINEERING",
                      "ELECTRONICS ENGINEERING", "ELECTRONICS AND TELECOMMUNICATION", "INFORMATION TECHNOLOGY",
                      "MECHANICAL ENGINEERING", 'CHEMICAL ENGINEERING', 'FIRST YEAR ENGINEERING',
                      'MASTER OF COMPUTER APPLICATION')
    drop.place(relx=0.3, rely=0.4)
    drop.config(font=robo11)
    mainmenu = root.nametowidget(drop.menuname)  # Get menu widget.
    mainmenu.config(font=robo11)

    # Submit Button
    SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=returnn, borderwidth=7, relief="raised",
                       font=('Roboto', 13))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy, borderwidth=7, relief="raised",
                     font=('Roboto', 13))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def deptIssue(bid, deptbookTable):
    checkAvail = "update " + deptbookTable + " set status = 'issued' where bid = '" + bid + "'"
    cur.execute(checkAvail)
    con.commit()


def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()
    deptbookTable = menu.get().replace(' ', '_')
    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select bid from " + bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "insert into " + issueTable + " values ('" + bid + "','" + issueto + "')"
    show = "select * from " + issueTable

    updateStatus = "update " + bookTable + " set status = 'issued' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            deptIssue(bid, deptbookTable)
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()


def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status, menu

    root = Toplevel()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    style = ttk.Style(root)
    style.configure('My.TEntry', padding=(10, 2, 2, 0))
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # put image in a label and place label as background
    imgTemp = Image.open("image2 - Edited.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(root, image=img)
    label.pack(side='top', fill=Y, expand=True)

    # Canvas1 = Canvas(root)
    # Canvas1.config(bg="#D6ED17")
    # Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Roboto', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black', highlightbackground="#42413f", highlightthickness=4)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Roboto', 11))
    lb1.place(relx=0.05, rely=0.15, relheight=0.12)

    inf1 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    inf1.place(relx=0.3, rely=0.15, relwidth=0.62, relheight=0.12)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white', font=('Roboto', 11))
    lb2.place(relx=0.05, rely=0.3, relheight=0.12)

    inf2 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    inf2.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.12)
    import tkinter.font as tkFont
    robo11 = tkFont.Font(family='Roboto', size=11)
    lb5 = Label(labelFrame, text="Department : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.45, relheight=0.12)
    menu = StringVar(labelFrame)
    menu.set("Select Department")

    drop = OptionMenu(labelFrame, menu, "COMPUTER SCIENCE ENGINEERING", "ELECTRICAL ENGINEERING",
                      "ELECTRONICS ENGINEERING", "ELECTRONICS AND TELECOMMUNICATION", "INFORMATION TECHNOLOGY",
                      "MECHANICAL ENGINEERING", 'CHEMICAL ENGINEERING', 'FIRST YEAR ENGINEERING',
                      'MASTER OF COMPUTER APPLICATION')
    drop.place(relx=0.3, rely=0.45)
    drop.config(font=robo11)
    mainmenu = root.nametowidget(drop.menuname)  # Get menu widget.
    mainmenu.config(font=robo11)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue, borderwidth=7, relief="raised",
                      font=('Roboto', 13))
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy, borderwidth=7, relief="raised",
                     font=('Roboto', 13))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()

def deleteBook():
    bid = bookInfo1.get()

    deleteSql = "delete from " + bookTable + " where bid = '" + bid + "'"
    deleteIssue = "delete from " + issueTable + " where bid = '" + bid + "'"
    deleteDept = "delete from " + menu.get().replace(' ', '_') + " where bid = '" + bid + "'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        cur.execute(deleteDept)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    bookInfo1.delete(0, END)
    root.destroy()


def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root, menu

    root = Toplevel()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    style = ttk.Style(root)
    style.configure('My.TEntry', padding=(10, 2, 2, 0))
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # put image in a label and place label as background
    imgTemp = Image.open("image2 - Edited.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(root, image=img)
    label.pack(side='top', fill=Y, expand=True)

    # Canvas1 = Canvas(root)
    #
    # Canvas1.config(bg="#006B38")
    # Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Roboto', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black', highlightbackground="#42413f", highlightthickness=4)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Roboto', 11))
    lb2.place(relx=0.05, rely=0.15, relheight=0.12)

    bookInfo1 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    bookInfo1.place(relx=0.3, rely=0.15, relwidth=0.62, relheight=0.12)
    import tkinter.font as tkFont
    robo11 = tkFont.Font(family='Roboto', size=11)
    lb5 = Label(labelFrame, text="Department : ", bg='black', fg='white', font=('Roboto', 11))
    lb5.place(relx=0.05, rely=0.4, relheight=0.12)
    menu = StringVar(labelFrame)
    menu.set("Select Department")

    drop = OptionMenu(labelFrame, menu, "COMPUTER SCIENCE ENGINEERING", "ELECTRICAL ENGINEERING",
                      "ELECTRONICS ENGINEERING", "ELECTRONICS AND TELECOMMUNICATION", "INFORMATION TECHNOLOGY",
                      "MECHANICAL ENGINEERING", 'CHEMICAL ENGINEERING', 'FIRST YEAR ENGINEERING',
                      'MASTER OF COMPUTER APPLICATION')
    drop.place(relx=0.3, rely=0.4)
    drop.config(font=robo11)
    mainmenu = root.nametowidget(drop.menuname)  # Get menu widget.
    mainmenu.config(font=robo11)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteBook, borderwidth=7,
                       relief="raised", font=('Roboto', 13))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy, borderwidth=7, relief="raised",
                     font=('Roboto', 13))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    options = menu.get().replace(' ', '_')

    insertBooks = "insert into " + bookTable + " values('" + bid + "','" + title + "','" + author + "','" + status + "')"
    insertBooksDept = "insert into " + options + " values('" + bid + "','" + title + "','" + author + "','" + status + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        cur.execute(insertBooksDept)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)
    print(options)

    root.destroy()


def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root, menu

    root = Toplevel()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    style = ttk.Style(root)
    style.configure('My.TEntry', padding=(10, 2, 2, 0))
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # put image in a label and place label as background
    imgTemp = Image.open("image2 - Edited.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(root, image=img)
    label.pack(side='top', fill=Y, expand=True)

    bookTable = "books"  # Book Table

    # Canvas1 = Canvas(root)
    #
    # Canvas1.config(bg="#ff6e40")
    # Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Roboto', 20, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black', highlightbackground="#42413f", highlightthickness=4)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Roboto', 11))
    lb1.place(relx=0.05, rely=0.1, relheight=0.12)

    bookInfo1 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    bookInfo1.place(relx=0.35, rely=0.1, relwidth=0.62, relheight=0.12)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white', font=('Roboto', 11))
    lb2.place(relx=0.05, rely=0.25, relheight=0.12)

    bookInfo2 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    bookInfo2.place(relx=0.35, rely=0.25, relwidth=0.62, relheight=0.12)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white', font=('Roboto', 11))
    lb3.place(relx=0.05, rely=0.4, relheight=0.12)

    bookInfo3 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    bookInfo3.place(relx=0.35, rely=0.4, relwidth=0.62, relheight=0.12)

    import tkinter.font as tkFont
    robo11 = tkFont.Font(family='Roboto', size=11)

    lb5 = Label(labelFrame, text="Department : ", bg='black', fg='white', font=('Roboto', 11))
    lb5.place(relx=0.05, rely=0.57, relheight=0.12)
    menu = StringVar(labelFrame)
    menu.set("Select Department")

    drop = OptionMenu(labelFrame, menu, "COMPUTER SCIENCE ENGINEERING", "ELECTRICAL ENGINEERING",
                      "ELECTRONICS ENGINEERING", "ELECTRONICS AND TELECOMMUNICATION", "INFORMATION TECHNOLOGY",
                      "MECHANICAL ENGINEERING", 'CHEMICAL ENGINEERING', 'FIRST YEAR ENGINEERING',
                      'MASTER OF COMPUTER APPLICATION')
    drop.place(relx=0.35, rely=0.57)
    drop.config(font=robo11)
    mainmenu = root.nametowidget(drop.menuname)  # Get menu widget.
    mainmenu.config(font=robo11)

    # Book Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white', font=('Roboto', 11))
    lb4.place(relx=0.05, rely=0.75, relheight=0.12)

    bookInfo4 = ttk.Entry(labelFrame, style='My.TEntry', font=('Roboto', 11))
    bookInfo4.place(relx=0.35, rely=0.75, relwidth=0.62, relheight=0.12)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister, borderwidth=7,
                       relief="raised", font=('Roboto', 13))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy, borderwidth=7, relief="raised",
                     font=('Roboto', 13))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()




allBid = []
issueTable = "books_issued"
bookTable = "books"  # Book Table
path = './database'
tableList = ['books', 'FIRST_YEAR_ENGINEERING', 'COMPUTER_SCIENCE_ENGINEERING', 'ELECTRICAL_ENGINEERING',
             'ELECTRONICS_ENGINEERING', 'ELECTRONICS_AND_TELECOMMUNICATION', 'INFORMATION_TECHNOLOGY',
             'MECHANICAL_ENGINEERING', 'CHEMICAL_ENGINEERING', 'MASTER_OF_COMPUTER_APPLICATION']
isExist = os.path.exists(path)
if isExist:
    if os.path.exists("./database/db.db"):
        try:
            sqliteConnection = sqlite3.connect('./database/db.db')
            sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
            cursor = sqliteConnection.cursor()
            tables = cursor.execute(sql_query)
            tblist = [i[0] for i in tables]
            print('tblist : ', tblist)
            temp3 = []
            for element in tableList:
                if element not in tblist:
                    temp3.append(element)
            print('Temp3 : ', temp3)
            if len(temp3) == 0:
                pass
            else:
                for i in range(len(temp3)):
                    if temp3[i] == 'books_issued':
                        cursor.execute('create table books_issued(bid varchar(20) primary key, issuedto varchar(30))')
                    else:
                        query = "create table " + temp3[
                            i] + "(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30))"
                        cursor.execute(query)
            cursor.execute(sql_query)
            print(cursor.fetchall())

        except sqlite3.Error as error:
            print("Failed to execute the above query", error)
    else:
        conn = sqlite3.connect('./database/db.db')
        for i in range(len(tableList)):
            query = "create table " + tableList[
                i] + "(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30))"
            conn.execute(query)
        conn.execute('create table books_issued(bid varchar(20) primary key, issuedto varchar(30))')

else:
    os.mkdir('./database')
    conn = sqlite3.connect('./database/db.db')
    for i in range(len(tableList)):
        query = "create table " + tableList[
            i] + "(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30))"
        conn.execute(query)
    conn.execute('create table books_issued(bid varchar(20) primary key, issuedto varchar(30))')


mydatabase = "./database/db.db"
con = sqlite3.connect(mydatabase)
cur = con.cursor()
root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


image = Image.open('image2 - Edited.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="FAMT Library", bg='black', fg='white', font=('Roboto', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook, borderwidth=7, relief="raised",
              font=('Roboto', 11))
btn1.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete, borderwidth=7, relief="raised",
              font=('Roboto', 11))
btn2.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View, borderwidth=7, relief="raised",
              font=('Roboto', 11))
btn3.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook, borderwidth=7,
              relief="raised", font=('Roboto', 11))
btn4.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook, borderwidth=7, relief="raised",
              font=('Roboto', 11))
btn5.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Attendance Monitor", bg='black', fg='white', command=attendance, borderwidth=7,
              relief="raised", font=('Roboto', 11))
btn6.place(relx=0.28, rely=0.85, relwidth=0.45, relheight=0.1)

root.mainloop()
