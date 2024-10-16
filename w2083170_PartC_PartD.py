import os
import tkinter as tk
from tkinter import messagebox
import statistics

class ResearchDataManager:
    def __init__(self):
        self.entries = []
        self.filename = "research_data.txt"

    def add_entry(self, experiment_name, date, researcher, data_points):
        entry = {
            "experiment_name": experiment_name,
            "date": date,
            "researcher": researcher,
            "data_points": data_points
        }
        self.entries.append(entry)

    def save_entries_to_file(self):
        with open(self.filename, 'w') as file:
            for entry in self.entries:
                data_points_str = ",".join(map(str, entry["data_points"]))
                file.write(f"{entry['experiment_name']},{entry['date']},{entry['researcher']},{data_points_str}\n")

    def load_entries_from_file(self):
        if not os.path.exists(self.filename):
            return
        self.entries = []
        with open(self.filename, 'r') as file:
            for line in file:
                parts = line.strip().split(",")
                experiment_name, date, researcher = parts[:3]
                try:
                    data_points = list(map(float, parts[3:]))
                except ValueError:
                    continue  # Skip lines with invalid data points
                entry = {
                    "experiment_name": experiment_name,
                    "date": date,
                    "researcher": researcher,
                    "data_points": data_points
                }
                self.entries.append(entry)

    def analysis_data(self):
        if not self.entries:
            return []
        analysis_results = []
        for entry in self.entries:
            data_points = entry["data_points"]
            average = statistics.mean(data_points)
            if len(data_points) > 1:
                standard_deviation = statistics.stdev(data_points)
            else:
                standard_deviation = 0
            median = statistics.median(data_points)
            analysis_results.append({
                "experiment": entry["experiment_name"],
                "average": average,
                "standard_deviation": standard_deviation,
                "median": median
            })
        return analysis_results

class ResearchDataGUI:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.root.title("Research Data Manager")

        self.experiment_label = tk.Label(root, text="Experiment Name:")
        self.experiment_label.grid(row=0, column=0)
        self.experiment_entry = tk.Entry(root)
        self.experiment_entry.grid(row=0, column=1)

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1)

        self.researcher_label = tk.Label(root, text="Researcher Name:")
        self.researcher_label.grid(row=2, column=0)
        self.researcher_entry = tk.Entry(root)
        self.researcher_entry.grid(row=2, column=1)

        self.data_point_label = tk.Label(root, text="Data Points (comma-separated):")
        self.data_point_label.grid(row=3, column=0)
        self.data_point_entry = tk.Entry(root)
        self.data_point_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Entries", command=self.view_entries)
        self.view_button.grid(row=5, column=0, columnspan=2)

        self.analysis_button = tk.Button(root, text="Analyze Data", command=self.analysis_data)
        self.analysis_button.grid(row=6, column=0, columnspan=2)

        self.save_button = tk.Button(root, text="Save Entries", command=self.save_entries)
        self.save_button.grid(row=7, column=0, columnspan=2)

    def add_entry(self):
        experiment = self.experiment_entry.get()
        date = self.date_entry.get()
        researcher = self.researcher_entry.get()
        try:
            data_points = [float(point.strip()) for point in self.data_point_entry.get().split(",")]
        except ValueError:
            messagebox.showerror("Error", "Invalid data points. Please enter numeric values.")
            return
        self.manager.add_entry(experiment, date, researcher, data_points)
        messagebox.showinfo("Info", "Entry added successfully!")

    def view_entries(self):
        entries = self.manager.entries
        if not entries:
            messagebox.showinfo("Info", "No entries to display.")
            return
        view_window = tk.Toplevel(self.root)
        view_window.title("View Entries")
        text = tk.Text(view_window)
        text.pack(expand=True, fill=tk.BOTH)
        for idx, entry in enumerate(entries, start=1):
            text.insert(tk.END, f"Entry {idx}:\n")
            text.insert(tk.END, f"  Experiment Name: {entry['experiment_name']}\n")
            text.insert(tk.END, f"  Date: {entry['date']}\n")
            text.insert(tk.END, f"  Researcher: {entry['researcher']}\n")
            text.insert(tk.END, f"  Data Points: {entry['data_points']}\n\n")

    def analysis_data(self):
        results = self.manager.analysis_data()
        if not results:
            messagebox.showinfo("Info", "No data available for analysis.")
            return
        analyze_window = tk.Toplevel(self.root)
        analyze_window.title("Analyze Data")
        text = tk.Text(analyze_window)
        text.pack(expand=True, fill=tk.BOTH)
        for result in results:
            text.insert(tk.END, f"Experiment: {result['experiment']}\n")
            text.insert(tk.END, f"  Average: {result['average']:.2f}\n")
            text.insert(tk.END, f"  Standard Deviation: {result['standard_deviation']:.2f}\n")
            text.insert(tk.END, f"  Median: {result['median']:.2f}\n\n")

    def save_entries(self):
        self.manager.save_entries_to_file()
        messagebox.showinfo("Info", "Entries saved successfully!")

def main():
    manager = ResearchDataManager()
    manager.load_entries_from_file()
    root = tk.Tk()
    gui = ResearchDataGUI(root, manager)
    root.mainloop()

if __name__ == "__main__":
    main()
