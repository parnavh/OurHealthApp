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
        reminder_active = PhotoImage(file=relative_to_assets("dashboard/reminder_active.png"))
        appointments_inactive = PhotoImage(file=relative_to_assets("dashboard/appointments_inactive.png"))
        prescriptions_inactive = PhotoImage(file=relative_to_assets("dashboard/prescriptions_inactive.png"))
        addReminder = PhotoImage(file=relative_to_assets("dashboard/addReminder.png"))
        profilepic = PhotoImage(file=relative_to_assets("dashboard/profilepic.png"))
        notificationBell = PhotoImage(file=relative_to_assets("dashboard/notificationBell.png"))
        garbage_1.extend([reminder_active, appointments_inactive, prescriptions_inactive, addReminder, profilepic, notificationBell])

        canvas.create_image(
            242,
            190,
            image=reminder_active
        )

        
        btn_appointment = Button(
            image=appointments_inactive,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_2"),
            relief="flat"
        )
        btn_appointment.place(
            x=373,
            y=170,
            width=119,
            height=39
        )        
        btn_prescriptions = Button(
            image=prescriptions_inactive,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_3"),
            relief="flat"
        )
        btn_prescriptions.place(
            x=580,
            y=169,
            width=118,
            height=40
        )
        canvas.create_rectangle(
            50,
            209,
            801,
            600,
            fill="#F8F7F2",
            outline="")

        canvas.create_rectangle(
            0,
            0,
            49,
            600,
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
            91,
            79,
            image=profilepic
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

            btn_notificationBell = get_button(self, notificationBell, i)
            btn_notificationBell.place(
                x=95,
                y=250 + cache
            )

            self.items.append((rect1, text1, text2, btn_notificationBell))

            cache += 55
            i += 1
        
        btn_addReminder = Button(
            image=addReminder,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Reminders"),
            relief="flat"
        )
        btn_addReminder.place(
            x=324,
            y=521,
            width=202,
            height=50
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

            btn_notificationBell = get_button(self, image, i)
            btn_notificationBell.place(
                x=95,
                y=250 + cache
            )

            self.items.append((rect1, text1, text2, btn_notificationBell))

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
        reminder_inactive = PhotoImage(file=relative_to_assets("dashboard/reminder_inactive.png"))
        prescriptions_inactive = PhotoImage(file=relative_to_assets("dashboard/prescriptions_inactive.png"))
        appointments_active = PhotoImage(file=relative_to_assets("dashboard/appointments_active.png"))
        addAppointment = PhotoImage(file=relative_to_assets("dashboard/addAppointment.png"))
        profilepic = PhotoImage(file=relative_to_assets("dashboard/profilepic.png"))
        doctor = PhotoImage(file=relative_to_assets("dashboard/doctor.png"))
        garbage_2.extend([reminder_inactive, prescriptions_inactive, appointments_active, addAppointment, profilepic, doctor])

        btn_reminder = Button(
            image=reminder_inactive,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_1"),
            relief="flat"
        )
        btn_reminder.place(
            x=195,
            y=176,
            width=94,
            height=33
        )

        
        btn_presctiptions = Button(
            image=prescriptions_inactive,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_3"),
            relief="flat"
        )
        btn_presctiptions.place(
            x=583.0,
            y=174.0,
            width=115.0,
            height=35.0
        )
        canvas.create_image(
            430,
            192,
            image=appointments_active
        )

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
            image=profilepic
        )
        
        canvas.create_image(
            104.0,
            266.0,
            image=doctor
        )

        btn_addAppointment = Button(
            image=addAppointment,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Appointments"),
            relief="flat"
        )
        btn_addAppointment.place(
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

            but = get_button(self, doctor, i)
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
        reminder_inactive = PhotoImage(file=relative_to_assets("dashboard/reminder_2.png"))
        appointments_active = PhotoImage(file=relative_to_assets("dashboard/appointments_inactive.png"))
        prescriptions_active = PhotoImage(file=relative_to_assets("dashboard/prescriptions_active.png"))
        addPrescription = PhotoImage(file=relative_to_assets("dashboard/addPrescription.png"))
        prescription_image = PhotoImage(file=relative_to_assets("dashboard/prescription_image.png"))
        profilepic = PhotoImage(file=relative_to_assets("dashboard/profilepic.png"))
        garbage_3.extend([reminder_inactive, appointments_active, prescriptions_active, addPrescription, prescription_image, profilepic])

        button_1 = Button(
            image=reminder_inactive,
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

        btn_appointment = Button(
            image=appointments_active,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_2"),
            relief="flat"
        )
        btn_appointment.place(
            x=371.0,
            y=174.0,
            width=119.0,
            height=35.0
        )

        btn_prescription = Button(
            image=prescriptions_active,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        btn_prescription.place(
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

        
        canvas.create_image(
            111.0,
            265.0,
            image=prescription_image
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

        canvas.create_image(
            91.0,
            79.0,
            image=profilepic
        )

        
        btn_addPrescription = Button(
            image=addPrescription,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        btn_addPrescription.place(
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