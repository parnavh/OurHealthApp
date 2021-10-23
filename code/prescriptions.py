from pathlib import Path
from tkinter import Frame, Canvas, Entry, Button, Label, PhotoImage, filedialog, messagebox
from firebase import upload, delete_file
import re
import webbrowser
from sql import Mysql

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/prescriptions")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def getfile(name):
    file = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PDF","*.pdf*"), ("all files","*.*")))

    filename = entry_1.get()
    pattern = '^([a-z]|[A-Z]|[0-9])+$'
    if not re.match(pattern, filename):
        messagebox.showerror('Error!', 'Invalid filename, filname cannot contain special characters')
        return

    if upload(filename, file, name):
        messagebox.showinfo('Info', 'Uploaded!')

def get_button(self, image, i):
    return Button(
        image=image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: self.remove(i),
        relief="flat"
    )

def get_label(self, link, cache):
    text2 = Label(
        self.canvas,
        text="Click here to view in browser",
        font=("Roboto", 12 * -1),
        bg="#ffffff"
    )
    text2.place(x=207, y=265 + cache)
    text2.bind("<Button-1>", lambda x: webbrowser.open_new_tab(link))

    return text2

def get_link(name, filename):
    return f"https://storage.googleapis.com/ourhealthapp-ca43a.appspot.com/{name}/{filename}"

def crossify(button, normal, onHover):
    button.bind("<Enter>", func=lambda e: button.config(image=onHover))
    button.bind("<Leave>", func=lambda e: button.config(image=normal))

class Prescriptions(Frame):
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

        db = Mysql()
        self.prescriptions = db.get_prescriptions(self.window.data_name)

        global image_1, entry_image, button_image_1, button_image_2, entry_1, cross
        cross = PhotoImage(file=relative_to_assets("cross.png"))
        image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        entry_image = PhotoImage(file=relative_to_assets("entry_1.png"))
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))

        canvas.create_rectangle(
            0,
            0,
            49,
            600,
            fill="#F8CD8C",
            outline="")

        canvas.create_rectangle(
            147,
            166,
            654,
            197,
            fill="#FEE5C0",
            outline="")

        canvas.create_text(
            331,
            173,
            anchor="nw",
            text="Your prescriptions",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )

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
            324,
            560,
            image=entry_image
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFCFC",
            highlightthickness=0
        )
        entry_1.place(
            x=112,
            y=546,
            width=426,
            height=28.0
        )

        self.entry_1 = entry_1

        canvas.create_text(
            108,
            525,
            anchor="nw",
            text="File name",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
        
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.add,
            relief="flat"
        )

        button_1.place(
            x=556,
            y=530,
            width=203,
            height=50.0
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
            text="Prescriptions",
            fill="#000000",
            font=("Roboto", 16 * -1)
        )
        
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.show_frame("Dash_3"),
            relief="flat"
        )
        button_2.place(
            x=13,
            y=530,
            width=23,
            height=23.0
        )

        cache = 0
        self.items = []
        i = 0
        for pre in self.prescriptions:
            rect1 = canvas.create_rectangle(
                138,
                243 + cache,
                739,
                286 + cache,
                fill="#FFFFFF",
                outline="")

            text1 = canvas.create_text(
                207,
                249 + cache,
                anchor="nw",
                text=pre[0],
                fill="#000000",
                font=("Roboto", 14 * -1)
            )

            text2 = get_label(self, get_link(self.window.data_name, pre[0]), cache)

            btn_file = get_button(self, image_1, i)
            btn_file.place(
                x=166,
                y=264 + cache,
                anchor="center"
            )

            crossify(btn_file, image_1, cross)

            self.items.append((rect1, text1, text2, btn_file))

            cache += 55
            i += 1

    def remove(self, number):
        if not messagebox.askokcancel("Prescriptions", "This prescription will be deleted", icon="warning"):
            return
        val = self.prescriptions.pop(int(number))
        self.remove_sql(val)
        delete_file(val[0], self.window.data_name)
        for batch in self.items:
            for item in batch:
                if hasattr(item, 'destroy'):
                    item.destroy()
                else:
                    self.canvas.delete(item)
        global image_1
        cache = 0
        self.items = []
        i = 0
        for pre in self.prescriptions:
            rect1 = self.canvas.create_rectangle(
                138,
                243 + cache,
                739,
                286 + cache,
                fill="#FFFFFF",
                outline="")

            text1 = self.canvas.create_text(
                207,
                249 + cache,
                anchor="nw",
                text=pre[0],
                fill="#000000",
                font=("Roboto", 14 * -1)
            )

            text2 = get_label(self, get_link(self.window.data_name, pre[0]), cache)

            btn_file = get_button(self, image_1, i)
            btn_file.place(
                x=166,
                y=264 + cache,
                anchor="center"
            )
            crossify(btn_file, image_1, cross)

            self.items.append((rect1, text1, text2, btn_file))

            cache += 55
            i += 1

    def add(self):
        filename = self.entry_1.get()

        file = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PDF","*.pdf*"), ("all files","*.*")))

        filename = entry_1.get()
        pattern = '^([a-z]|[A-Z]|[0-9])+$'
        if not re.match(pattern, filename):
            messagebox.showerror('Error!', 'Invalid filename, filname cannot contain special characters')
            return

        if upload(filename, file, self.window.data_name):
            messagebox.showinfo('Info', 'Uploaded!')
            db = Mysql()
            db.execute(f"insert into prescriptions (username, filename) values ('{self.window.data_name}', '{filename}')")
            self.window.show_frame("Dash_3")

    def remove_sql(self, value):
        db = Mysql()
        db.execute(f"delete from prescriptions where username='{self.window.data_name}' and filename='{value[0]}'")