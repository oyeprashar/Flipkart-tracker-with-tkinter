from tkinter import*
from tkinter import messagebox
import requests
import time
from time import ctime
from bs4 import BeautifulSoup
import pandas as pd 
from PIL import ImageTk, Image



root = Tk()
root.geometry("400x100")
root.title("Flipkart Price Tracker")
root.resizable(height=False, width=False)
root.iconbitmap("price.ico")
back_img = ImageTk.PhotoImage(Image.open("388275.jpg"))
back_label = Label(root, image=back_img)
back_label.place(x=0, y=0, relheight=1, relwidth=1)
global count
count = 0
def func_checkprice():
    try:
        global product_link
        global back_img1
        product_link = link.get()
        page =requests.get(product_link)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_name = soup.find(class_='_35KyD6').get_text()
        price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()
        # print(product_name ,price, ctime())
        product_window = Toplevel()
        product_window.geometry("200x200")
        product_window.iconbitmap("price.ico")
        back_img1 = ImageTk.PhotoImage(Image.open("388275.jpg"))
        back_label1 = Label(product_window, image=back_img1)
        back_label1.place(x=0, y=0, relheight=1, relwidth=1)
        details_name = Label(product_window , text=product_name, wraplength=120,padx=10)
        details_price = Label(product_window , text=price, wraplength=120)
        details_name.grid(row=0,column=0)
        details_price.grid(row=0,column=1)
        okay_button = Button(product_window, text="Okay", command=product_window.destroy)
        okay_button.grid(row=1, column=0, columnspan=2, ipadx=10, pady=5)
        link.delete(0,END)
    except:
        popup = messagebox.showerror("Error","Invalid Link") 
        
def func_write():
    global product_link
    try:
        product_link = link.get()
        page =requests.get(product_link)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_name = soup.find(class_='_35KyD6').get_text()
        price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()

    # print(product_name ,price, ctime() )
        product_details = pd.DataFrame({
            'Name':[product_name],
            'Price':[price],
            'Time':[time.ctime()],
            }
            
                )

        product_details.to_csv('flipkart_scrapper_gui.csv', mode='a', header=False)
        link.delete(0,END)
        popup1 = messagebox.showinfo("Success", "Successfully written to CSV file")
    except:
        popup = messagebox.showerror("Error", "Invalid Link")
    
link = Entry(root, border=3)
link.insert(0,"Link")
link.grid(row=0, column=0,columnspan=2,ipadx=80, padx=(50,0),pady=5)

check_price = Button(root, text="Check Price", command=func_checkprice)
check_price.grid(row=1, column=0,padx=(70,0))
write = Button(root, text="Write to CSV", command=func_write)
write.grid(row=1, column=1,padx=(1,50))

root.mainloop()
