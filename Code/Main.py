#Import required libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 
import tkinter.font as tkFont
import os
import random
import time
import threading
#Removes place holder text when user is entering data
def on_entry_click(event, entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, tk.END)
        entry_widget.configure(foreground='black')

#if no data is in the entry block is displays the placeholder text
def on_entry_leave(event, entry_widget, placeholder):
    if entry_widget.get() == '':
        entry_widget.insert(0, placeholder)
        entry_widget.configure(foreground='grey')

#Primary function that checks the directory size and creates new files with random data if the desired size has not been met
def run_process():

    directory_path = entry1.get()
    desired_size = entry2.get()
    desired_size_float = float(desired_size)
    total_size = 0

    while total_size <= desired_size_float:
        random_number = random.randint(0, 30)
        random_word = random.choice(open('Randomwords.txt').read().splitlines())
        file_extension = random.choice(['csv', 'jpeg', 'docx', 'xlsx', 'png', 'pdf', 'mp3', 'mp4', 'zip', 'html', 'exe', 'psd', 'rar'])
        if random.randint(0, 1):
            filename = f"{random_word}{random_number}.{file_extension}"
        else:
            filename = f"{random_word}.{file_extension}"
        
        filepath = os.path.join(directory_path, filename)
        if (file_extension == "mp3" or file_extension == "mp4" or file_extension == "zip" or file_extension == "exe" or file_extension == "rar"):
            size_in_bytes = random.randint(1024, 1073741824)
           
        else:
            size_in_bytes = random.randint(1024, 1048576)
         
        data = os.urandom(size_in_bytes)
        
        with open(filepath, 'wb') as f:
            f.write(data)

        total_size += size_in_bytes / (1024 * 1024 * 1024)
        message_text.insert(tk.END, f"{filepath} was created\n")
        message_text.insert(tk.END, f"Folder size is now:{total_size}GB\n")
        message_text.update_idletasks()
        message_text.yview_moveto(1.0)
        time.sleep(5)
    message_text.insert(tk.END, f"process complete")

#sends the run_process to a different thread to allow the GUI to function in real time
def start_process_thread():
    process_thread = threading.Thread(target=run_process)
    process_thread.start()

#Below this line is the code that defines the visible GUI
root = tk.Tk()
root.title("FileFiesta")
custom_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
sombrero = Image.open("sombrero_PNG7.png")
icon = ImageTk.PhotoImage(sombrero)
root.iconphoto(True, icon)
#This section defines the dark mode theme
dark_mode_bg = "#282828"
dark_mode_fg = "white"
dark_mode_entry_bg = "#333333"
dark_mode_entry_fg = "white"
dark_mode_button_bg = "#666666"
dark_mode_button_fg = "black"
dark_mode_label_fg = "white"
dark_mode_message_text_bg = "#222222"
dark_mode_message_text_fg = "white"
style = ttk.Style()
style.configure("TFrame", background=dark_mode_bg)
style.configure("TLabel", foreground=dark_mode_label_fg, background=dark_mode_bg)
style.configure("TButton", foreground=dark_mode_button_fg, background=dark_mode_button_bg)
style.configure("TEntry", foreground=dark_mode_entry_fg, background=dark_mode_entry_bg)
style.configure("TText", foreground=dark_mode_message_text_fg, background=dark_mode_message_text_bg)

#This section defines the main GUI segments
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="FileFiesta", font=custom_font).grid(column=0, row=0)

#Placeholder and entry block for directory location to write new files
placeholder1 = "Directory to write files to: 'c:\\temp\\'"
entry1 = ttk.Entry(frm, width=50, foreground='grey')
entry1.insert(0, placeholder1)
entry1.bind("<FocusIn>", lambda event: on_entry_click(event, entry1, placeholder1))
entry1.bind("<FocusOut>", lambda event: on_entry_leave(event, entry1, placeholder1))
entry1.grid(row=2, column=0, pady=10, padx=10)

#Placeholder and entry block for desired directory size. The code may exceed the limit as it only stops after it goes has the limit set
placeholder2 = "Desired size of directory in GB: '0.1' or '1' or '2.3'"
entry2 = ttk.Entry(frm, width=50, foreground='grey')
entry2.insert(0, placeholder2)
entry2.bind("<FocusIn>", lambda event: on_entry_click(event, entry2, placeholder2))
entry2.bind("<FocusOut>", lambda event: on_entry_leave(event, entry2, placeholder2))
entry2.grid(row=3, column=0, pady=10, padx=10)

#Run Button that starts the code
button1 = ttk.Button(frm, text="Run", command=start_process_thread)
button1.grid(column=0, row=4, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

#exits the program
button2 = ttk.Button(frm, text="Stop", command=root.destroy)
button2.grid(column=0, row=5, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

message_text = tk.Text(frm, wrap=tk.WORD, width=35, height=10, background='grey')
message_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()