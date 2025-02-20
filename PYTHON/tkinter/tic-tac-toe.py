import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe!")

# First Horizontal row 

def color_change():
    counter = 0
    if counter == 0:
        btn1.config(bg='orange')
    elif (counter % 2) == 1:
        btn1.config(bg='blue')
        


btn1 = tk.Button(root, text=" ", command=color_change)
btn1.grid(row = 0, column= 0)
btn1.config(width=8, height=4)

btn2 = tk.Button(root, text=" ")
btn2.grid(row = 0, column= 1)
btn2.config(width=8, height=4)

btn3 = tk.Button(root, text=" ")
btn3.grid(row = 0, column= 2)
btn3.config(width=8, height=4)


#Second horizontal row 
btn4 = tk.Button(root, text=" ")
btn4.grid(row = 1, column= 0)
btn4.config(width=8, height=4)

btn5 = tk.Button(root, text=" ")
btn5.grid(row = 1, column= 1)
btn5.config(width=8, height=4)

btn6 = tk.Button(root, text=" ")
btn6.grid(row = 1, column= 2)
btn6.config(width=8, height=4)

#Third horizontal row
btn7 = tk.Button(root, text=" ")
btn7.grid(row = 2, column= 0)
btn7.config(width=8, height=4)

btn8 = tk.Button(root, text=" ")
btn8.grid(row = 2, column= 1)
btn8.config(width=8, height=4)

btn9 = tk.Button(root, text=" ")
btn9.grid(row = 2, column= 2)
btn9.config(width=8, height=4)

root.mainloop()