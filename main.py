from tkinter import *
from tkinter import messagebox

SAMPLE_EMAIL = "meow@gmail.com"
is_it_ok = False

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# password_list = []
password_list = ([random.choice(letters) for char in range(nr_letters)])
password_list.append([random.choice(letters) for char in range(nr_symbols)])
password_list.append([random.choice(letters) for char in range(nr_numbers)])
print(password_list)
# random.shuffle(password_list)
# password = ""
# for char in password_list:
#     password += char


# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#     password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#     password_list += random.choice(numbers)
#
# random.shuffle(password_list)
#
# password = ""
# for char in password_list:
#     password += char
#
# print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_form():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    global is_it_ok
    website_name = website_entry.get()
    email_or_username = email_entry.get()
    user_password = password_entry.get()
    print(website_name, email_or_username, user_password)

    if len(website_name) and len(email_or_username) and len(user_password) <= 0:
        messagebox.showwarning(title="Ooops", message="Please dont leave any fields empty")
        print(len(website_name), len(email_or_username), len(user_password))
    else:
        is_it_ok = messagebox.askokcancel(title=website_name, message=
        f"These are the details entered: \nEmail:{email_or_username} \n"
        f"Password: {user_password} \n Is it ok to save?")

    if is_it_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website_name} | {email_or_username} | {user_password} \n")
        clear_form()


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

password_entry = Entry(width=18, show="*")
password_entry.grid(row=3, column=1)

# Button
generate_pass_button = Button(text="Generate  Password", highlightthickness=0)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, padx=0, pady=0, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
