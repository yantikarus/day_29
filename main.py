from tkinter import *
from tkinter import messagebox
import pyperclip

SAMPLE_EMAIL = "meow@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for char in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for char in range(random.randint(2, 4))])

    random.shuffle(password_list)
    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
    return generated_password

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website_name = website_entry.get()
    email_or_username = email_entry.get()
    user_password = password_entry.get()

    if website_name and email_or_username and user_password:
        is_it_ok = messagebox.askokcancel(title=website_name, message=
            f"These are the details entered: \nEmail:{email_or_username} \n"
            f"Password: {user_password} \n Is it ok to save?")

        if is_it_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_name} | {email_or_username} | {user_password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Ooops", message="Please dont leave any fields empty")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Label
website = Label(text="Website:")
website.grid(row=1, column=0)

email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entry

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, SAMPLE_EMAIL)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Button
generate_pass_button = Button(text="Generate  Password", highlightthickness=0, command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, padx=0, pady=0, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
