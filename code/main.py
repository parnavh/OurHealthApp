from tkinter import Frame, Tk
from reminders import Reminders

# FRAMES = [Dash_1, Dash_2, Dash_3]

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

        self.frames = {}

        # for f in FRAMES:
        #     name = f.__name__
        #     frame = f(self, container)
        #     self.frames[name] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")
        #     frame.tkraise()

        Reminders(self, container)

        self.mainloop()

def main():
    app = App()

if __name__ == "__main__":
    main()