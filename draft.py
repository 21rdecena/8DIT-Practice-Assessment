from tkinter import *

class Data:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.has_phone = True
    
class GatherData:
    def __init__(self, parent):
        self.yesno = StringVar()
        self.yesno.set("yes")

        # parent
        info_lb = Label(parent, text="Collecting Person Data", bg='pink', height = 3, wraplength = 200)
        info_lb.grid(row=0, column=0)

        self.switch_btn = Button(parent, text="Show All", command=self.switch_frames)
        self.switch_btn.grid(row=0, column=1)

        # data entry frame
        self.data_frame = Frame(parent)
        self.data_frame.grid(row=1, column=0, columnspan=2)

        name_lb = Label(self.data_frame, text="First name: ")
        name_lb.grid(row=0, column=0)
        
        self.name_entry = Entry(self.data_frame)
        self.name_entry.grid(row=0, column=1)

        age_lb = Label(self.data_frame, text="Age: ")
        age_lb.grid(row=1, column=0)
        
        self.age_entry = Entry(self.data_frame)
        self.age_entry.grid(row=1, column=1)

        phone_lb = Label(self.data_frame, text="Do you have a mobile phone?")
        phone_lb.grid(row=2, column=0)

        self.yes_rb = Radiobutton(self.data_frame, text="Yes", variable = self.yesno, value = "yes")
        self.yes_rb.grid(row=2, column=1)
        
        self.no_rb = Radiobutton(self.data_frame, text="No", variable = self.yesno, value = "no")
        self.no_rb.grid(row=3, column=1)

        self.enter_btn = Button(self.data_frame, text="Enter Data:",  command=self.enter_data)
        self.enter_btn.grid(row=4, column=0, columnspan=2)

        # displaying data

    def enter_data(self):
        print("Data entered!")
    
    def switch_frames(self):
        print("Frames switched")

if __name__ == "__main__":
    root = Tk()
    root.title("Gather Data")
    app = GatherData(root)
    root.configure(bg='pink')
    root.mainloop()

