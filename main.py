# main.py
from ears_module import cat_ears, alien_ears
from data_handler import retrieve_data, store_data
from exception_handler import handle_exception
import tkinter as tk
from tkinter import ttk


class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ears Calculator")

        # Create input labels and entry widgets
        self.label_cats = ttk.Label(self, text="Enter the number of cats:")
        self.entry_cats = ttk.Entry(self)

        self.label_aliens = ttk.Label(self, text="Enter the number of aliens:")
        self.entry_aliens = ttk.Entry(self)

        # Create calculate button
        self.calculate_button = ttk.Button(self, text="Calculate", command=self.calculate_ears)

        # Create result label
        self.result_label = ttk.Label(self, text="Result: ")

        # Grid layout
        self.label_cats.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_cats.grid(row=0, column=1, padx=5, pady=5)

        self.label_aliens.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_aliens.grid(row=1, column=1, padx=5, pady=5)

        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label.grid(row=3, column=0, columnspan=2)

    def calculate_ears(self):
        try:
            num_cats = int(self.entry_cats.get())
            num_aliens = int(self.entry_aliens.get())

            result_cat_ears = cat_ears(num_cats)
            result_alien_ears = alien_ears(num_aliens)

            result_str = (
                f"Total cat ears: {result_cat_ears}\n"
                f"Total alien ears: {result_alien_ears}"
            )

            # Display the result in the GUI
            self.result_label.config(text=result_str)

            # Store the result in a file
            store_data(result_str)

        except ValueError:
            error_message = "Invalid input. Please enter valid numbers."
            handle_exception(error_message)


if __name__ == "__main__":
    app = MyGUI()
    app.mainloop()
