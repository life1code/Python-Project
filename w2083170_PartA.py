# Part A: Structured Programming with Text Files
import os
import statistics

def add_entry(entries):
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    researcher = input("Enter researcher name: ")
    data_points = list(map(float, input("Enter data points separated by commas: ").split(',')))
    entries.append((experiment_name, date, researcher, data_points))

def view_entries(entries):
    for entry in entries:
        print(f"Experiment: {entry[0]}, Date: {entry[1]}, Researcher: {entry[2]}, Data Points: {entry[3]}")

def save_entries_to_file(entries, filename):
    with open(filename, 'w') as f:
        for entry in entries:
            f.write(f"{entry[0]},{entry[1]},{entry[2]},{','.join(map(str, entry[3]))}\n")

def load_entries_from_file(filename):
    entries = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                experiment_name = parts[0]
                date = parts[1]
                researcher = parts[2]
                data_points = list(map(float, parts[3:]))
                entries.append((experiment_name, date, researcher, data_points))
    return entries

def analyze_data(entries):
    for entry in entries:
        data_points = entry[3]
        print(f"Experiment: {entry[0]}")
        print(f"Average: {statistics.mean(data_points)}")
        print(f"Standard Deviation: {statistics.stdev(data_points) if len(data_points) > 1 else 'N/A'}")
        print(f"Median: {statistics.median(data_points)}")

def main():
    filename = "research_data.txt"
    entries = load_entries_from_file(filename)
    
    while True:
        print("\nMenu:")
        print("1. Add a research data entry")
        print("2. View all entries")
        print("3. Analyze data")
        print("4. Save entries to file")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            analyze_data(entries)
        elif choice == '4':
            save_entries_to_file(entries, filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
