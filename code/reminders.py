from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry, messagebox
from re import fullmatch
from sql import Mysql

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Reminders(Frame):
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

        global entryImage, image1, setnow, home
        entryImage = PhotoImage(file=relative_to_assets("reminders/entryImage.png"))
        image1 = PhotoImage(file=relative_to_assets("reminders/image1.png"))
        setnow = PhotoImage(file=relative_to_assets("reminders/setnow.png"))
        home = PhotoImage(file=relative_to_assets("reminders/home.png"))

        canvas.create_rectangle(
            0,
            0,
            49,
            600,
            fill="#F8CD8C",
            outline="")

        canvas.create_text(
            60,
            49,
            anchor="nw",
            text=f"Hey {self.window.data_name}!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            60,
            97,
            anchor="nw",
            text="Never miss out on your health!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )
    
        canvas.create_image(
            654,
            325,
            image=image1
        )

        canvas.create_text(
            90,
            190,
            anchor="nw",
            text="What shoud I remind you about?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        canvas.create_image(
            202,
            231,
            image=entryImage
        )
        entry1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry1.place(
            x=90,
            y=217,
            width=224,
            height=28
        )

        canvas.create_text(
            90,
            280,
            anchor="nw",
            text="By when do you wish to get it done?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        canvas.create_image(
            200,
            320,
            image=entryImage
        )
        entry2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry2.place(
            x=88,
            y=306,
            width=224,
            height=28
        )

        canvas.create_text(
            90,
            369,
            anchor="nw",
            text="Set a description (optional)",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        canvas.create_image(
            202,
            415,
            image=entryImage
        )
        entry3 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry3.place(
            x=90,
            y=402,
            width=224,
            height=27
        )

        canvas.create_rectangle(
            642,
            32,
            875,
            81,
            fill="#FEECD0",
            outline="")

        canvas.create_text(
            667,
            46,
            anchor="nw",
            text="Set a reminder",
            fill="#000000",
            font=("Roboto", 16 * -1)
        )
        
        btn_setnow = Button(
            image=setnow,
            borderwidth=0,
            highlightthickness=0,
            command=self.add,
            relief="flat"
        )
        btn_setnow.place(
            x=541,
            y=512,
            width=202,
            height=50.0
        )

        
        btn_home = Button(
            image=home,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_1"),
            relief="flat"
        )
        btn_home.place(
            x=13,
            y=530,
            width=23,
            height=23.0
        )

        self.entry_1 = entry1
        self.entry_2 = entry2
        self.entry_3 = entry3

    def add(self):
        title = self.entry_1.get()
        date = self.entry_2.get()
        description = self.entry_3.get()

        if title == "":
            messagebox.showwarning("Set Reminder", "Please enter a title")
            return
        
        if not fullmatch(r'[0-9]{2}-[0-9]{2}-[0-9]{2}', date):
            messagebox.showwarning("Set Reminder", "Please enter the date in a valid format:\nFormat: YY-MM-DD")
            return

        db = Mysql()

        db.execute(f"insert into reminders (username, topic, date, description) values ('{self.window.data_name}', '{title}', '{date}', '{description}')")
        
        self.window.show_frame("Dash_1")