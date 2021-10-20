from tkinter import Frame, Tk
from reminders import Reminders
from register import Register
from login import Login
from appointments import Appointments
from dashboard import Dash_1, Dash_2, Dash_3
from prescriptions import Prescriptions

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("800x600")
        self.title("Our Health App")
        self.resizable(False, False)
        self.configure(bg = "#FFFFFF")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.container = container
        self.show_frame("Login")
        self.mainloop()

    def show_frame(self, page_name):
        if hasattr(self, "current_frame"):
            self.current_frame.master.destroy()
            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.container = container
        self.current_frame = eval(f"{page_name}(self, self.container)")
        self.current_frame.tkraise()

def main():
    app = App()

if __name__ == "__main__":
    main()