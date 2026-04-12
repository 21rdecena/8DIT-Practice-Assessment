from tkinter import *

class Data:
    def __init__ (self, name, age, has_phone):
        self.name = name
        self.age = age
        self.has_phone = has_phone
    
class GatherData:
    def __init__(self, parent):
        self.yesno_var = StringVar()
        self.yesno_var.set("yes")

        self.person_data = []

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

        self.yes_rb = Radiobutton(self.data_frame, text="Yes", variable = self.yesno_var, value = "yes")
        self.yes_rb.grid(row=2, column=1)
        
        self.no_rb = Radiobutton(self.data_frame, text="No", variable = self.yesno_var, value = "no")
        self.no_rb.grid(row=3, column=1)

        self.enter_btn = Button(self.data_frame, text="Enter Data:",  command=self.enter_data)
        self.enter_btn.grid(row=4, column=0, columnspan=2)
       
    '''
        # displaying data

        self.display_frame = Frame(parent)
        self.display_frame.grid(row=1, column=0, columnspan=2)

        name_lb = Label(self.data_frame, text="First name: ")
        name_lb.grid(row=0, column=0)
        
        age_lb = Label(self.data_frame, text="Age: ")
        age_lb.grid(row=1, column=0)
        
        phone_lb = Label(self.data_frame, text="Do you have a mobile phone?")
        phone_lb.grid(row=2, column=0)

        self.enter_btn = Button(self.data_frame, text="Enter Data:",  command=self.enter_data)
        self.enter_btn.grid(row=4, column=0, columnspan=2)

        self.enter_btn = Button(self.data_frame, text="Enter Data:",  command=self.enter_data)
        self.enter_btn.grid(row=4, column=0, columnspan=2)
     '''


    def enter_data(self):
        user_first = self.name_entry.get()
        user_age = self.age_entry.get()
        user_phone = self.yesno_var.get()
        self.person_data.append(Data(user_first, user_age, user_phone))
        for person in self.person_data:
            print(person.name)
            print(person.age)
            print(person.has_phone)
            
    
    def switch_frames(self):
        print("Frames switched")

if __name__ == "__main__":
    root = Tk()
    root.title("Gather Data")
    app = GatherData(root)
    root.configure(bg='pink')
    root.mainloop()

