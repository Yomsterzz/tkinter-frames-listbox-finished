import tkinter as tk

def show_fruit(event):
    item_index = listbox1.curselection()
    for index in item_index:
        print(listbox1.get(index))

def add_item():
    imaginary_fruit = entry.get()
    if imaginary_fruit:
        listbox1.insert(tk.END, imaginary_fruit)
        entry.delete(0, tk.END)

def clear():
    items = listbox1.curselection()
    for i in items:
        listbox1.delete(i)
        
window = tk.Tk()
window.title("Frames")
window.geometry("1000x800")

mainframe = tk.Frame(window, borderwidth=20, relief="groove")
mainframe.pack(fill=tk.BOTH, expand=True)

subframe1 = tk.Frame(mainframe, borderwidth=20, relief="ridge")
subframe1.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=10, pady=20)

subframe2 = tk.Frame(mainframe, borderwidth=20, relief="solid")
subframe2.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=10, pady=20)

label1 = tk.Label(subframe1, text="WOAH", font=("Helvetica", 20))
label1.pack(pady=10)

listbox1 = tk.Listbox(subframe1, selectmode=tk.MULTIPLE)
listbox1.pack()

fruits = ["apple", "orange", "banana", "cherry"]

for fruit in fruits:
    listbox1.insert(tk.END, fruit)

listbox1.bind("<<ListboxSelect>>", show_fruit)

entry = tk.Entry(subframe1, font=("Helvetica", 20))
entry.pack(pady=30)

add_item_button = tk.Button(subframe1, text="Add Item", command=add_item)
add_item_button.pack(padx=10, pady=10)

delete_item_button = tk.Button(subframe1, text="Delete Item", command=clear)
delete_item_button.pack(padx=10, pady=10)

window.mainloop()