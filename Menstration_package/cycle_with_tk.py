import tkinter as tk
from datetime import datetime, timedelta


class MenstrualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menstrual Cycle App")

        self.cycle_start_label = tk.Label(root, text="Cycle Start Date (YYYY-MM-DD):")
        self.cycle_start_label.pack()
        self.cycle_start_entry = tk.Entry(root)
        self.cycle_start_entry.pack()

        self.cycle_length_label = tk.Label(root, text="Cycle Length (in days):")
        self.cycle_length_label.pack()
        self.cycle_length_entry = tk.Entry(root)
        self.cycle_length_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_cycle)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate_cycle(self):
        cycle_start = self.cycle_start_entry.get()
        cycle_length = self.cycle_length_entry.get()

        try:
            cycle_start_date = datetime.strptime(cycle_start, "%Y-%m-%d")
            cycle_length = int(cycle_length)

            period_start = cycle_start_date
            ovulation_date = cycle_start_date + timedelta(days=(cycle_length // 2))
            safe_start = cycle_start_date + timedelta(days=(cycle_length - 18))
            safe_end = cycle_start_date + timedelta(days=(cycle_length - 11))

            result_text = f"Period Start: {period_start.strftime('%Y-%m-%d')}\n"
            result_text += f"Ovulation Date: {ovulation_date.strftime('%Y-%m-%d')}\n"
            result_text += f"Safe Period: {safe_start.strftime('%Y-%m-%d')} to {safe_end.strftime('%Y-%m-%d')}"

            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Invalid input. Please check your date format and cycle length.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MenstrualApp(root)
    root.mainloop()
