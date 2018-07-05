from tkinter import *


class SimpleFrame:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button_switch = Button(frame, text="ON/OFF", command=self.switch_value)
        self.button_switch_value = "ON"
        self.button_quit = Button(frame, text="Exit", command=master.destroy)

        self.button_switch.pack(side=LEFT)
        self.button_quit.pack()

    def switch_value(self):
        if self.button_switch_value == "ON":
            self.button_switch_value = "OFF"
        else:
            self.button_switch_value = "ON"
        print(self.button_switch_value)


root = Tk()
a = SimpleFrame(root)
root.mainloop()