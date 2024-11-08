#link opener
import webbrowser

link = input("Enter a link to open: ")

while True:    
    try:
        webbrowser.open(link)
        break
    except:
        link = input("Enter a link to open: ")
