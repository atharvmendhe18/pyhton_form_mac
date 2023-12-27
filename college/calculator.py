import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Hello World")

lable = tk.Label(root, text="Calculator", font=("Arial", 18))
lable.pack(padx=10, pady=10)

textbox = tk.Text(root, font=("Arial", 18), height=3)
textbox.pack(padx=20, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn1 = tk.Button(
    buttonframe,
    text="2",
    font=("Arial", 18),
)
btn1.grid(row=0, column=1, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn1.grid(row=0, column=2, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn1.grid(row=1, column=0, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn1.grid(row=1, column=1, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn1.grid(row=1, column=2, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="7", font=("Arial", 18))
btn1.grid(row=2, column=0, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="8", font=("Arial", 18))
btn1.grid(row=2, column=1, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="9", font=("Arial", 18))
btn1.grid(row=2, column=2, sticky=tk.W + tk.E)

btn1 = tk.Button(buttonframe, text="0", font=("Arial", 18))
btn1.grid(row=3, column=1, sticky=tk.W + tk.E)

buttonframe.pack(fill="x")


root.mainloop()
