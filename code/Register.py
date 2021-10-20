from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry, messagebox
from sql import Mysql
from re import fullmatch

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/createacc")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Register(Frame):
    def __init__(self, window, parent):
        Frame.__init__(self, parent)
        self.window = window
        canvas = Canvas(
            parent,
            bg = "#FFFFFF",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        global entry_image_1, entry_image_2, entry_image_3, entry_image_4, button_image_1, image_image_1, image_image_2, image_image_3
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_image_4 = PhotoImage(file=relative_to_assets("entry_1.png"))
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_image_3 = PhotoImage( file=relative_to_assets("image_3.png"))
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))

        canvas.create_image(
            179.06845092773438,
            267.3637924194336,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=82.0,
            y=257.0,
            width=190,
            height=20
        )

        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_2.place(
            x=82.0,
            y=301.0,
            width=190,
            height=20
        )

        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_3.place(
            x=82.0,
            y=345.0,
            width=190,
            height=20
        )
        

        entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            show='*'
        )
        entry_4.place(
            x=78.0,
            y=400.0,
            width=190,
            height=18
        )

        canvas.create_text(
            82.0,
            240.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Roboto", 10 * -1)
        )

        canvas.create_image(
            179.06845092773438,
            409,
            image=entry_image_4
        )
        
        canvas.create_text(
            82.0,
            383.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Roboto", 10 * -1)
        )
        canvas.create_image(
            179.06845092773438,
            355.3637924194336,
            image=entry_image_2
        )
        

        canvas.create_text(
            82.0,
            331.0,
            anchor="nw",
            text="Your age",
            fill="#000000",
            font=("Roboto", 10 * -1)
        )
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.register,
            relief="flat"
        )
        button_1.place(
            x=70.0,
            y=435.0,
            width=219.0,
            height=24.999984741210938
        )

        canvas.create_image(
            179.06845092773438,
            311.3637933731079,
            image=entry_image_3
        )

        canvas.create_text(
            82.0,
            286.0,
            anchor="nw",
            text="He/She/They/Them",
            fill="#000000",
            font=("Roboto", 10 * -1)
        )

        canvas.create_text(
            70.0,
            185.0,
            anchor="nw",
            text="Create your account to get started!",
            fill="#000000",
            font=("Roboto", 18 * -1)
        )
        
        canvas.create_image(
            180,
            70,
            image=image_image_1
        )

        canvas.create_image(
            574.0,
            295.0,
            image=image_image_2
        )

        canvas.create_image(
            591.0,
            468.0,
            image=image_image_3
        )

        self.entry_1 = entry_1
        self.entry_2 = entry_2
        self.entry_3 = entry_3
        self.entry_4 = entry_4

    def register(self):
        username = self.entry_1.get()
        gender = self.entry_2.get()
        age = self.entry_3.get()
        password = self.entry_4.get()

        db = Mysql()
        if len(username) < 4:
            messagebox.showwarning("Register", "Username should contain atleast 4 characters")
            return
        elif db.name_exists(username):
            messagebox.showwarning("Register", "The name already exists")
            return

        if gender == "":
            messagebox.showwarning("Register", "Please enter the gender field")
            return
        elif gender in ["male", "he"]:
            gender = "male"
        elif gender in ["female", "she"]:
            gender = "female"
        else:
            gender = "other"

        try:
            age = int(age)
        except Exception:
            messagebox.showwarning("Register", "Please enter a valid value for Age")
            return

        if age < 5:
            messagebox.showwarning("Register", "You must be atleast 5 years old to use this software")
            return

        if not fullmatch(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,39})', password):
            messagebox.showwarning("Register", "Your password should contain:\nAtleast 8 characters\nOne digit from 0-9\nOne special character\nOne lowercase letter\nOne uppercase letter")
            return

        db.execute(f"insert into login (username, password) values ('{username}', '{password}')")
        db.execute(f"insert into userdata (username, gender, age) values ('{username}', '{gender}', '{age}')")

        self.window.data_name = username
        self.window.data_age = str(age)

        self.window.show_frame("Dash_1")