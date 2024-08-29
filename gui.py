import tkinter as tk
from tkinter import filedialog


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


content = tk.Frame(
    root,
    padx=10,
    pady=10,
    bg=DRACULA_PALETTE["background"],
)

info_frame = tk.Frame(
    content,
    width=200,
    height=100,
    relief="solid",
    bg=DRACULA_PALETTE["background"],
    highlightbackground=DRACULA_PALETTE["purple"],
    highlightcolor=DRACULA_PALETTE["purple"],
    highlightthickness=2,
    bd=0,
)

filebtn = tk.Button(
    content, text="Choose File", command=get_filename, width=1
)
dirbtn = tk.Button(
    content, text="Choose Directory", command=get_directory, width=1
)
createbtn = tk.Button(content, text="Create .md file", padx=10, pady=10)


content.grid(column=0, row=0, sticky="N S E W")
info_frame.grid(column=0, row=0, sticky="N S E W", columnspan=2, rowspan=2)

filebtn.grid(column=0, row=2, columnspan=1, sticky="E W")
dirbtn.grid(column=1, row=2, columnspan=1, sticky="E W")
createbtn.grid(column=0, row=3, columnspan=2, sticky="E W")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=2)
content.columnconfigure(1, weight=2)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)


root.mainloop()
