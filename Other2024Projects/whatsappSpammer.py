import pyautogui
import pyperclip
import time

# Get the message from the user
message = input("Enter the message you want to spam: ")

# Give the user 5 seconds to focus on the input field
print("You have 5 seconds to switch to WhatsApp...")
time.sleep(5)
#copy the message to clipboard
pyperclip.copy(message)

# Loop to send the message 100 times
for _ in range(100):
    # Paste the message and send it
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(0.1)  # Small delay to avoid overwhelming the system