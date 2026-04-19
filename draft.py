from tkinter import *
from tkinter import messagebox

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
        self.info_lb.grid(row=0, column=0, padx= 25)

        self.switch_btn = Button(parent, text="Show All", command=self.frames_switch)
        self.switch_btn.grid(row=0, column=1)

        # data entry frame
        self.data_frame = Frame(parent)
        self.data_frame.grid(row=1, column=0, columnspan=2)

        name_lb = Label(self.data_frame, text="First name: ")
        name_lb.grid(row=0, column=0, padx = 15, pady = 5, sticky = NW)
        
        self.name_entry = Entry(self.data_frame)
        self.name_entry.grid(row=0, column=1, padx = 15, pady = 5)

        age_lb = Label(self.data_frame, text="Age: ")
        age_lb.grid(row=1, column=0, padx = 15, pady = 5, sticky = NW)
        
        self.age_entry = Entry(self.data_frame)
        self.age_entry.grid(row=1, column=1, padx = 15, pady = 5)

        phone_lb = Label(self.data_frame, text="Do you have a mobile phone?")
        phone_lb.grid(row=2, column=0, padx = 15, pady = 5, sticky = NW)

        self.yes_rb = Radiobutton(self.data_frame, text="Yes", variable = self.yesno_var, value = "yes")
        self.yes_rb.grid(row=2, column=1)
        
        self.no_rb = Radiobutton(self.data_frame, text="No", variable = self.yesno_var, value = "no")
        self.no_rb.grid(row=3, column=1)

        self.enter_btn = Button(self.data_frame, text="Enter Data:",  command=self.enter_data)
        self.enter_btn.grid(row=4, column=0, columnspan=2, pady= 20)
       
        # displaying data
        self.display_frame = Frame(parent)

        name_lb = Label(self.display_frame, text="First name: ")
        name_lb.grid(row=0, column=0, padx = 15, pady = 5)
        
        self.output_name = Label(self.display_frame, text="No data found")
        self.output_name.grid(row=0, column=1, pady = 5)
        
        age_lb = Label(self.display_frame, text="Age: ")
        age_lb.grid(row=1, column=0, padx = 15, pady = 5)
        
        self.output_age = Label(self.display_frame, text="No data found")
        self.output_age.grid(row=1, column=1, padx = 25, pady = 5)
        
        self.output_phone = Label(self.display_frame, text="No data found")
        self.output_phone.grid(row=2, column=0, columnspan=2, padx = 15, pady = 5)

        self.prev_btn = Button(self.display_frame, text="Previous",  command=lambda: self.switch_person(-1))
        self.prev_btn.grid(row=3, column=0, padx=15, pady = 5)

        self.next_btn = Button(self.display_frame, text="Next",  command=lambda: self.switch_person(1))
        self.next_btn.grid(row=3, column=1, padx=15, pady = 5, sticky=E)

    def enter_data(self):
        user_first = self.name_entry.get().title().strip()
        user_phone = self.yesno_var.get()
        try:
            user_age = int(self.age_entry.get())
            user_input = Person(user_first, user_age, user_phone)
            if user_age >= 1:
                self.person_data.append(user_input)
                
            else:
                messagebox.showerror("Negative number found", "Please enter a positive number!")
                self.age_entry.delete(0, END)
                self.age_entry.focus()

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer!")
            self.age_entry.delete(0, END)
            self.age_entry.focus()


    def switch_person(self, amount):
        self.person_index += amount
        self.update_labels()

    def frames_switch(self):
        if self.frame_count == 0:
            self.data_frame.grid_forget()
            self.display_frame.grid(row=1, column=0, columnspan=2, sticky=W+E)
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
            if len(self.person_data) != 0:                                  # avoids a list out of index error
                self.update_labels()
            else:
                self.prev_btn.configure(state=DISABLED)
                self.next_btn.configure(state=DISABLED)
        else:
            self.info_lb.configure(text="Collecting Person Data")
            self.switch_btn.configure(text="Show All")
            
    def update_labels(self):
        self.prev_btn.configure(state=NORMAL)
        self.next_btn.configure(state=NORMAL)
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

