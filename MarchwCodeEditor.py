import tkinter as tk
from tkinter import messagebox, filedialog, font, ttk
import webbrowser
import subprocess
import os

class VersionSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Select Version")

        # Ustawienie niestandardowego tła
        self.background_image = tk.PhotoImage(file="background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Ustawienie niestandardowego fontu dla napisu
        self.custom_font = font.Font(family="Helvetica", size=30, weight="bold")

        # Dodanie napisu Select Version
        self.label = tk.Label(self, text="Select Version", font=self.custom_font, bg="white")
        self.label.pack(pady=20)

        # Ustawienia ComboBoxa z wersjami
        self.version = tk.StringVar()
        self.version.set("v1.1.0-Alpha")

        self.version_options = [
            "v1.0.0-Beta",
            "v1.0.1",
            "v1.1.0-Alpha",
            "v2.0.0 Coming Soon..."
        ]

        self.version_menu = ttk.Combobox(self, textvariable=self.version, values=self.version_options, font=("Helvetica", 16))
        self.version_menu.pack(pady=10)

        # Przycisk "Launch"
        self.start_button = tk.Button(self, text="Launch", font=("Helvetica", 16), command=self.launch_editor)
        self.start_button.pack(pady=20)

        # Zamykanie aplikacji
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def launch_editor(self):
        selected_version = self.version.get()
        self.destroy()  # Zamknięcie okna wyboru wersji

        if selected_version == "v1.0.0-Beta":
            root = tk.Tk()
            editor = CodeEditorV1_Beta(root)
            root.mainloop()

        elif selected_version == "v1.0.1":
            root = tk.Tk()
            editor = CodeEditorV1(root)
            root.mainloop()

        elif selected_version == "v1.1.0-Alpha":
            root = tk.Tk()
            editor = CodeEditorV1_1_0(root)
            root.mainloop()

        elif selected_version == "v2.0.0 Comming Soon...":
            version_selector = VersionSelector()
            version_selector.mainloop()

        #elif selected_version == "v2.0.0":
        #    root = tk.Tk()
        #    editor = CodeEditorV2(root)
        #    root.mainloop()
            
        #version_selector = VersionSelector()  # Ponowne otwarcie okna wyboru wersji
        #version_selector.mainloop()


    def on_close(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.destroy()

class CodeEditorV1_Beta:
    def __init__(self, root):
        self.root = root
        self.filename = None
        self.root.title("MarchwCodeEditor v1.0.0-Beta")

        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")



class CodeEditorV1:
    def __init__(self, root):
        self.root = root
        self.filename = None
        self.root.title("MarchwCodeEditor")

        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Website", command=self.open_website)
        self.help_menu.add_command(label="Discord", command=self.open_discord)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Current version: v1.0.1")

        self.root.bind("<Control-s>", self.save_file_shortcut)

    def new_file(self):
        self.filename = None
        self.text_area.delete(1.0, "end")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("All files", "*.*"),
            ("Text files", "*.txt"), 
            ("Python files", "*.py"),
            ("Batch files", ("*.bat", "*.cmd"))
        ])

        if file_path:
            self.filename = file_path
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, "end")
                self.text_area.insert("end", file.read())

    def save_file(self, event=None):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, "end"))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("Batch files", ("*.bat", "*.cmd"))
        ])

        if file_path:
            self.filename = file_path
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end"))

    def exit_editor(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    def save_file_shortcut(self, event):
        self.save_file()

    def open_website(self):
        webbrowser.open("http://www.example.com")

    def open_discord(self):
        webbrowser.open("http://discord.com")


class CodeEditorV1_1_0:
    def __init__(self, root):
        self.root = root
        self.filename = None
        self.root.title("MarchwCodeEditor")

        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        self.start_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Start", menu=self.start_menu)
        self.start_menu.add_command(label="Start module", command=self.Start_Module)
        self.start_menu.add_command(label="Start module .mar", command=self.Start_Module_mar)
        self.start_menu.entryconfigure("Start module .mar", state="disabled")

        self.help_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Website", command=self.open_website)
        self.help_menu.add_command(label="Discord", command=self.open_discord)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Current version: v1.1.0", command=self.open_version)

        self.root.bind("<Control-s>", self.save_file_shortcut)
        self.root.bind("<Control-o>", self.open_file_shortcut)

        # Podświetlenie znaków
        self.text_area.bind("<KeyRelease>", self.highlight_characters)

    def new_file(self):
        self.filename = None
        self.text_area.delete(1.0, "end")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("Batch files", ("*.bat", "*.cmd")),
            ("Mar files", "*.mar")
        ])

        if file_path:
            self.filename = file_path
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, "end")
                self.text_area.insert("end", file.read())

    def save_file(self, event=None):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, "end"))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
            ("All files", "*.*"),
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("Batch files", ("*.bat", "*.cmd")),
            ("Mar files", "*.mar")
        ])

        if file_path:
            self.filename = file_path
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end"))

    def exit_editor(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    def save_file_shortcut(self, event):
        self.save_file()

    def open_file_shortcut(self, event):
        self.open_file()

    def open_website(self):
        webbrowser.open("http://www.example.com")

    def open_discord(self):
        webbrowser.open("http://discord.com")

    def highlight_characters(self, event):
        characters_to_highlight = ["(", ")", "[", "]", "{", "}", "<", ">", "'", '"']  # Dodaj inne znaki, które chcesz podświetlać

        for char in characters_to_highlight:
            self.highlight_character(char)

    def highlight_characters(self, event):
        # Zbierz informacje o wprowadzonym znaku
        char = event.char
        index = self.text_area.index(tk.INSERT)
    
        charList = str('([{}"<')
        # Sprawdź, czy wprowadzony znak to nawias otwierający
        if char in charList:
            # Pobierz odpowiadający nawias zamykający
            matching_bracket = self.get_matching_bracket(char)
            # Wstaw nawias zamykający po wprowadzonym znaku
            self.text_area.insert(index, matching_bracket)
            # Przesuń kursor do poprzedniej pozycji
            self.text_area.mark_set(tk.INSERT, index)

    def Start_Module(self):
        self.save_file()  # Zapisz plik przed uruchomieniem

        # Uruchomienie skryptu w wierszu poleceń
        try:
            subprocess.run(["python", self.filename], shell=True)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def Start_Module_mar():
        pass


    def get_matching_bracket(self, char):
        if char == "(":
            return ")"
        elif char == "[":
            return "]"
        elif char == "{":
            return "}"
        elif char == "'":
            return "'"
        elif char == '"':
            return '"'
        elif char == "<":
            return ">"
        else:
            return ""

    def open_version(self):
        version_selector = VersionSelector()
        version_selector.mainloop()


def main():
    version_selector = VersionSelector()
    version_selector.mainloop()

if __name__ == "__main__":
    main()
