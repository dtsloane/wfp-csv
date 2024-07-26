import csv
import sys
from collections import defaultdict

def differentiate_names(input_file, output_file, column_index):
    name_count = defaultdict(int)
    
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write the header
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            if len(row) > column_index:
                name = row[column_index]
                if name:
                    name_count[name] += 1
                    if name_count[name] > 1:
                        row[column_index] = f"{name} ({name_count[name] - 1})"
            writer.writerow(row)

    print(f"Processed file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file> <output_file> <column_index>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    column_index = int(sys.argv[3]) - 1  # Convert to 0-based index
    
    differentiate_names(input_file, output_file, column_index)