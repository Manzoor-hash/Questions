import csv

def calculate_stats(data, column_index):
    column_data = [float(row[column_index]) for row in data]
    if column_data:
        average = sum(column_data) / len(column_data)
        maximum = max(column_data)
        minimum = min(column_data)
        return average, maximum, minimum
    else:
        return None, None, None

def main():
    csv_filename = input("Enter the CSV file name: ")
    column_index = int(input("Enter the column index (0-based) to calculate stats for: "))

    try:
        with open(csv_filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

            if column_index < 0 or column_index >= len(data[0]):
                print("Invalid column index.")
            else:
                average, maximum, minimum = calculate_stats(data[1:], column_index)
                if average is not None:
                    print("Average:", average)
                    print("Maximum:", maximum)
                    print("Minimum:", minimum)
                else:
                    print("No data found in the specified column.")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()