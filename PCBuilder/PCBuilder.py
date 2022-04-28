"""
Program: PCBuilder.py
Author: Matt Kimmel
Last date modified: 4/26/2022

The purpose of this GUI program is to calculate the total cost of
building a PC. It does this by allowing the user to input the cost
of each component and then adding these costs together to calculate
the total. Additionally, the user can click the compare button to
bring up another window that allows the user to compare two different
builds and their respective costs.
"""
from tkinter import *

class pcBuilder(Tk):
    def __init__(root):
        Tk.__init__(root)
        
        # Adding a title to the window
        root.title("PCBuilder")

        # Icon
        root.iconbitmap('pcIcon.ico')

        # Banner
        imageLabel = Label(root, relief=RAISED, bd=4)
        imageLabel.grid(row=0, column=0, columnspan=4, padx=8, pady=8)
        root.image = PhotoImage(file = "sbanner1.ppm")
        imageLabel["image"] = root.image
    
        # Header labels
        compLabel = Label(root, text="Component Type")
        compLabel.grid(row=1, column=0, padx=23, pady=5)

        descLabel = Label(root, text="Description")
        descLabel.grid(row=1, column=1, padx=5, pady=5)

        quantityLabel = Label(root, text="Quantity")
        quantityLabel.grid(row=1, column=2, padx=5, pady=5)

        costLabel = Label(root, text="Cost")
        costLabel.grid(row=1, column=3, padx=5, pady=5)

        # Entry Fields
        dropOptions = [
            "None", "CPU", "CPU Cooler", "Motherboard", "Memory", 
            "Storage", "Video Card", "Case", "Power Supply", 
            "Operating System", "Monitor", "Expansion Cards", 
            "Peripherals", "Accessories"]
        # Row 1
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=2, column=0, padx=2, pady=2)

        descInput1 = Entry(root, borderwidth=5, width=50)
        descInput1.grid(row=2, column=1)

        quantityInput1 = Entry(root, borderwidth=5, width=3)
        quantityInput1.grid(row=2, column=2)

        costInput1 = Entry(root, borderwidth=5, width=8)
        costInput1.grid(row=2, column=3)

        # Row 2
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=3, column=0, padx=2, pady=2)

        descInput2 = Entry(root, borderwidth=5, width=50)
        descInput2.grid(row=3, column=1)

        quantityInput2 = Entry(root, borderwidth=5, width=3)
        quantityInput2.grid(row=3, column=2)

        costInput2 = Entry(root, borderwidth=5, width=8)
        costInput2.grid(row=3, column=3)

        # Row 3
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=4, column=0, padx=2, pady=2)

        descInput3 = Entry(root, borderwidth=5, width=50)
        descInput3.grid(row=4, column=1)

        quantityInput3 = Entry(root, borderwidth=5, width=3)
        quantityInput3.grid(row=4, column=2)

        costInput3 = Entry(root, borderwidth=5, width=8)
        costInput3.grid(row=4, column=3)

        # Row 4
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=5, column=0, padx=2, pady=2)

        descInput4 = Entry(root, borderwidth=5, width=50)
        descInput4.grid(row=5, column=1)

        quantityInput4 = Entry(root, borderwidth=5, width=3)
        quantityInput4.grid(row=5, column=2)

        costInput4 = Entry(root, borderwidth=5, width=8)
        costInput4.grid(row=5, column=3)

        # Row 5
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=6, column=0, padx=2, pady=2)

        descInput5 = Entry(root, borderwidth=5, width=50)
        descInput5.grid(row=6, column=1)

        quantityInput5 = Entry(root, borderwidth=5, width=3)
        quantityInput5.grid(row=6, column=2)

        costInput5 = Entry(root, borderwidth=5, width=8)
        costInput5.grid(row=6, column=3)

        # Row 6
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=7, column=0, padx=2, pady=2)

        descInput6 = Entry(root, borderwidth=5, width=50)
        descInput6.grid(row=7, column=1)

        quantityInput6 = Entry(root, borderwidth=5, width=3)
        quantityInput6.grid(row=7, column=2)

        costInput6 = Entry(root, borderwidth=5, width=8)
        costInput6.grid(row=7, column=3)

        # Row 7
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=8, column=0, padx=2, pady=2)

        descInput7 = Entry(root, borderwidth=5, width=50)
        descInput7.grid(row=8, column=1)

        quantityInput7 = Entry(root, borderwidth=5, width=3)
        quantityInput7.grid(row=8, column=2)

        costInput7 = Entry(root, borderwidth=5, width=8)
        costInput7.grid(row=8, column=3)

        # Row 8
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=9, column=0, padx=2, pady=2)

        descInput8 = Entry(root, borderwidth=5, width=50)
        descInput8.grid(row=9, column=1)

        quantityInput8 = Entry(root, borderwidth=5, width=3)
        quantityInput8.grid(row=9, column=2)

        costInput8 = Entry(root, borderwidth=5, width=8)
        costInput8.grid(row=9, column=3)

        # Row 9
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=10, column=0, padx=2, pady=2)

        descInput9 = Entry(root, borderwidth=5, width=50)
        descInput9.grid(row=10, column=1)

        quantityInput9 = Entry(root, borderwidth=5, width=3)
        quantityInput9.grid(row=10, column=2)

        costInput9 = Entry(root, borderwidth=5, width=8)
        costInput9.grid(row=10, column=3)

        # Row 10
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=11, column=0, padx=2, pady=2)

        descInput10 = Entry(root, borderwidth=5, width=50)
        descInput10.grid(row=11, column=1)

        quantityInput10 = Entry(root, borderwidth=5, width=3)
        quantityInput10.grid(row=11, column=2)

        costInput10 = Entry(root, borderwidth=5, width=8)
        costInput10.grid(row=11, column=3)

        # Row 11
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=12, column=0, padx=2, pady=2)

        descInput11 = Entry(root, borderwidth=5, width=50)
        descInput11.grid(row=12, column=1)

        quantityInput11 = Entry(root, borderwidth=5, width=3)
        quantityInput11.grid(row=12, column=2)

        costInput11 = Entry(root, borderwidth=5, width=8)
        costInput11.grid(row=12, column=3)

        # Row 12
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=13, column=0, padx=2, pady=2)

        descInput12 = Entry(root, borderwidth=5, width=50)
        descInput12.grid(row=13, column=1)

        quantityInput12 = Entry(root, borderwidth=5, width=3)
        quantityInput12.grid(row=13, column=2)

        costInput12 = Entry(root, borderwidth=5, width=8)
        costInput12.grid(row=13, column=3)

        # Row 13
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=14, column=0, padx=2, pady=2)

        descInput13 = Entry(root, borderwidth=5, width=50)
        descInput13.grid(row=14, column=1)

        quantityInput13 = Entry(root, borderwidth=5, width=3)
        quantityInput13.grid(row=14, column=2)

        costInput13 = Entry(root, borderwidth=5, width=8)
        costInput13.grid(row=14, column=3)

        # Row 14
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=15, column=0, padx=2, pady=2)

        descInput14 = Entry(root, borderwidth=5, width=50)
        descInput14.grid(row=15, column=1)

        quantityInput14 = Entry(root, borderwidth=5, width=3)
        quantityInput14.grid(row=15, column=2)

        costInput14 = Entry(root, borderwidth=5, width=8)
        costInput14.grid(row=15, column=3)

        # Row 15
        selected = StringVar()
        selected.set(dropOptions[0])
        compDrop = OptionMenu(root, selected, *dropOptions)
        compDrop.grid(row=16, column=0, padx=2, pady=2)

        descInput15 = Entry(root, borderwidth=5, width=50)
        descInput15.grid(row=16, column=1)

        quantityInput15 = Entry(root, borderwidth=5, width=3)
        quantityInput15.grid(row=16, column=2)

        costInput15 = Entry(root, borderwidth=5, width=8)
        costInput15.grid(row=16, column=3)

        # Row 16
        totalCost = Entry(root, borderwidth=5, width=8, state=DISABLED)
        totalCost.grid(row=17, column=3)

        # Defining button functions
        #def multiQuan(): # Multiplies cost of component by quantity
            #return    

        #def totalCost(): # Adds each component cost to calculate total cost
            #return
        
        #def compare(): # Opens new window to compare builds
            #return

        # Creating the buttons
        compareButton = Button(root, text="Compare")
        compareButton.grid(row=17, column=0, padx=5, pady=5)

        calcButton = Button(root, text="Calculate")
        calcButton.grid(row=18, column=3, padx=5, pady=5)
        totalLabel = Label(root, text="Total Cost")
        totalLabel.grid(row=17, column=2, padx=5, pady=5)

        exitButton = Button(root, text="Exit", padx=15)
        exitButton.grid(row=18, column=0, padx=5, pady=5)


def main():
    pcBuilder().mainloop()

if __name__ == "__main__":
    main()

