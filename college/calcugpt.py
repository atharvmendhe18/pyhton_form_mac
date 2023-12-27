import tkinter as tk


def add_value(value):
    current_text = text_var.get()
    if value == "=":
        result = str(eval(current_text))
        text_var.set(result)
    else:
        updated_text = current_text + value
        text_var.set(updated_text)


# Create the main window
root = tk.Tk()
root.title("Button Press Demo")

# Create a StringVar to hold the text in the textbox
text_var = tk.StringVar()

# Create a Textbox to display the values
text_box = tk.Entry(root, textvariable=text_var, width=30)
text_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create buttons with values
values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "="]
row_val = 1
col_val = 0

for value in values:
    tk.Button(
        root, text=value, width=5, height=2, command=lambda v=value: add_value(v)
    ).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()
