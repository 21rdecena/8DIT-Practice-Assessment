from tkinter import *

class Person:
    def __init__ (self, name, age, has_phone):
        self.name = name
        self.age = age
        self.has_phone = has_phone
    
class GatherData:
    def __init__(self, parent):
        self.yesno_var = StringVar()
        self.yesno_var.set("yes")

        self.frame_count = 0
        self.person_index = 0
        self.person_data = []

        # parent
        self.info_lb = Label(parent, text="Collecting Person Data", bg='pink', height = 3, wraplength = 200)
        self.info_lb.grid(row=0, column=0)

        self.switch_btn = Button(parent, text="Show All", command=self.frames_switch)
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
       
        # displaying data

        self.display_frame = Frame(parent)

        name_lb = Label(self.display_frame, text="First name: ")
        name_lb.grid(row=0, column=0)
        
        self.output_name = Label(self.display_frame, text="Placeholder")
        self.output_name.grid(row=0, column=1)
        
        age_lb = Label(self.display_frame, text="Age: ")
        age_lb.grid(row=1, column=0)
        
        self.output_age = Label(self.display_frame, text="Placeholder")
        self.output_age.grid(row=1, column=1)
        
        self.output_phone = Label(self.display_frame, text="Lorem ipsum")
        self.output_phone.grid(row=2, column=0, columnspan=2)

        self.prev_btn = Button(self.display_frame, text="Previous",  command=lambda: self.switch_person(-1))
        self.prev_btn.grid(row=3, column=0)

        self.next_btn = Button(self.display_frame, text="Next",  command=lambda: self.switch_person(1))
        self.next_btn.grid(row=3, column=1)


    def enter_data(self):
        user_first = self.name_entry.get()
        user_age = self.age_entry.get()
        user_phone = self.yesno_var.get()
        self.person_data.append(Person(user_first, user_age, user_phone))


    def switch_person(self, amount):
        self.person_index += amount
        self.update_labels()

    def frames_switch(self):
        if self.frame_count == 0:
            self.data_frame.grid_forget()
            self.display_frame.grid(row=1, column=0, columnspan=2)
            self.info_switch()
            self.frame_count += 1
        else:
            self.display_frame.grid_forget()
            self.data_frame.grid(row=1, column=0, columnspan=2)
            self.info_switch()
            self.frame_count = 0

    def info_switch(self):
        if self.frame_count == 0:
            self.info_lb.configure(text="Displaying Person Data")
            self.switch_btn.configure(text="Add New Person")
            self.update_labels()
        else:
            self.info_lb.configure(text="Collecting Person Data")
            self.switch_btn.configure(text="Show All")
            
    def update_labels(self):
        person = self.person_data[self.person_index]
        self.output_name.configure(text=f'{person.name}')
        self.output_age.configure(text=f'{person.age}')
        if person.has_phone == "yes":
            self.output_phone.configure(text=f'{person.name} has a mobile phone')
        else:
            self.output_phone.configure(text=f"{person.name} doesn't have a mobile phone")

if __name__ == "__main__":
    root = Tk()
    root.title("Gather Data")
    app = GatherData(root)
    root.configure(bg='pink')
    root.mainloop()

