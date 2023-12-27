import tkinter as tk


def update_textbox(value):
    current_text = textbox_str.get()
    if value == "=":
        result = str(eval(current_text))
        textbox_str.set(result)
    else:
        updated_text = current_text + value
        textbox_str.set(updated_text)


root = tk.Tk()
# root.geometry("500x500")
root.title("Hehe")

textbox_str = tk.StringVar()

textbox = tk.Entry(root, textvariable=textbox_str, width=30)
textbox.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "="]

row_val = 1
col_val = 0

for value in values:
    button = tk.Button(
        root, text=value, command=lambda v=value: update_textbox(v), width=5, height=2
    ).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 2:
        row_val += 1
        col_val = 0


root.mainloop()
