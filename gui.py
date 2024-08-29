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
    padx=5,
    pady=5,
)


# Labels Section
class WrappingInfoLabel(tk.Label):
    """a type of Label that automatically adjusts the wrap to the size
    has a static text attribute that wont change when using update_text()"""

    def __init__(self, master=None, static_text=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs, text=static_text)
        self.stext = static_text
        self.bind("<Configure>", self.update_wrap)

    def update_wrap(self, event):
        self.config(wraplength=self.master.winfo_width())

    def update_text(self, new_text):
        updated_text = f"{self.stext}\t{new_text}"
        self.config(text=updated_text)


label_font = tkFont.Font(family="Fira Code", size=10)

info_label1 = WrappingInfoLabel(
    master=info_frame,
    font=label_font,
    static_text="Selected File:",
    justify="left",
    fg=DRACULA_PALETTE["green"],
    background=DRACULA_PALETTE["background"],
    anchor="w",
)
info_label2 = WrappingInfoLabel(
    master=info_frame,
    font=label_font,
    static_text="Selected Directory:",
    justify="left",
    fg=DRACULA_PALETTE["green"],
    background=DRACULA_PALETTE["background"],
    anchor="w",
)
info_label3 = WrappingInfoLabel(
    master=info_frame,
    font=label_font,
    static_text="Logs:",
    justify="left",
    fg=DRACULA_PALETTE["green"],
    background=DRACULA_PALETTE["background"],
    anchor="w",
)


# Label Functions
def update_log_info(log):
    old_text = info_label3["text"]
    new_text = f"{old_text}\t{log}"
    info_label3.config(text=new_text)


# Button functions
def get_filename():
    filename = filedialog.askopenfilename()
    info_label1.update_text(filename)
    print(filename)


def get_directory():
    directory = filedialog.askdirectory()
    info_label2.update_text(directory)
    print(directory)


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

info_label1.grid(column=0, row=0, padx=5, sticky="E W")
info_label2.grid(column=0, row=1, padx=5, sticky="E W")
info_label3.grid(column=0, row=2, padx=5, sticky="E W")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=2)
content.columnconfigure(1, weight=2)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)


root.mainloop()
