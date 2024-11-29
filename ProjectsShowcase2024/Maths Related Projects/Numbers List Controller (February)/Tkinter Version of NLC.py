import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    fileText = []
    filepath = askopenfilename(
        filetypes=[("List Files", "*.list"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.config(state = tk.NORMAL)
    txt_edit.delete("1.0", tk.END)
    txt_edit.config(state= "disabled")
    file = open(filepath, mode="r", encoding="utf-8")
    for line in file:
        line = line.strip("\n")
        fileText.append(line)
    window.title(f"Simple List Editor - {filepath}")
    return fileText

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("List Files", "*.list"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    else:
        return filepath
    window.title(f"Simple List Editor - {filepath}")

def loadList():
    global thisList
    thisList = []
    fileOutput = open_file()
    for number in fileOutput:
        thisList.append(int(number))
    txt_edit.config(state = tk.NORMAL)
    txt_edit.insert(tk.END, thisList)
    txt_edit.config(state= "disabled")

def addToList(thisList):
    numToAdd = numberEntry.get()
    thisList.append(int(numToAdd))
    txt_edit.config(state = tk.NORMAL)
    txt_edit.delete("1.0", tk.END)
    txt_edit.insert(tk.END, thisList)
    txt_edit.config(state= "disabled")

def saveList(thisList):
    filepath = save_file()
    file = open(filepath, 'w')
    for number in thisList:
        file.write(str(number)+"\n")
    file.close()

def removeFromList(thisList):
    first = thisList[0]
    thisList.remove(first)
    txt_edit.config(state = tk.NORMAL)
    txt_edit.delete("1.0", tk.END)
    txt_edit.insert(tk.END, thisList)
    txt_edit.config(state= "disabled")

window = tk.Tk()
window.title("Simple List Editor")

window.rowconfigure(1, minsize=400, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
frm_controls = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Load List", command=loadList)
btn_save = tk.Button(frm_buttons, text="Save As...", command=lambda: saveList(thisList))
btn_add = tk.Button(frm_controls, text="Add to List", command=lambda: addToList(thisList))
numberEntry = tk.Entry(frm_controls)
btn_remove = tk.Button(frm_controls, text="Remove from list", command=lambda: removeFromList(thisList))

txt_edit.config(state= "disabled")


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_add.grid(row=0, column=0, sticky="ns", padx=5, pady=5)
numberEntry.grid(row=0, column=1, sticky="ns", padx=5, pady=5)
btn_remove.grid(row=0, column=2, sticky="ns", padx=5, pady=5)

frm_controls.grid(row=0, columnspan=2)
frm_buttons.grid(row=1, column=0)
txt_edit.grid(row=1, column=1)

window.mainloop()
