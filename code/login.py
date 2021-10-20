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


        global imageLogo, image1, imageThought, imageEntry, imageLogin, makeaccount
        imageLogo = PhotoImage(file=relative_to_assets("logo.png"))
        image1 = PhotoImage(file=relative_to_assets("image1.png"))
        imageThought = PhotoImage(file=relative_to_assets("thought.png"))
        imageEntry = PhotoImage(file=relative_to_assets("entry.png"))
        imageLogin = PhotoImage(file=relative_to_assets("login.png"))
        makeaccount = PhotoImage(file=relative_to_assets("makeaccount.png"))
        
        canvas.create_image(
            180,
            70,
            image=imageLogo
        )
        canvas.create_text(
            80,
            185,
            anchor="nw",
            text="Access your account!",
            fill="#000000",
            font=("Roboto", 18 * -1)
        )
        canvas.create_image(
            194,
            273,
            image=imageEntry
        )
        entry1 = Entry(
            canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry1.place(
            x=82,
            y=259,
            width=224,
            height=28.0
        )

        self.entry_1 = entry1

        canvas.create_text(
            84,
            237,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )

        canvas.create_image(
            194,
            338,
            image=imageEntry
        )
        entry2 = Entry(
            canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            show='*'
        )
        entry2.place(
            x=82,
            y=324,
            width=224,
            height=28.0
        )

        self.entry_2 = entry2

        canvas.create_text(
            84,
            303,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )
        canvas.create_image(
            603,
            300,
            image=image1
        )
        btn_login = Button(
            canvas,
            image=imageLogin,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.login("login"),
            relief="flat"
        )
        btn_login.place(
            x=70,
            y=388,
            width=242,
            height=36.0
        )
        btn_register = Button(
            canvas,
            image=makeaccount,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.window.show_frame("Register"),
            relief="flat"
        )
        btn_register.place(
            x=70,
            y=388.0 + 50,
            width=242,
            height=36.0
        )
        canvas.create_image(
            580,
            458,
            image=imageThought
        )

        entry1.bind("<Return>", self.login)
        entry2.bind("<Return>", self.login)

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