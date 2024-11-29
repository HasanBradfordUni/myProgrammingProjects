import pytesseract
from PIL import Image
import pyautogui
import pyperclip
import time

# Specify the Tesseract executable path if it's not in the PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\fifau\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_poll_text(image_path):
    """Extract poll text from an image using OCR."""
    image = Image.open(image_path)
    poll_text = pytesseract.image_to_string(image)
    return poll_text

def parse_poll(poll_text):
    """Parse poll question and options from the extracted text."""
    lines = poll_text.strip().split("\n")
    question = lines[0]  # Assume the first line is the poll question
    options = lines[1:]  # Remaining lines are options
    return question, options

def automate_whatsapp_poll(question, options):
    """Automate the creation of a poll in WhatsApp Web."""
    # Wait a few seconds to let user switch to WhatsApp
    time.sleep(2)
    print(question)

    # Type the poll question
    pyperclip.copy(question)
    pyautogui.hotkey("ctrl", "v")  # Paste question
    key = "tab"
    pyautogui.press(key)  # Press Enter to send the question
    time.sleep(1)
    key = "down"

    # Type each option
    for option in options:
        if option != "€@ Select one or more":
            option = option.replace("CO", "")
            option = option.replace(" 0", "")
            option = option.replace("@i", "")
            option = option.replace("©", "")
            option = option.replace("O ", "")
            option = option.replace("C D) ", "")
            option = option.replace("(V) ", "")                        
            print(option)
            pyperclip.copy(option)
            pyautogui.hotkey("ctrl", "v")  # Paste each option
            pyautogui.press(key)  # Press Enter to send the option
            time.sleep(1)

if __name__ == "__main__":
    image_path = input("First enter the path to the image file: ")

    # Extract poll text from the image
    poll_text = extract_poll_text(image_path)

    # Parse the poll text into question and options
    question, options = parse_poll(poll_text)

    # Automate WhatsApp poll creation
    print("Now switch to WhatsApp and open the desired chat...")
    automate_whatsapp_poll(question, options)
    print("Poll sent successfully!")
