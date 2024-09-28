import pandas as pd
import os
from argparse import ArgumentParser

def calculate():

    # Load your data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/nyc_311_limit_2020.csv")
    df = pd.read_csv(data_path, header=None, low_memory=False)

    # Give the zipcode column a name so that we can reference it without using iloc or loc.
    # Using iloc or loc would give a copy of the series back, but we need to modify it in place,
    # so instead we reference it using its name so that it is modified correctly in
    # place to be in integer values later.
    df.rename(columns={df.columns[8]: 'zipcode'}, inplace=True)

    # Even though we removed the records with empty zipcodes, there are still zipcodes
    # that have invalid values, like strings for example, so we drop the NA values.
    df = df.dropna(subset=['zipcode'])

    # Remove decimal points, here it is modified correctly in place because it is referenced using its name
    # instead of using iloc or loc.
    df['zipcode'] = df['zipcode'].astype(int)

    date_format = "%m/%d/%Y %I:%M:%S %p"

    # Calculate time_difference before calculating response_time
    time_difference = pd.to_timedelta(pd.to_datetime(df.iloc[:, 2], format=date_format) - pd.to_datetime(df.iloc[:, 1], format=date_format))

    # Calculate response time in hours
    df['response_time'] = time_difference.dt.total_seconds() / 3600

    # Filter for closed incidents and for the year 2020
    df = df[(df.iloc[:, 2].notnull()) & (pd.to_datetime(df.iloc[:, 1], format=date_format).dt.year == 2020)]

    # Extract month from the created_date
    df['month'] = pd.to_datetime(df.iloc[:, 1], format=date_format).dt.month

    # Group by month and zipcode, calculating average response time
    monthly_avg_response = df.groupby(['month', 'zipcode'])['response_time'].mean().reset_index()
    
    # Save the result to a CSV file
    monthly_avg_response.to_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/results/monthly_avg_response_time.csv"), index=False)

def main():
    parser = ArgumentParser(description = "There are too many incidents in 2020 to be able to load and process quickly (at least quickly enough for the dashboard to update quickly).  The way to solve this is to pre-process the data using this script so that the dashboard is just loading the monthly response-time averages for each zipcode instead of trying to compute the response-time averages when the dashboard updates.")
    args = parser.parse_args()
    calculate()

if __name__ == "__main__":
    main()
