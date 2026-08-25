import tkinter as tk
import webbrowser
from urllib.parse import quote_plus

def search(entry):
    query = entry.get().strip()
    if query:
        webbrowser.open_new_tab(
            "https://www.google.com/search?q=" + quote_plus(query)
        )


def search_all():
    for entry in entries:
        query = entry.get().strip()

        if query:
            webbrowser.open_new_tab(
                "https://www.google.com/search?q=" + quote_plus(query)
            )


root = tk.Tk()
root.title("MultiSearch")
root.geometry("500x480")
root.resizable(False, False)

titles = [
    "Table 1",
    "Table 2",
    "Table 3",
    "Table 4",
    "Table 5",
    "Table 6",
    "Table 7",
    "Table 8",
    "Table 9",
    "Table 10",
]

entries = []

for title in titles:
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=12, pady=4)

    label = tk.Label(frame, text=title, width=12, anchor="w")
    label.pack(side="left")

    entry = tk.Entry(frame)
    entry.pack(side="left", fill="x", expand=True, padx=5)

    entries.append(entry)

    button = tk.Button(
        frame,
        text="Search",
        command=lambda e=entry: search(e)
    )
    button.pack(side="right")

    entry.bind(
        "<Return>",
        lambda event, e=entry: search(e)
    )


# GO = search every filled box in its own browser tab
go_button = tk.Button(
    root,
    text="GO",
    command=search_all,
    width=20,
    height=2,
    bg="#4CAF50",
    fg="white"
)
go_button.pack(pady=15)

root.mainloop()
