from tkinter import *
root = Tk()
root.title("Calculator")
#create a text entry box
text_entry = Entry(root, width=35, borderwidth=5)
text_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#create a function to handle the button clicks
def button_click(number):
    current = text_entry.get()
    text_entry.delete(0, END)
    text_entry.insert(0, str(current) + str(number))

#create a function to handle the clear button
def button_clear():
    text_entry.delete(0, END)

#craeting buttons for numbers
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1)).grid(row=1, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2)).grid(row=1, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3)).grid(row=1, column=2)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7)).grid(row=3, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8)).grid(row=3, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9)).grid(row=3, column=2)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0)).grid(row=4, column=0)
button_add = Button(root, text="+", padx=40, pady=20).grid(row=1, column=3)
button_sub = Button(root, text="-", padx=40, pady=20).grid(row=2, column=3)
button_mul = Button(root, text="*", padx=40, pady=20).grid(row=3, column=3)
button_div = Button(root, text="/", padx=40, pady=20).grid(row=4, column=3)
button_equal = Button(root, text="=", padx=40, pady=20).grid(row=4, column=2)
button_clear = Button(root, text="Clear", padx=40, pady=20, command=button_clear).grid(row=4, column=1)



#main function
root.mainloop()