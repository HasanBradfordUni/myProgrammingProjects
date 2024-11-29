import pytesseract
from PIL import Image
import pyautogui
import pyperclip
import time
import pywhatkit

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
    # Wait a few seconds to switch to WhatsApp Web
    pywhatkit.sendwhatmsg_to_group_instantly("LdBPZUwXSmy9WTCpsrAfmU", "")
    time.sleep(3)

    # Type the poll question
    pyperclip.copy(question)
    pyautogui.hotkey("ctrl", "v")  # Paste question
    key = "enter"
    pyautogui.press(key)  # Press Enter to send the question
    time.sleep(1)

    # Type each option
    for option in options:
        if option != "€@ Select one or more":
            option = option.replace("CO", "")
            option = option.replace(" 0", "")
            option = option.replace("@i", "")
            option = option.replace("©", "")
            print(option)
            pyperclip.copy(option)
            pyautogui.hotkey("ctrl", "v")  # Paste each option
            pyautogui.press(key)  # Press Enter to send the option
            time.sleep(1)

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")

    # Extract poll text from the image
    poll_text = extract_poll_text(image_path)

    # Parse the poll text into question and options
    question, options = parse_poll(poll_text)

    # Automate WhatsApp poll creation
    print("Switch to WhatsApp Web and open the chat...")
    automate_whatsapp_poll(question, options)
    print("Poll sent successfully!")
