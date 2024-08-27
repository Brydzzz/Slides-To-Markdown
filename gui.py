import tkinter as tk


root = tk.Tk()
root.title("Slides to Markdown")
root.geometry("500x300")

content = tk.Frame(root, padx=10, pady=10)

file_frame = tk.Frame(
    content, borderwidth=2, relief="solid", width=200, height=100
)
dir_frame = tk.Frame(
    content, borderwidth=2, relief="solid", width=200, height=100
)

filebtn = tk.Button(content, text="Choose File")
dirbtn = tk.Button(content, text="Choose Directory")

content.grid(column=0, row=0, sticky="N S E W")
file_frame.grid(column=0, row=0, rowspan=2, padx=5, sticky="N S E W")
dir_frame.grid(column=1, row=0, rowspan=2, sticky="N S E W")

filebtn.grid(column=0, row=2, padx=5, sticky="N S E W")
dirbtn.grid(column=1, row=2, sticky="N S E W")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.rowconfigure(1, weight=1)

root.mainloop()
