from argparse import ArgumentParser
from datetime import datetime
import csv

def process_complaints(input_file, start_date, end_date):
    complaints_count = {}

    # Convert start and end dates from strings to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    with open(input_file, mode='r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            date_str = row[2].split(' ')[0]
            complaint_type = row[5]  
            borough = row[16] 
            
            # Convert date string to datetime object
            row_date = datetime.strptime(date_str, "%m/%d/%Y")
            
            # Check if the date is within the specified range
            if start_date <= row_date <= end_date:
                # Create a unique key for each (complaint_type, borough)
                key = (complaint_type, borough)
                if key in complaints_count:
                    complaints_count[key] += 1
                else:
                    complaints_count[key] = 1

    return complaints_count

def main():
    parser = ArgumentParser(description = "This script processes NYC 311 data to provide the number of each complaint type per borough for a given (creation) date range. The results are output in a CSV file.")
    parser.add_argument("-i", help = "This is the input file to be processed.", required=True)
    parser.add_argument("-s", help = "This is the start date.", required=True)
    parser.add_argument("-e", help = "This is the end date.", required=True)
    parser.add_argument("-o", help = "This is the name of the output file.")

    args = parser.parse_args()
    complaints_count = process_complaints(args.i, args.s, args.e)

    output = "complaint type,borough,count\n"
    for (complaint_type, borough), count in complaints_count.items():
        output += f"{complaint_type},{borough},{count}\n"

    # Print to stdout or write to output file
    if args.o:
        with open(args.o, mode='w') as outfile:
            outfile.write(output)
    else:
        print(output)

if __name__ == "__main__":
    main()