from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry, messagebox
from sql import Mysql

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/login")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Login(Frame):
    def __init__(self, window, parent):
        Frame.__init__(self, parent)
        self.window = window
        self.parent = parent
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


        global image_image_1, image_image_2, image_image_3, button_image_1, entry_image, button_image_2
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        entry_image = PhotoImage(file=relative_to_assets("entry.png"))
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        
        canvas.create_image(
            180,
            70,
            image=image_image_1
        )
        canvas.create_text(
            80.0,
            185.0,
            anchor="nw",
            text="Access your account!",
            fill="#000000",
            font=("Roboto", 18 * -1)
        )
        canvas.create_image(
            194.0,
            273.0,
            image=entry_image
        )
        entry_1 = Entry(
            canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=82.0,
            y=259.0,
            width=224.0,
            height=28.0
        )

        self.entry_1 = entry_1

        canvas.create_text(
            84.0,
            237.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )

        canvas.create_image(
            194.0,
            338.0,
            image=entry_image
        )
        entry_2 = Entry(
            canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            show='*'
        )
        entry_2.place(
            x=82.0,
            y=324.0,
            width=224.0,
            height=28.0
        )

        self.entry_2 = entry_2

        canvas.create_text(
            84.0,
            303.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )
        canvas.create_image(
            603.0,
            300.0,
            image=image_image_2
        )
        button_1 = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.login("login"),
            relief="flat"
        )
        button_1.place(
            x=70.0,
            y=388.0,
            width=242,
            height=36.0
        )
        button_2 = Button(
            canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.window.show_frame("Register"),
            relief="flat"
        )
        button_2.place(
            x=70.0,
            y=388.0 + 50,
            width=242,
            height=36.0
        )
        canvas.create_image(
            580.0,
            458.0,
            image=image_image_3
        )

        entry_1.bind("<Return>", self.login)
        entry_2.bind("<Return>", self.login)

    def login(self, event):
        username = self.entry_1.get()
        password = self.entry_2.get()

        if username == "":
            messagebox.showwarning("Login", "Please fill out the username field")
            return
        if password == "":
            messagebox.showwarning("Login", "Please fill out the password field")
            return
        db = Mysql()
        name = db.check_credentials(username, password)

        if not name:
            messagebox.showerror("Login failed", "Invalid Credentials")
            return

        self.window.data_name = name
        self.window.data_age = db.get_age(name)

        self.window.show_frame("Dash_1")