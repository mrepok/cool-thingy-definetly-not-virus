import subprocess
import sys
import ctypes
import time
import random
import threading
import os
import tkinter as tk
from tkinter import messagebox

# Function to shake the command prompt window
def shake_window(window_handle, duration=20):
    start_time = time.time()
    center_x, center_y = 500, 300  # Center of the screen
    while time.time() - start_time < duration:
        new_x = center_x + random.randint(-20, 20)
        new_y = center_y + random.randint(-20, 20)
        ctypes.windll.user32.MoveWindow(window_handle, 
                                         new_x, 
                                         new_y, 
                                         800, 
                                         600, 
                                         True)
        time.sleep(0.1)

# Function to type text in the command prompt
def type_text():
    text = "THERE IS NO ESCAPE"
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.5)  # Wait a bit before typing "A"

    for _ in range(20):  # Type "A" followed by a new line 20 times
        sys.stdout.write("A\n")
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.5)  # Wait a bit before typing "CAN I SEE HOW YOU LOOK LIKE??"
    
    text = "CAN I SEE HOW YOU LOOK LIKE??"
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)  # Typing more slowly

# Function to open the browser and visit the IP address website
def open_browser():
    time.sleep(11)  # Wait for typing "CAN I SEE HOW YOU LOOK LIKE??"
    os.startfile("microsoft.windows.camera:")
    time.sleep(5)  # Wait for 5 seconds
    os.system("TASKKILL /F /IM WindowsCamera.exe")  # Close the camera app
    sys.stdout.write("NICE")
    sys.stdout.flush()
    time.sleep(0.5)  # Wait a bit before typing "I WILL DOX YOU"
    sys.stdout.write("\nI WILL DOX YOU")
    sys.stdout.flush()
    time.sleep(0.5)  # Wait a bit before opening browser
    
    # Open browser and search for "what is my ip address"
    if os.path.exists("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"):
        browser = "chrome.exe"
        browser_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    elif os.path.exists("C:\\Program Files\\Mozilla Firefox\\firefox.exe"):
        browser = "firefox.exe"
        browser_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    else:
        sys.exit("No supported browser found!")
    
    os.startfile(browser_path)
    time.sleep(3)  # Wait for browser to open

    # Open a new tab with the URL
    if browser == "chrome.exe":
        url = "https://whatismyipaddress.com/"
        os.system(f'start chrome.exe "{url}"')
    elif browser == "firefox.exe":
        url = "https://whatismyipaddress.com/"
        os.system(f'start firefox.exe -new-tab "{url}"')
        time.sleep(2)
        os.system("TASKKILL /F /IM firefox.exe")

# Function to get the IP address
def get_ip():
    time.sleep(15) # Wait for the browser to open and load the page
    for _ in range(30):  # Print IP address 30 times
        os.system('curl https://ifconfig.me/ip > temp.txt')
        with open("temp.txt", "r") as f:
            ip = f.read().strip()
            sys.stdout.write(f"\nYour IP address is: {ip}")
            sys.stdout.flush()
            f.close()
        os.system("del temp.txt")
        time.sleep(0.1)  # Sleep for 0.1 seconds

# Function to close all windows
def close_windows():
    time.sleep(30)  # Wait for spamming IP address
    os.system("TASKKILL /F /IM explorer.exe")  # Close all windows

# Function to show a message box
def show_message():
    time.sleep(33)  # Wait for closing all windows
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Error", "You did a mistake, your computer is mine")
    root.destroy()

# Main function
def main():
    # Open command prompt
    subprocess.Popen("cmd", shell=True)

    # Wait a bit for cmd to open
    time.sleep(1)

    # Find the handle of the command prompt window
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()

    # Set window title
    ctypes.windll.kernel32.SetConsoleTitleW("haha")

    # Shake the window
    shake_thread = threading.Thread(target=shake_window, args=(hwnd,))
    shake_thread.start()

    # Type text
    type_thread = threading.Thread(target=type_text)
    type_thread.start()

    # Open browser
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.start()

    # Get IP address
    ip_thread = threading.Thread(target=get_ip)
    ip_thread.start()

    # Close all windows
    close_thread = threading.Thread(target=close_windows)
    close_thread.start()

    # Show message box
    message_thread = threading.Thread(target=show_message)
    message_thread.start()

    shake_thread.join()
    type_thread.join()
    browser_thread.join()
    ip_thread.join()
    close_thread.join()
    message_thread.join()
    sys.exit()

if __name__ == "__main__":
    main()
