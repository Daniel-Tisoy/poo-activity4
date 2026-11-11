import tkinter as tk
from tkinter import filedialog, messagebox
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_settings()
        
        MainContainer(self)

    
    def window_settings(self):
        self.title("File writter")
        self.geometry("300x400")

class MainContainer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True)
        self.config(bg="lightblue")
        
        menubar = tk.Menu(master)
        file = tk.Menu(menubar, tearoff=0)
        file.add_command(label ='Open...', command = self.open_file)
        file.add_command(label ='Save', command = self.save_text)

        menubar.add_cascade(label="file", menu=file)

        master.config(menu = menubar)

        self.text = tk.Text(self)
        self.text.pack(side=tk.TOP, padx=3, pady=3, fill="both")

    def save_text(self):
        try:
            text = self.text.get("1.0", "end-1c")
            path = filedialog.asksaveasfilename(initialfile="no_title.txt", defaultextension=".txt",filetypes=[("Text files", "*.txt"), ("All files", "*.*")], title="save as")

            if path:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(text)
                messagebox.showinfo("Succes", "File saved :)")

        except Exception as e:
            messagebox.showerror("Error", f"couldn't save the file:\n{e}")

    def open_file(self):
        """ only plain text"""
        try:
            path = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title="Open file"
            )

            if path:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                self.text.delete("1.0", "end")
                self.text.insert("1.0", content)
                
                messagebox.showinfo("Success", "File loaded :)")

        except Exception as e:
            messagebox.showerror("Error", f"couldn't open the file:\n{e}")