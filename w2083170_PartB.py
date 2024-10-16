# Part B: Object-Oriented Programming with Text Files
import os
import statistics

class ResearchDataManager:
    def __init__(self):
        self.entries = []
        self.filename = "research_data.txt"
    
    def add_entry(self):
        experiment_name = input("Enter experiment name: ")
        date = input("Enter date (YYYY-MM-DD): ")
        researcher = input("Enter researcher name: ")
        data_points = list(map(float, input("Enter data points separated by commas: ").split(',')))
        self.entries.append((experiment_name, date, researcher, data_points))
    
    def view_entries(self):
        for entry in self.entries:
            print(f"Experiment: {entry[0]}, Date: {entry[1]}, Researcher: {entry[2]}, Data Points: {entry[3]}")
    
    def save_entries_to_file(self):
        with open(self.filename, 'w') as f:
            for entry in self.entries:
                f.write(f"{entry[0]},{entry[1]},{entry[2]},{','.join(map(str, entry[3]))}\n")
    
    def load_entries_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.entries = []
                for line in f:
                    parts = line.strip().split(',')
                    experiment_name = parts[0]
                    date = parts[1]
                    researcher = parts[2]
                    data_points = list(map(float, parts[3:]))
                    self.entries.append((experiment_name, date, researcher, data_points))
    
    def analyze_data(self):
        for entry in self.entries:
            data_points = entry[3]
            print(f"Experiment: {entry[0]}")
            print(f"Average: {statistics.mean(data_points)}")
            print(f"Standard Deviation: {statistics.stdev(data_points) if len(data_points) > 1 else 'N/A'}")
            print(f"Median: {statistics.median(data_points)}")

def main():
    manager = ResearchDataManager()
    manager.load_entries_from_file()
    
    while True:
        print("\nMenu:")
        print("1. Add a research data entry")
        print("2. View all entries")
        print("3. Analyze data")
        print("4. Save entries to file")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            manager.add_entry()
        elif choice == '2':
            manager.view_entries()
        elif choice == '3':
            manager.analyze_data()
        elif choice == '4':
            manager.save_entries_to_file()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
