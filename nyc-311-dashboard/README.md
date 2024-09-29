# NYC 311 Service Request Dashboard: A Data-Driven Exploration of Complaints Across Zipcodes
This project provides command-line tools for investigating 311 service requests across New York City's zip codes. It also offers an interactive Bokeh dashboard to analyze the response times across zip codes for the year of 2020. It also offers a jupyter notebook that allows the user to visualize the number of occurrences of the overall most abundant complaint type over the first 2 months (January and February) of 2020, compared to the same complaint type in June and July of 2020. The project emulates a proper folder structure (data, src, scripts, readme), ensuring scripts are well-organized with functions and argparse for flexibility. Please maintain the relative pathways of the folders so that the OS module captures the correct pathways for the required files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation
Step-by-step instructions on how to get the development environment running.

1. **Clone the Repository:**
   - Clone the project repository from GitHub using Visual Studio:
     ```bash
     git clone https://github.com/khalil431/Data-Science-Projects.git
     ```
   - Alternatively, download the repository ZIP file and extract it.

2. **Create a data directory inside nyc-311-dashboard folder:**
   - The CSV file will be installed inside the data folder:
     ```bash
     cd nyc-311-dashboard
     mkdir data
     cd data
     mkdir results
     wget https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
     ```
3. **Trim down the CSV file:**
   - Use the following command to ensure that start and end dates are in 2020 only:
     ```bash
     grep -E "^[^,]*,[01][0-9]/[0-9][0-9]/2020.*,[01][0-9]/[0-9][0-9]/2020" nyc_311_limit.csv  > nyc_311_limit.csv
     ```
   - Use the following command to ensure that the 9th field (which has zip codes) is not empty:
     ```bash
     grep -E "^[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]+,.*$" nyc_311_limit.csv > nyc_311_limit.csv
     ```
   - Use the following command to ensure that the end date is not empty. This is important because the first step does not take care of it (since the first step can match into later fields that contain 2020):
     ```bash
     grep -E "^[^,]*,[^,]*,[^,]+,.*$" nyc_311_limit.csv > nyc_311_limit.csv
     ```
   - Use the following command to ensure that the 17th field (which specifies the borough) is not empty:
     ```bash
     grep -E "^[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]+,.*$" nyc_311_limit.csv > nyc_311_limit.csv
     ```
   
## Usage

1. **Command-Line Tools (scripts):**

   The `borough_complaints.py` script allows users to investigate complaint types across boroughs within a given date range. It saves the output file in the results folder of the data folder. The help commands for these scripts are also available through the --help flag.
   
   - **Usage example:**
      ```bash
      cd scripts
      python borough_complaints.py -i nyc_311_limit.csv -s 2020-01-01 -e 2020-02-28 -o results-jan-feb.csv
      python borough_complaints.py -i nyc_311_limit.csv -s 2020-06-01 -e 2020-07-31 -o results-june-july.csv
      ```
   There are too many incidents in 2020 to be able to load and process quickly (at least quickly enough for the dashboard to update quickly). The way to solve this is to pre-process the data using the `calculate_monthly_averages.py` script so that the dashboard is just loading the monthly response-time averages for each zipcode instead of trying to compute the response-time averages when the dashboard updates.

   - **Usage example:**
     ```bash
      cd scripts
      python calculate_monthly_averages.py
      ```

2. **Bokeh Dashboard:**
   
   The goal of the dashboard is to allow a city official to evaluate the difference in response time to complaints filed through the 311 service by zipcode. Response time is measured as the amount of time    from incident creation to incident closed. It contains two dropdown boxes which can be used to select two different zip codes. The data for the two zipcodes are then plotted on two separate lines and compared to a third line displaying the data for all of 2020. To display the bokeh dashboard, the `calculate_monthly_averages.py` script in the scripts folder needs to be run first. The instructions can be found above.

   - **Usage example:**
     ```bash
     cd src
     bokeh serve bokeh_code.py --port 8080
     ```
     
   The link given by the command line should then be copied into a web browser.

3. **Jupyter notebook:**

   The jupyter notebook allows the user to visualize the number of occurrences of the overall most abundant complaint type over the first 2 months (January and February) of 2020, compared to June and July of 2020. The data is plotted on a bar chart. Before running this step, the `borough_complaints.py` script needs to be run first for two times (one time for January and February, and another time for June and July) to capture the complaint types across boroughs. The instructions can be found in the "command-line tools" section above.

   - **Usage example:**
     ```bash
     cd src
     jupyter notebook
     ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

