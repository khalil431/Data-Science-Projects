# NYC 311 Service Request Dashboard: A Data-Driven Exploration of Complaints Across Zipcodes


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
   wget https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
   ```
3. **Trim down the CSV file:**
   - Use the following command to ensure that start and end dates are in 2020 only:
   ```bash
   grep "^[^,]*,[01][0-9]/[0-9][0-9]/2020.*,[01][0-9]/[0-9][0-9]/2020" nyc_311_limit.csv  > nyc_311_limit.csv
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

