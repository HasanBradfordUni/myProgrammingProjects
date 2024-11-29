#Importing the modules
import vertexai
from vertexai.generative_models import GenerativeModel
import google.auth
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pyperclip

credentials, project_id = google.auth.default()

vertexai.init(project="generalpurposeai", location="us-central1")

model = GenerativeModel(model_name="gemini-1.0-pro")

class ChatbotWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('AI Cover Letter Writer')
        self.geometry('1000x600')
        self.cleanOutput = ""

        # Create scrolled text widget for conversation
        self.resume_section = ScrolledText(self, wrap=NONE, height=15, width=60)
        self.resume_section.grid(row=0, column=0, sticky='nsew')

        self.job_desc_section = ScrolledText(self, wrap=NONE, height=15, width=60)
        self.job_desc_section.grid(row=0, column=1, sticky='nsew')

        self.response_section = ScrolledText(self, wrap=NONE, height=20)
        self.response_section.configure(state='disabled')
        self.response_section.grid(row=1, column=0, columnspan=2, sticky='nsew')

        # Create send button
        self.send_button = Button(self, text='Send', command=self.send_message)
        self.send_button.grid(row=2, column=0, sticky='nsew')

        # Create copy button
        self.copy_button = Button(self, text='Copy', command=self.copy_response)
        self.copy_button.grid(row=2, column=1, sticky='nsew')

        # Create clean output button
        self.clean_output_button = Button(self, text='Clean Output', command=self.clean_output)
        self.clean_output_button.grid(row=3, column=0, sticky='nsew')

        # Create export button
        self.export_button = Button(self, text='Export', command=self.export_response)
        self.export_button.grid(row=3, column=1, sticky='nsew')

    def send_message(self):
        resume = self.resume_section.get("1.0", 'end')
        job_description = self.job_desc_section.get("1.0", 'end')
        if resume and job_description:
            # Add user message to conversation
            self.response_section.delete('1.0', 'end')
            self.response_section.configure(state='normal')
            prompt = f"""Given the contents of my CV (Resume) and the job description which are below:
            \nMy Resume/CV is as follows: {resume}
            The job description is as follows: {job_description}
            \nPlease generate an appropriate cover letter."""
            responses = model.generate_content(prompt, stream=True)
            insertionText = ""
            for response in responses:
                insertionText = response.text
                self.response_section.insert('end', insertionText)
            self.response_section.configure(state='disabled')

    def copy_response(self):
        pyperclip.copy(self.cleanOutput)

    def clean_output(self):
        self.cleanOutput = self.response_section.get("1.0", 'end')
        self.cleanOutput = self.cleanOutput.replace("#", "").replace("*", "").replace("`", "")

    def export_response(self):
        pass

if __name__ == "__main__":
    window = ChatbotWindow()
    window.mainloop()
