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


class WrappingInfoLabel(tk.Label):
    """a type of Label that automatically adjusts the wrap to the size
    has a static text attribute that wont change when using update_text()"""

    def __init__(self, master=None, static_text=None, **kwargs):
        tk.Label.__init__(self, master, text=static_text, **kwargs)
        self.stext = static_text
        self.bind("<Configure>", self.update_wrap)

    def update_wrap(self, event):
        self.config(wraplength=self.master.winfo_width())

    def update_text(self, new_text):
        updated_text = f"{self.stext}\t{new_text}"
        self.config(text=updated_text)


class LogLabel(WrappingInfoLabel):
    def __init__(
        self, master=None, static_text="Logs:", max_logs=5, **kwargs
    ):
        WrappingInfoLabel.__init__(
            self, master, static_text=static_text, **kwargs
        )
        self.max_logs = max_logs
        self.logs_count = 0

    def update_log_info(self, new_log):
        if self.logs_count < self.max_logs:
            old_text = self["text"]
            new_text = f"{old_text}\n{new_log}"
            self.logs_count += 1
        else:
            new_text = f"{self.stext}\n{new_log}"
            self.logs_count = 1
        self.config(text=new_text)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, master=parent, *args, **kwargs)
        self.parent = parent
        self.configure(padx=10, pady=10, bg=DRACULA_PALETTE["background"])
        self.filename = None
        self.directory = None

        # Info Frame Config
        info_frame = tk.Frame(
            master=self,
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

        # Labels Config
        label_font = tkFont.Font(family="Fira Code", size=10)

        self.file_label = WrappingInfoLabel(
            master=info_frame,
            font=label_font,
            static_text="Selected File:",
            justify="left",
            fg=DRACULA_PALETTE["green"],
            background=DRACULA_PALETTE["background"],
            anchor="w",
        )
        self.dir_label = WrappingInfoLabel(
            master=info_frame,
            font=label_font,
            static_text="Selected Directory:",
            justify="left",
            fg=DRACULA_PALETTE["green"],
            background=DRACULA_PALETTE["background"],
            anchor="w",
        )
        self.log_label = LogLabel(
            master=info_frame,
            font=label_font,
            static_text="Logs:",
            justify="left",
            fg=DRACULA_PALETTE["green"],
            background=DRACULA_PALETTE["background"],
            anchor="w",
        )

        # Font for buttons
        btn_font = tkFont.Font(family="Fira Code", size=12)

        # Buttons Config
        filebtn = tk.Button(
            master=self,
            text="Choose File",
            command=self.get_filename,
            width=1,
            font=btn_font,
            bg=DRACULA_PALETTE["selection"],
            fg=DRACULA_PALETTE["cyan"],
            activeforeground=DRACULA_PALETTE["foreground"],
            activebackground=DRACULA_PALETTE["comment"],
            relief="flat",
        )

        dirbtn = tk.Button(
            master=self,
            text="Choose Directory",
            command=self.get_directory,
            width=1,
            font=btn_font,
            bg=DRACULA_PALETTE["selection"],
            fg=DRACULA_PALETTE["yellow"],
            activeforeground=DRACULA_PALETTE["foreground"],
            activebackground=DRACULA_PALETTE["comment"],
            relief="flat",
        )
        createbtn = tk.Button(
            master=self,
            text="Create .md file",
            command=self.create_md_file,
            font=btn_font,
            bg=DRACULA_PALETTE["selection"],
            fg=DRACULA_PALETTE["pink"],
            activeforeground=DRACULA_PALETTE["foreground"],
            activebackground=DRACULA_PALETTE["comment"],
            relief="flat",
        )

        # Layout Config
        self.grid(column=0, row=0, sticky="N S E W")
        info_frame.grid(
            column=0, row=0, sticky="N S E W", columnspan=2, rowspan=2
        )

        filebtn.grid(column=0, row=2, columnspan=1, sticky="E W", padx=10)
        dirbtn.grid(column=1, row=2, columnspan=1, sticky="E W", padx=10)
        createbtn.grid(column=0, row=3, columnspan=2, sticky="E W", padx=10)

        self.file_label.grid(column=0, row=0, padx=5, sticky="E W")
        self.dir_label.grid(column=0, row=1, padx=5, sticky="E W")
        self.log_label.grid(column=0, row=2, padx=5, sticky="E W")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    # Button functions
    def get_filename(self):
        self.filename = filedialog.askopenfilename()
        self.file_label.update_text(self.filename)

    def get_directory(self):
        self.directory = filedialog.askdirectory()
        self.dir_label.update_text(self.directory)

    def create_md_file(self):
        self.log_label.update_log_info("Checking requirements...")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Slides to Markdown")
    root.geometry("500x300")
    MainApplication(parent=root).pack(side="top", fill="both", expand=True)
    root.mainloop()
