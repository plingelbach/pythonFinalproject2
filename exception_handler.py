# exception_handler.py
import tkinter as tk
from tkinter import messagebox


def handle_exception(error_message: str) -> None:
    """Handle exceptions and display an error message in the GUI."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messagebox.showerror("Error", error_message)

    root.destroy()
