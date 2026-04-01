from tkinter import *

class Data:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.has_phone = True
    
class GatherData:
    def __init__(self, parent):
        self.collect_lb = Label(parent, text="Collecting person data", bg="pink")
        self.collect_lb.grid(row=0, column=0)
        
        show_all_btn = Button(parent, text="Show All", command = self.switch_frames)  # can probably configure the text here when user switches frame?
        show_all_btn.grid(row=0, column=2)                                                         # maybe one single method to change frames??

        self.collect_frame = Frame(parent)
        self.collect_frame.grid()

        lbl1 = Label(self.collect_frame, text='first name')
        lbl1.grid(row=1, column=0)

        name_entry = Entry(self.collect_frame)
        name_entry.grid(row=1, column=2)

        lbl2 = Label(self.collect_frame, text='age')
        lbl2.grid(row=2, column=0)
        
        age_entry = Entry(self.collect_frame)
        age_entry.grid(row=2, column=2)

        lbl3 = Label(self.collect_frame, text='do u have  amobile phone')
        lbl3.grid(row=3, column=0)
        
        
        

        
    def switch_frames(self):
        pass

if __name__ == "__main__":
    root = Tk()
    root.title("Gather Data")
    root.configure(bg = "pink")
    app = GatherData(root)
    root.mainloop()

