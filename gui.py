import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont

DRACULA_PALETTE = {
    "background": "#282a36",  # Dark grayish blue
    "current_line": "#44475a",  # Slightly lighter gray-blue
    "selection": "#44475a",  # Same as current_line
    "foreground": "#f8f8f2",  # Near-white
    "comment": "#6272a4",  # Muted blue
    "cyan": "#8be9fd",  # Bright cyan
    "green": "#50fa7b",  # Bright green
    "orange": "#ffb86c",  # Soft orange
    "pink": "#ff79c6",  # Bright pink
    "purple": "#bd93f9",  # Soft purple
    "red": "#ff5555",  # Bright red
    "yellow": "#f1fa8c",  # Pale yellow
}


def get_filename():
    filename = filedialog.askopenfilename()
    print(filename)


def get_directory():
    directory = filedialog.askdirectory()
    print(directory)


# Main Window Config
root = tk.Tk()
root.title("Slides to Markdown")
root.geometry("500x300")

# Content Frame Config
content = tk.Frame(
    master=root,
    padx=10,
    pady=10,
    bg=DRACULA_PALETTE["background"],
)

# Info Frame Config
info_frame = tk.Frame(
    master=content,
    width=200,
    height=100,
    relief="solid",
    bg=DRACULA_PALETTE["background"],
    highlightbackground=DRACULA_PALETTE["purple"],
    highlightcolor=DRACULA_PALETTE["purple"],
    highlightthickness=2,
    bd=0,
)
label_font = tkFont.Font(family="Fira Code", size=10)

info_label = tk.Label(
    master=info_frame,
    font=label_font,
    text="Selected File: N/A\nSelected Directory: N/A\nLogs:",
    justify="left",
    fg=DRACULA_PALETTE["green"],
    background=DRACULA_PALETTE["background"],
)

# Font for buttons
btn_font = tkFont.Font(family="Fira Code", size=12)

# Buttons Config
filebtn = tk.Button(
    master=content,
    text="Choose File",
    command=get_filename,
    width=1,
    font=btn_font,
    bg=DRACULA_PALETTE["selection"],
    fg=DRACULA_PALETTE["cyan"],
    activeforeground=DRACULA_PALETTE["foreground"],
    activebackground=DRACULA_PALETTE["comment"],
    relief="flat",
)

dirbtn = tk.Button(
    master=content,
    text="Choose Directory",
    command=get_directory,
    width=1,
    font=btn_font,
    bg=DRACULA_PALETTE["selection"],
    fg=DRACULA_PALETTE["yellow"],
    activeforeground=DRACULA_PALETTE["foreground"],
    activebackground=DRACULA_PALETTE["comment"],
    relief="flat",
)
createbtn = tk.Button(
    master=content,
    text="Create .md file",
    font=btn_font,
    bg=DRACULA_PALETTE["selection"],
    fg=DRACULA_PALETTE["pink"],
    activeforeground=DRACULA_PALETTE["foreground"],
    activebackground=DRACULA_PALETTE["comment"],
    relief="flat",
)


# Layout Config
content.grid(column=0, row=0, sticky="N S E W")
info_frame.grid(column=0, row=0, sticky="N S E W", columnspan=2, rowspan=2)

filebtn.grid(column=0, row=2, columnspan=1, sticky="E W", padx=10)
dirbtn.grid(column=1, row=2, columnspan=1, sticky="E W", padx=10)
createbtn.grid(column=0, row=3, columnspan=2, sticky="E W", padx=10)
info_label.grid(column=0, row=0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=2)
content.columnconfigure(1, weight=2)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)


root.mainloop()
