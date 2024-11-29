"""A small app that will convert from markdown to plaintext
and either allow you to copy it or export it then"""
import pyperclip
from tkinter import *

class ConversionWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Markdown to Plaintext converter')
        self.geometry('1000x500')

        # Create text widget for conversion
        self.markdownTextBox = Text(self, width=60)
        self.markdownTextBox.grid(row=0, column=0, sticky='nsew', padx=7, pady=10)

        self.plaintextBox = Text(self, width=60)
        self.plaintextBox.grid(row=0, column=1, sticky='nsew', padx=7, pady=10)

        # Create convert button
        self.convertButton = Button(self, text='convert', command=self.convert_text)
        self.convertButton.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        self.filenameEntry = Entry(self)
        self.filenameEntry.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

        # Create export button
        self.exportButton = Button(self, text='export', command=self.writeToFile)
        self.exportButton.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        # Create copy button
        self.copyButton = Button(self, text='copy', command=self.copyText)
        self.copyButton.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)

    def convert_text(self):
        markdownText = self.markdownTextBox.get("1.0", 'end')
        if markdownText:
            # Add user message to conversation
            self.plaintextBox.delete('1.0', 'end')
            self.plaintextBox.configure(state='normal')
            plaintext = markdownText.replace("#", "").replace("*", "").replace("`", "")
            self.plaintextBox.insert('end', plaintext)
            self.plaintextBox.configure(state='disabled')
    
    def writeToFile(self):
        filename = self.getTestFilename()+".txt"
        text = self.plaintextBox.get("1.0", "end")
        with open(filename, 'w') as file:
            file.write(text)
            file.close()

    def getTestFilename(self):
        #print(self.filenameEntry.get())
        return self.filenameEntry.get()
    
    def copyText(self):
        text = self.plaintextBox.get("1.0", "end")
        pyperclip.copy(text)

if __name__ == "__main__":
    print("""Welcome to the small tool that converts text input 
from markdown styling to plaintext developed by 
Akhtar Hasan aka Python Programmer""")
    window = ConversionWindow()
    window.mainloop()
