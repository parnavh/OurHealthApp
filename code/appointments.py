from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, Entry, messagebox
from sql import Mysql
import re


OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Appointments(Frame):
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

        global entryImage, image1
        global addNow, home
        entryImage = PhotoImage(file=relative_to_assets("appointments/entryimage.png"))
        image1 = PhotoImage(file=relative_to_assets("appointments/image_1.png"))
        addNow = PhotoImage(file=relative_to_assets("appointments/addNow.png"))
        home = PhotoImage(file=relative_to_assets("appointments/home.png"))

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
            text="Hey John!",
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

        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_2.place(
            x=99,
            y=210,
            width=225,
            height=25
        )
        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_3.place(
            x=99,
            y=301,
            width=225,
            height=25
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        entry_1.place(
            x=99,
            y=393,
            width=225,
            height=25
        )
        canvas.create_text(
            90,
            185,
            anchor="nw",
            text="Whom are you consulting?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        canvas.create_image(
            212,
            223,
            image=entryImage
        )
        
        canvas.create_text(
            90,
            277,
            anchor="nw",
            text="When?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        canvas.create_image(
            212,
            314,
            image=entryImage
        )
        canvas.create_text(
            90,
            368,
            anchor="nw",
            text="For whom?",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        canvas.create_image(
            212,
            405,
            image=entryImage
        )
        
        canvas.create_image(
            641,
            328,
            image=image1
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
            text="Appointments\n",
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        btn_addNow = Button(
            image=addNow,
            borderwidth=0,
            highlightthickness=0,
            command=self.add,
            relief="flat"
        )
        btn_addNow.place(
            x=541,
            y=512,
            width=202,
            height=50
        )

        btn_home = Button(
            image=home,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_2"),
            relief="flat"
        )
        btn_home.place(
            x=13,
            y=530,
            width=23,
            height=23
        )

        self.entry_2 = entry_2
        self.entry_3 = entry_3
        self.entry_1 = entry_1

    def add(self):
        doctor = self.entry_2.get()
        date = self.entry_3.get()
        patient = self.entry_1.get()

        if doctor == '':
            messagebox.showwarning("Set Appointment", "Please enter the doctor's name")
            return
        
        if not re.fullmatch(r'[0-9]{2}-[0-9]{2}-[0-9]{2}', date):
            messagebox.showwarning("Set Appointment", "Please enter the date in a valid format:\nFormat: YY-MM-DD")
            return

        if patient == '':
            patient = self.window.data_name
        
        db = Mysql()
        db.execute(f"insert into appointments (username, doctor, date, patient) values ('{self.window.data_name}', '{doctor}', '{date}', '{patient}')")
        self.window.show_frame("Dash_2")