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

        global entry_image_1, entry_image_2, entry_image_3, image_image_1
        global button_image_1, button_image_2
        entry_image_1 = PhotoImage(file=relative_to_assets("reminders/entry_1.png"))
        entry_image_2 = PhotoImage(file=relative_to_assets("reminders/entry_2.png"))
        entry_image_3 = PhotoImage(file=relative_to_assets("reminders/entry_3.png"))
        image_image_1 = PhotoImage(file=relative_to_assets("reminders/image_1.png"))
        button_image_1 = PhotoImage(file=relative_to_assets("reminders/button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("reminders/button_2.png"))

        canvas.create_rectangle(
            0.0,
            0.0,
            49.0,
            600.0,
            fill="#F8CD8C",
            outline="")

        canvas.create_text(
            60.0,
            49.0,
            anchor="nw",
            text="Hey John!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            60.0,
            97.0,
            anchor="nw",
            text="Never miss out on your health!",
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        
        image_1 = canvas.create_image(
            654.0,
            325.0,
            image=image_image_1
        )

        canvas.create_text(
            90.0,
            191.0,
            anchor="nw",
            text="What shoud I remind you about?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        entry_bg_1 = canvas.create_image(
            202.0,
            231.64544677734375,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=90.0,
            y=218,
            width=224.0,
            height=28
        )

        canvas.create_text(
            90.0,
            280.0,
            anchor="nw",
            text="By when do you wish to get it done?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        entry_bg_2 = canvas.create_image(
            200.9072265625,
            320.44366455078125,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_2.place(
            x=88.9072265625,
            y=306,
            width=224.0,
            height=28
        )

        canvas.create_text(
            90.0,
            369.0,
            anchor="nw",
            text="Set a description (optional)",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        
        entry_bg_3 = canvas.create_image(
            202.586181640625,
            415.6081237792969,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_3.place(
            x=90.586181640625,
            y=403,
            width=224.0,
            height=27
        )

        canvas.create_rectangle(
            642.0000610351562,
            32.0,
            875.0000610351562,
            81.0,
            fill="#FEECD0",
            outline="")

        canvas.create_text(
            667.0000610351562,
            46.0,
            anchor="nw",
            text="Set a reminder",
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.add,
            relief="flat"
        )
        button_1.place(
            x=541.0,
            y=512.0,
            width=202.77001953125,
            height=50.0
        )

        
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_1"),
            relief="flat"
        )
        button_2.place(
            x=13.0,
            y=530.0,
            width=23.0,
            height=23.0
        )

        self.entry_1 = entry_1
        self.entry_2 = entry_2
        self.entry_3 = entry_3

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