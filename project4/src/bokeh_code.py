from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.layouts import column
import pandas as pd
import os

# Load the preprocessed data
csvPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/results/monthly_avg_response_time.csv")
monthly_avg_response = pd.read_csv(csvPath)

# Get unique zipcodes for dropdowns
zipcodes = monthly_avg_response['zipcode'].unique().tolist()
zipcodes_str = [str(zipcode) for zipcode in zipcodes]

# Create data sources
source_all = ColumnDataSource(data={})
source_zip1 = ColumnDataSource(data={})
source_zip2 = ColumnDataSource(data={})

# Create initial plot
p = figure(title='Monthly Average Incident Response Time (in hours)', 
           x_axis_label='Month', y_axis_label='Average Response Time (hours)', 
           x_range=(monthly_avg_response['month'].min(), monthly_avg_response['month'].max()))

# Add line plots for all data, zip code 1, and zip code 2
p.line('month', 'response_time', legend_label='All 2020 Data', line_width=2, color='blue', source=source_all)
p.line('month', 'response_time', legend_label='Zipcode 1', line_width=2, color='green', source=source_zip1)
p.line('month', 'response_time', legend_label='Zipcode 2', line_width=2, color='red', source=source_zip2)

# Create dropdowns
zipcode1_select = Select(title="Select Zipcode 1:", value=zipcodes[0], options=zipcodes_str)
zipcode2_select = Select(title="Select Zipcode 2:", value=zipcodes[1], options=zipcodes_str)

# Function to update the plot based on dropdown selections
def update_plot():
    zipcode1 = int(zipcode1_select.value)
    zipcode2 = int(zipcode2_select.value)
    
    # Filter data for the selected zipcodes
    data_all = monthly_avg_response
    data_zip1 = monthly_avg_response[monthly_avg_response['zipcode'] == zipcode1]
    data_zip2 = monthly_avg_response[monthly_avg_response['zipcode'] == zipcode2]
    
    # Update the data sources
    source_all.data = {
        'month': data_all['month'],
        'response_time': data_all['response_time']
    }
    
    source_zip1.data = {
        'month': data_zip1['month'],
        'response_time': data_zip1['response_time']
    }
    
    source_zip2.data = {
        'month': data_zip2['month'],
        'response_time': data_zip2['response_time']
    }

# Call update_plot initially
update_plot()

# Attach the update function to the dropdowns
zipcode1_select.on_change('value', lambda attr, old, new: update_plot())
zipcode2_select.on_change('value', lambda attr, old, new: update_plot())

# Layout the components
layout = column(zipcode1_select, zipcode2_select, p)

# Add layout to current document
curdoc().add_root(layout)
curdoc().title = "NYC Dash"


