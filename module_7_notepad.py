import tkinter as tk
import os
from tkinter import filedialog, messagebox

def new_file():
    if confirm_save_changes():
        text_area.delete(1.0, tk.END)
        global current_file
        current_file = None
        window.title("Текстовый редактор - Новый файл")

def open_file():
    if confirm_save_changes():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
            global current_file
            current_file = file_path
            window.title(f"Текстовый редактор - {file_path}")

def save_file():
    global current_file
    if current_file:
        with open(current_file, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        save_file_as()

def save_file_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        current_file = file_path
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        window.title(f"Текстовый редактор - {file_path}")

def exit_editor():
    if confirm_save_changes():
        window.quit()

def confirm_save_changes():
    if text_area.edit_modified():
        response = messagebox.askyesnocancel("Сохранение изменений", "Вы хотите сохранить изменения?")
        if response:  
            save_file()
            return True
        elif response is False:  
            return True
        else: 
            return False
    return True

def show_version():
    messagebox.showinfo("Версия", "Версия приложения: module 7")

def show_developer():
    messagebox.showinfo("Разработчик", "Разработчик: Urban - Student")

window = tk.Tk()
window.title("Текстовый редактор")
window.geometry("600x400")

text_area = tk.Text(window, wrap='word', undo=True)
text_area.pack(expand=1, fill='both')

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Сохранить как...", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_editor)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="Версия приложения", command=show_version)
help_menu.add_command(label="Разработчик", command=show_developer)

current_file = None

window.protocol("WM_DELETE_WINDOW", exit_editor)

window.mainloop()
