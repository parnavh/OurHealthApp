from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame, messagebox
from sql import Mysql

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_button(self, image, i):
    return Button(
        image=image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: self.remove(i),
        relief="flat"
    )

class Dash_1(Frame):
    def __init__(self, window, parent):
        Frame.__init__(self, parent)
        self.window = window

        db = Mysql()
        self.reminders = db.get_reminders(self.window.data_name)

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

        self.canvas = canvas

        global garbage_1
        garbage_1 = []
        button_image_1 = PhotoImage(file=relative_to_assets("1/button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("1/button_2.png"))
        button_image_3 = PhotoImage(file=relative_to_assets("1/button_3.png"))
        button_image_4 = PhotoImage(file=relative_to_assets("1/button_4.png"))
        image_image_1 = PhotoImage(file=relative_to_assets("1/image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("1/image_2.png"))
        garbage_1.extend([button_image_1, button_image_2, button_image_3, button_image_4, image_image_1, image_image_2])

        canvas.create_image(
            242,
            190,
            image=button_image_1
        )

        
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_2"),
            relief="flat"
        )
        button_2.place(
            x=373.0,
            y=170.0,
            width=119.0,
            height=39.0
        )

        
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_3"),
            relief="flat"
        )
        button_3.place(
            x=580.0,
            y=169.0,
            width=118.0,
            height=40.0
        )

        canvas.create_rectangle(
            50.0,
            209.0,
            801.0,
            600.0,
            fill="#F8F7F2",
            outline="")

        canvas.create_rectangle(
            0.0,
            0.0,
            49.0,
            600.0,
            fill="#F8CD8C",
            outline="")

        canvas.create_text(
            124,
            54,
            anchor="nw",
            text="Welcome @" + self.window.data_name,
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            124,
            83,
            anchor="nw",
            text= "Age: " + self.window.data_age,
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        canvas.create_image(
            91.0,
            79.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            182,
            209,
            302,
            209,
            fill="#FFFFFF",
            outline="")

        cache = 0
        self.items = []
        i = 0
        for rem in self.reminders:
            rect1 = canvas.create_rectangle(
                77,
                244 + cache,
                761,
                284 + cache,
                fill="#FFFFFF",
                outline="")

            text1 = canvas.create_text(
                156,
                250 + cache,
                anchor="nw",
                text=rem[0],
                fill="#000000",
                font=("Roboto", 14 * -1)
            )

            text2 = canvas.create_text(
                156,
                266 + cache,
                anchor="nw",
                text=rem[1],
                fill="#000000",
                font=("Roboto", 12 * -1)
            )

            but = get_button(self, image_image_2, i)
            but.place(
                x=95,
                y=250.0 + cache
            )

            self.items.append((rect1, text1, text2, but))

            cache += 55
            i += 1
        
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Reminders"),
            relief="flat"
        )
        button_4.place(
            x=324.0,
            y=521.0,
            width=202,
            height=50.0
        )

    def remove(self, number):
        if not messagebox.askokcancel("Reminders", "This entry will be marked as done", icon="warning"):
            return
        self.reminders.pop(int(number))
        for batch in self.items:
            for item in batch:
                if hasattr(item, 'destroy'):
                    item.destroy()
                else:
                    self.canvas.delete(item)
        cache = 0
        self.items = []
        i = 0
        global garbage_1
        image = garbage_1[5]
        cache = 0
        self.items = []
        i = 0
        for rem in self.reminders:
            rect1 = self.canvas.create_rectangle(
                77,
                244 + cache,
                761,
                284 + cache,
                fill="#FFFFFF",
                outline="")

            text1 = self.canvas.create_text(
                156,
                250 + cache,
                anchor="nw",
                text=rem[0],
                fill="#000000",
                font=("Roboto", 14 * -1)
            )

            text2 = self.canvas.create_text(
                156,
                266 + cache,
                anchor="nw",
                text=rem[1],
                fill="#000000",
                font=("Roboto", 12 * -1)
            )

            but = get_button(self, image, i)
            but.place(
                x=95,
                y=250 + cache
            )

            self.items.append((rect1, text1, text2, but))

            cache += 55
            i += 1
        

class Dash_2(Frame):
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

        self.canvas = canvas

        self.appointments = [("Appointment with Dr. John Doe","Time: 2:00 P.M IST"), ("Appointment with Dr. dfgdfg Doe","Time: 5:00 P.M IST")]

        global garbage_2
        garbage_2 = []
        button_image_1 = PhotoImage(file=relative_to_assets("2/button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("2/button_2.png"))
        button_image_3 = PhotoImage(file=relative_to_assets("2/button_3.png"))
        button_image_4 = PhotoImage(file=relative_to_assets("2/button_4.png"))
        image_image_1 = PhotoImage(file=relative_to_assets("2/image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("2/image_2.png"))
        garbage_2.extend([button_image_1, button_image_2, button_image_3, button_image_4, image_image_1, image_image_2])

        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_1"),
            relief="flat"
        )
        button_1.place(
            x=195.0,
            y=176.0,
            width=94.0,
            height=33.0
        )

        
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_3"),
            relief="flat"
        )
        button_2.place(
            x=583.0,
            y=174.0,
            width=115.0,
            height=35.0
        )
        canvas.create_image(
            430,
            192,
            image=button_image_3
        )

        
        # button_3 = Button(
        #     image=button_image_3,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.window.show_frame("Dash_3"),
        #     relief="flat"
        # )
        # button_3.place(
        #     x=363.0,
        #     y=175.0,
        #     width=134.0,
        #     height=34.0
        # )

        canvas.create_rectangle(
            49.0,
            209.0,
            800.0,
            600.0,
            fill="#F8F7F2",
            outline="")

        canvas.create_rectangle(
            369.0,
            209.0,
            489.0,
            209.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            0.0,
            0.0,
            49.0,
            600.0,
            fill="#F8CD8C",
            outline="")

        canvas.create_text(
            124,
            54,
            anchor="nw",
            text="Welcome @" + self.window.data_name,
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            124,
            83,
            anchor="nw",
            text= "Age: " + self.window.data_age,
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        canvas.create_image(
            91.0,
            79.0,
            image=image_image_1
        )
        
        canvas.create_image(
            104.0,
            266.0,
            image=image_image_2
        )

        
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=324.0,
            y=521.0,
            width=202.77001953125,
            height=50.0
        )
        cache = 0
        self.items = []
        i = 0
        for appoint in self.appointments:
            rect1 = canvas.create_rectangle(
                77,
                244 + cache,
                761,
                284 + cache,
                fill="#FFFFFF",
                outline="")

            text1 = canvas.create_text(
                156,
                250 + cache,
                anchor="nw",
                text=appoint[0],
                fill="#000000",
                font=("Roboto", 14 * -1)
            )

            text2 = canvas.create_text(
                156,
                266 + cache,
                anchor="nw",
                text=appoint[1],
                fill="#000000",
                font=("Roboto", 12 * -1)
            )

            canvas.create_text(
                156.28997802734375,
                266.0,
                anchor="nw",
                text="Time: 2:00 P.M IST,",
                fill="#000000",
                font=("Roboto", 12 * -1)
            )

            but = get_button(self, image_image_2, i)
            but.place(
                x=95,
                y=250.0 + cache
            )

            self.items.append((rect1, text1, text2, but))

            cache += 55
            i += 1

    def remove(self, number):
        if not messagebox.askokcancel("Reminders", "This entry will be marked as done", icon="warning"):
            return
        self.appointments.pop(int(number))
        for batch in self.items:
            for item in batch:
                if hasattr(item, 'destroy'):
                    item.destroy()
                else:
                    self.canvas.delete(item)
        cache = 0
        self.items = []
        i = 0
        global garbage_2
        image = garbage_2[5]
        cache = 0
        self.items = []
        i = 0
        for rem in self.appointments:
            rect1 = self.canvas.create_rectangle(
                77,
                244 + cache,
                761,
                284 + cache,
                fill="#FFFFFF",
                outline="")

            text1 = self.canvas.create_text(
                156,
                250 + cache,
                anchor="nw",
                text=rem[0],
                fill="#000000",
                font=("Roboto", 14 * -1)
            )

            text2 = self.canvas.create_text(
                156,
                266 + cache,
                anchor="nw",
                text=rem[1],
                fill="#000000",
                font=("Roboto", 12 * -1)
            )

            but = get_button(self, image, i)
            but.place(
                x=95,
                y=250 + cache
            )

            self.items.append((rect1, text1, text2, but))

            cache += 55
            i += 1

class Dash_3(Frame):
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

        global garbage_3
        garbage_3 = []
        button_image_1 = PhotoImage(file=relative_to_assets("3/button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("3/button_2.png"))
        button_image_3 = PhotoImage(file=relative_to_assets("3/button_3.png"))
        button_image_4 = PhotoImage(file=relative_to_assets("3/button_4.png"))
        image_image_1 = PhotoImage(file=relative_to_assets("3/image_1.png"))
        image_image_2 = PhotoImage(file=relative_to_assets("3/image_2.png"))
        garbage_3.extend([button_image_1, button_image_2, button_image_3, button_image_4, image_image_1, image_image_2])

        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_1"),
            relief="flat"
        )
        button_1.place(
            x=185.0,
            y=175.0,
            width=110.0,
            height=34.0
        )

        
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_2"),
            relief="flat"
        )
        button_2.place(
            x=371.0,
            y=174.0,
            width=119.0,
            height=35.0
        )

        
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=584.0,
            y=174.0,
            width=109.0,
            height=29.0
        )

        canvas.create_rectangle(
            49.0,
            209.0,
            800.0,
            600.0,
            fill="#F8F7F2",
            outline="")

        canvas.create_rectangle(
            0.0,
            0.0,
            49.0,
            600.0,
            fill="#F8CD8C",
            outline="")

        canvas.create_rectangle(
            77.969970703125,
            244.0,
            761.3798828125,
            286.6699981689453,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            156.2900390625,
            250.0,
            anchor="nw",
            text="Prescription Name (Dental )",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

        canvas.create_text(
            156.2900390625,
            266.0,
            anchor="nw",
            text="<link here>",
            fill="#000000",
            font=("Roboto", 12 * -1)
        )

        
        image_1 = canvas.create_image(
            111.0,
            265.0,
            image=image_image_1
        )

        canvas.create_text(
            124,
            54,
            anchor="nw",
            text="Welcome @" + self.window.data_name,
            fill="#000000",
            font=("Roboto", 20 * -1)
        )

        canvas.create_text(
            124,
            83,
            anchor="nw",
            text= "Age: " + self.window.data_age,
            fill="#000000",
            font=("Roboto", 16 * -1)
        )

        
        image_2 = canvas.create_image(
            91.0,
            79.0,
            image=image_image_2
        )

        
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=324.0,
            y=521.0,
            width=202.77001953125,
            height=50.0
        )

        canvas.create_rectangle(
            578.0,
            209.0,
            698.0,
            209.0,
            fill="#FFFFFF",
            outline="")