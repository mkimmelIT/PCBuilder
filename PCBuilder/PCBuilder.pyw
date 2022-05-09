"""
Program: PcBuilder.py
Author: Matt Kimmel
Last date modified: 5/02/2022

The purpose of this GUI program is to calculate the total cost of
building a PC. It does this by allowing the user to input the cost
of each component and then adding these costs together to calculate
the total. Additionally, the user can click the compare button to
bring up another window that allows the user to compare two different
builds and their respective costs.
"""
from tkinter import *
from tkinter import messagebox

class PcBuilder(Tk):
    def __init__(self):
        """Displays a window with the specified attributes"""

        # Creates the window
        super().__init__()
        
        # Adding a title to the window
        self.title("PcBuilder")

        # Icon
        self.iconbitmap('pcIcon.ico')

        # Fixed window size
        self.resizable(0, 0)

        # Create Widgets

        # Banner Image
        self.imageLabel = Label(self, relief=RAISED, bd=4)
        self.imageLabel.grid(row=0, column=0, columnspan=4, padx=8, pady=8)
        self.image = PhotoImage(file = "sbanner1.ppm")
        self.imageLabel["image"] = self.image
    
        # Header labels
        self.compLabel = Label(self, text="Component Type")
        self.compLabel.grid(row=1, column=0, padx=23, pady=5)

        self.descLabel = Label(self, text="Description")
        self.descLabel.grid(row=1, column=1, padx=5, pady=5)

        self.quantityLabel = Label(self, text="Quantity")
        self.quantityLabel.grid(row=1, column=2, padx=5, pady=5)

        self.costLabel = Label(self, text="Cost")
        self.costLabel.grid(row=1, column=3, padx=5, pady=5)

        # Entry Fields

        # Options for drop down menu
        self.dropOptions = [
            "None", "CPU", "CPU Cooler", "Motherboard", "Memory", 
            "Storage", "Video Card", "Case", "Power Supply", 
            "Operating System", "Monitor", "Expansion Cards", 
            "Peripherals", "Accessories"]

        # Generate 15 Rows of identical entry fields
        # Lists used to calculate total and transfer entries to Window 2
        self.dropEntries = []
        self.descEntries = []
        self.qEntries = []
        self.costEntries = []
        for i in range(15):

            # Drop down menu
            self.selected = StringVar()
            self.selected.set(self.dropOptions[0])
            self.compDrop = OptionMenu(self, self.selected, *self.dropOptions)
            self.compDrop.grid(row=[i + 2], column=0, padx=2, pady=2)
            self.dropEntries.append(self.selected)      # Saves entry to a list to be referenced by window 2

            # Description Input
            self.descInput = Entry(self, borderwidth=5, width=50)
            self.descInput.grid(row=[i + 2], column=1)
            self.descEntries.append(self.descInput)     # Saves entry to a list to be referenced by window 2

            # Quantity Input
            self.quantityInput = Entry(self, borderwidth=5, width=3)
            self.quantityInput.grid(row=[i + 2], column=2)
            self.quantityInput.insert(0, '1')
            self.qEntries.append(self.quantityInput)     # Saves entry to a list to be referenced by window 2 and calculate total 
            self.reg = self.register(self.qValid)    # Registers input validation
            self.quantityInput.config(validate ="key", validatecommand=(self.reg, '%P'))   # Input validation

            # Cost Input
            self.costInput = Entry(self, borderwidth=5, width=8)
            self.costInput.grid(row=[i + 2], column=3)
            self.costInput.insert(0, "0.00")
            self.costEntries.append(self.costInput)     # Saves entry to a list to be referenced by window 2 and calculate total 
            self.reg = self.register(self.cValid)    # Registers input validation   
            self.costInput.config(validate ="key", validatecommand=(self.reg, '%P'))    # Input validation


        # Total cost output
        self.totalCost = Label(self, relief=SUNKEN, bd=4, width=7, anchor='w')
        self.totalCost.grid(row=17, column=3)
        self.totalLabel = Label(self, text="Total Cost")
        self.totalLabel.grid(row=17, column=2, padx=5, pady=5)

        # Creating the buttons
        self.compareButton = Button(self, text="Compare", command=self.compare)
        self.compareButton.grid(row=17, column=0, padx=5, pady=5)

        self.calcButton = Button(self, text="Calculate", command=self.totalAdd)
        self.calcButton.grid(row=18, column=3, padx=5, pady=5)

        self.exitButton = Button(self, text="Exit", padx=15, command=self.destroy)
        self.exitButton.grid(row=18, column=0, padx=5, pady=5)


    # Input Validation
    def qValid(self, input):
        """Checks the quantity input and allows only integers"""
        if input.isdigit():
            return True

        elif input == "":
            return True

        else:
            return False
    
    def cValid(self, input):
        """Checks the cost input and allows only floats"""
        if self.isFloat(input):
            return True

        elif input == "":
            return True

        else:
            return False

    def isFloat(self, x):
        """Tests whether input is a float"""
        try:
            float(x)
            return True

        except ValueError:
            return False

    def errPopup(self, row):
        """Displays an error message when an empty string is used when calculating total cost"""
        messagebox.showerror("Missing Value", f"Quantity and cost must have a number to calculate total.\nMissing value in row {row}.")

    # Button Commands
    def totalAdd(self):
        """For Window 1: multiplies the quantities by cost, adds them to generate a total, and displays the total"""
        self.totalCost["text"] = ""
        total = 0
        for i in range(len(self.qEntries)):
            if self.qEntries[i].get() == "" or self.costEntries[i].get() == "":  # Input Validation
                self.errPopup(i + 1)
            else:
                total += int(self.qEntries[i].get()) * float(self.costEntries[i].get())
        self.totalCost["text"] = f"{total: .2f}"

    def b1_totalAdd(self):
        """For Window 2, Build 1: multiplies the quantities by cost, adds them to generate a total, and displays the total"""
        self.b1_totalCost["text"] = ""
        total = 0
        for i in range(len(self.b1_qEntries)):
            if self.b1_qEntries[i].get() == "" or self.b1_costEntries[i].get() == "":  # Input Validation
                self.errPopup(i + 1)
            else:
                total += int(self.b1_qEntries[i].get()) * float(self.b1_costEntries[i].get())
        self.b1_totalCost["text"] = f"{total: .2f}"
        self.costDiff()
                  
    def b2_totalAdd(self):
        """For Window 2 Build 2: multiplies the quantities by cost, adds them to generate a total, and displays the total"""
        self.b2_totalCost["text"] = ""
        total = 0
        for i in range(len(self.b2_qEntries)):
            if self.b2_qEntries[i].get() == "" or self.b2_costEntries[i].get() == "":  # Input Validation
                self.errPopup(i + 1)
            else:
                total += int(self.b2_qEntries[i].get()) * float(self.b2_costEntries[i].get())
        self.b2_totalCost["text"] = f"{total: .2f}"
        self.costDiff()

    def costDiff(self):
        """For Window 2: finds which build has the lowest total cost, subtracts it from the higher total cost, and displays the difference"""
        if self.b1_totalCost.cget("text") != "" and self.b2_totalCost.cget("text") != "":
            b1_cost = float(self.b1_totalCost.cget("text"))
            b2_cost = float(self.b2_totalCost.cget("text"))
            if b1_cost < b2_cost:
                self.diffLabel["text"] = f"Build 1 is ${b2_cost - b1_cost:.2f} cheaper than Build 2."
            else:
                self.diffLabel["text"] = f"Build 2 is ${b1_cost - b2_cost:.2f} cheaper than Build 1."

    def compare(self):
        """Opens up a new window to compare two builds side by side"""

        # Creates the new window
        self.top = Toplevel()

        # Adding a title to the window
        self.top.title("PcBuilder")

        # Icon
        self.top.iconbitmap('pcIcon.ico')

        # Fixed window size
        self.top.resizable(0, 0)

        # Banner
        self.imageLabel = Label(self.top, relief=RAISED, bd=4)
        self.imageLabel.grid(row=0, column=0, columnspan=2, padx=8, pady=8)
        self.top.image = PhotoImage(file = "sbanner2.ppm")
        self.imageLabel["image"] = self.top.image

        # Build frames
        self.frame1 = LabelFrame(self.top, text="Build 1", padx=19, pady=2)
        self.frame1.grid(row=1, column=0)
        self.frame2 = LabelFrame(self.top, text="Build 2", padx=19, pady=2)
        self.frame2.grid(row=1, column=1)

        
        # Build 1 Frame
        # Build 1 Header labels
        self.compLabel = Label(self.frame1, text="Component Type")
        self.compLabel.grid(row=2, column=0, padx=23, pady=5)

        self.descLabel = Label(self.frame1, text="Description")
        self.descLabel.grid(row=2, column=1, padx=5, pady=5)

        self.quantityLabel = Label(self.frame1, text="Quantity")
        self.quantityLabel.grid(row=2, column=2, padx=5, pady=5)

        self.costLabel = Label(self.frame1, text="Cost")
        self.costLabel.grid(row=2, column=3, padx=5, pady=5)

        # Build 1 Generate 15 Rows of identical entry fields
        # Lists used to calculate total
        self.b1_qEntries = []
        self.b1_costEntries = []
        for i in range(15):

            # Drop down menu
            self.b1_selected = StringVar()
            self.b1_selected.set(self.dropEntries[i].get())     # Sets value equal to the entry in window 1
            self.b1_compDrop = OptionMenu(self.frame1, self.b1_selected, *self.dropOptions)
            self.b1_compDrop.grid(row=[i + 3], column=0, padx=2, pady=2)

            # Description Input
            self.b1_descInput = Entry(self.frame1, borderwidth=5, width=50)
            self.b1_descInput.grid(row=[i + 3], column=1)
            self.b1_descInput.insert(0, self.descEntries[i].get())      # Sets value equal to the entry in window 1

            # Quantity Input
            self.b1_quantityInput = Entry(self.frame1, borderwidth=5, width=3)
            self.b1_quantityInput.grid(row=[i + 3], column=2)
            self.b1_quantityInput.insert(0, self.qEntries[i].get())     # Sets value equal to the entry in window 1
            self.b1_qEntries.append(self.b1_quantityInput)    # Saves entry to a list to calculate total
            self.b1_quantityInput.config(validate ="key", validatecommand=(self.reg, '%P'))   # Input validation

            # Cost Input
            self.b1_costInput = Entry(self.frame1, borderwidth=5, width=8)
            self.b1_costInput.grid(row=[i + 3], column=3)
            self.b1_costInput.insert(0, self.costEntries[i].get())      # Sets value equal to the entry in window 1
            self.b1_costEntries.append(self.b1_costInput)     # Saves entry to a list to calculate total
            self.b1_costInput.config(validate ="key", validatecommand=(self.reg, '%P'))   # Input validation

        # Build 1 Cost Output
        self.b1_totalCost = Label(self.frame1, relief=SUNKEN, bd=4, width=7, anchor='w')
        self.b1_totalCost.grid(row=18, column=3)
        self.b1_totalCost["text"] = self.totalCost.cget("text")     # Sets value equal to the entry in window 1
        self.b1_totalLabel = Label(self.frame1, text="Total Cost")
        self.b1_totalLabel.grid(row=18, column=2, padx=5, pady=5)

        # Build 1 Creating the buttons
        self.b1_calcButton = Button(self.frame1, text="Calculate", command=self.b1_totalAdd)
        self.b1_calcButton.grid(row=18, column=1, padx=5, pady=5, sticky='e')


        # Build 2 Frame
        # Build 2 Header labels
        self.compLabel = Label(self.frame2, text="Component Type")
        self.compLabel.grid(row=2, column=0, padx=23, pady=5)

        self.descLabel = Label(self.frame2, text="Description")
        self.descLabel.grid(row=2, column=1, padx=5, pady=5)

        self.quantityLabel = Label(self.frame2, text="Quantity")
        self.quantityLabel.grid(row=2, column=2, padx=5, pady=5)

        self.costLabel = Label(self.frame2, text="Cost")
        self.costLabel.grid(row=2, column=3, padx=5, pady=5)

        # Build 1 Generate 15 Rows of identical entry fields
        # Lists used to calculate total
        self.b2_qEntries = []
        self.b2_costEntries = []
        for i in range(15):

            # Drop down menu
            self.b2_selected = StringVar()
            self.b2_selected.set(self.dropOptions[0])
            self.b2_compDrop = OptionMenu(self.frame2, self.b2_selected, *self.dropOptions)
            self.b2_compDrop.grid(row=[i + 3], column=0, padx=2, pady=2)

            # Description Input
            self.b2_descInput = Entry(self.frame2, borderwidth=5, width=50)
            self.b2_descInput.grid(row=[i + 3], column=1)

            # Quantity Input
            self.b2_quantityInput = Entry(self.frame2, borderwidth=5, width=3)
            self.b2_quantityInput.grid(row=[i + 3], column=2)
            self.b2_quantityInput.insert(0, '1')
            self.b2_qEntries.append(self.b2_quantityInput)   # Saves entry to a list to calculate total  
            self.b2_quantityInput.config(validate ="key", validatecommand=(self.reg, '%P'))   # Input validation

            # Cost Input
            self.b2_costInput = Entry(self.frame2, borderwidth=5, width=8)
            self.b2_costInput.grid(row=[i + 3], column=3)
            self.b2_costInput.insert(0, "0.00")
            self.b2_costEntries.append(self.b2_costInput)     # Saves entry to a list to calculate total   
            self.b2_costInput.config(validate ="key", validatecommand=(self.reg, '%P'))     # Input validation

        # Build 2 Cost Output
        self.b2_totalCost = Label(self.frame2, relief=SUNKEN, bd=4, width=7, anchor='w')    
        self.b2_totalCost.grid(row=18, column=3)
        self.b2_totalLabel = Label(self.frame2, text="Total Cost")
        self.b2_totalLabel.grid(row=18, column=2, padx=5, pady=5)

        # Build 2 Creating the buttons
        self.b2_calcButton = Button(self.frame2, text="Calculate", command=self.b2_totalAdd)
        self.b2_calcButton.grid(row=18, column=1, padx=5, pady=5, sticky='e')

        # Window 2

        # Cost difference label
        self.diffLabel = Label(self.top, relief=RAISED, bd=4, width=30)
        self.diffLabel.grid(row=19, column=0, columnspan=2, padx=3, pady=3)

        # Exit button
        self.exitButton = Button(self.top, text="Exit", padx=15, command=self.top.destroy)
        self.exitButton.grid(row=20, column=0, padx=5, pady=5, sticky='w')


def main():
    PcBuilder().mainloop()

if __name__ == "__main__":
    main()

