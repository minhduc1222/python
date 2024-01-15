from tkinter import *



window = Tk()
window.geometry('600x400')

book_list = {'Harry porter': ['J.k. Rowling', 1200, 30], 
             'The old man and the sea': ['Hermingway', 300, 10]}

def box_selected(event):
    
    name = listbox_book.curselection()[0]
    book_info = listbox_book.get(name)
    author = book_list[book_info][0]
    page = book_list[book_info][1]
    price = book_list[book_info][2]
    insert(author, page, price)
    
def insert(author, page, price):
    en_author.delete(0, END)
    en_page.delete(0, END)
    en_price.delete(0, END)
    
    en_author.insert(0, author)
    en_page.insert(0, page)
    en_price.insert(0, price)
    
    

lbl_book = Label(window, text='Book')
lbl_book.grid(row = 0, column=0, sticky=W, padx= 5, pady=5)

listbox_book = Listbox(window, width=40, height=10)
listbox_book.insert(END, *book_list)
listbox_book.grid(row = 1, column=0, rowspan=5, columnspan=2, padx= 15, pady=20)
listbox_book.bind('<<ListboxSelect>>', box_selected)

lbl_author = Label(window, text='author')
lbl_author.grid(row = 1, column=2, sticky=NW)
en_author = Entry(window, width=20)
en_author.grid(row=2, column=2, sticky=W)

lbl_page = Label(window, text='page')
lbl_page.grid(row = 3, column=2, sticky=W)
en_page = Entry(window, width=20)
en_page.grid(row=4, column=2, sticky=W)
lbl_price = Label(window, text='price')
lbl_price.grid(row = 5, column=2, sticky=W)
en_price = Entry(window, width=20)
en_price.grid(row=6, column=2, sticky=W)
window.mainloop()