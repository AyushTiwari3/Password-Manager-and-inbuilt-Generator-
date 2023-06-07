from tkinter import *
import random
from tkinter import messagebox #################333
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    Password=""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    for n in range(1,nr_letters+1):
        Password+=random.choice(letters)
    
    for n in range(1,nr_symbols+1):
        Password+=random.choice(symbols)
        
    for n in range(1,nr_numbers+1):
        Password+=random.choice(numbers)
    pass_word=Password
    pyperclip.copy(pass_word)


    input_pass.insert(0,pass_word)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    a=input_website.get()
    b=input_name.get()
    c=input_pass.get()
     
    if len(a)==0 or len(b)==0 or len(c)==0:
        messagebox.showerror(title="Oops",message=f"Plese don't leave any fields empyty")
    
    else:
        is_ok=messagebox.askokcancel(title=a,message=f"These are the details entered: \nEmail: {b} \nPassword: {c} ")

        if is_ok:
            with open("day29file.txt",mode="a") as file:
                file.write(a)
                file.write(" | ")
                file.write(b)
                file.write(" | ")
                file.write(c)
                file.write("\n")
            input_website.delete(0,END)
            input_name.delete(0,END)
            input_pass.delete(0,END)
        else:
            input_website.delete(0,END)
            input_name.delete(0,END)
            input_pass.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
#Window made

windows=Tk()
windows.config(padx=50,pady=50)


#Canvas and image added

canvas=Canvas(width=220,height=224)
my_pass_logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_pass_logo)
canvas.grid(row=0,column=1)

#Lables

my_label_website=Label(text="Website:",font=("Courier",15,"bold"))
my_label_website.config(padx=10,pady=10)
my_label_website.grid(row=1,column=0)


my_label_name=Label(text="Email/Username:",font=("Courier",15,"bold"))
my_label_name.config(padx=10,pady=10)
my_label_name.grid(row=2,column=0)

my_label_pass=Label(text="Password:",font=("Courier",15,"bold"))
my_label_pass.config(padx=10,pady=10)
my_label_pass.grid(row=3,column=0)

#Buttons

generate_button=Button(text="Generate Password",command=generate_pass)
generate_button.place(x=455,y=335)

add_button=Button(text="Add",width=50,command=add_info)
add_button.grid(row=4,column=1)


#FOR ENTRYYYYYYY
# 
input_website=Entry(width=60)
print(input_website.get())
input_website.grid(row=1,column=1)

input_name=Entry(width=60)
print(input_name.get())
input_name.grid(row=2,column=1)

#IF WANT E-MAIL SAVED
# input_name=Entry(width=60)
# print(input_name.get())
# input_name.insert(0,"PUT YOUR E-MAIL HERE")
# input_name.grid(row=2,column=1)


input_pass=Entry(width=30)
print(input_pass.get())
input_pass.place(x=204,y=340)





windows.mainloop()