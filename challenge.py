import csv
import pandas as pd

# data to write: list of rows (each row is a list)
data = [
    ['date', 'product', 'cost'],  # header row
    ['2025-08-01', 'Book', '120'],
    ['2025-08-01', 'Pen', '30'],
    ['2025-08-01', 'Notebook', '80'],
    ['2025-08-02', 'Book', '150'],
    ['2025-08-02', 'Pen', '20'],
    ['2025-08-03', 'Notebook', '200'],
    ['2025-08-03', 'Pen', '50']
]

# open a new file in write mode
with open('sales.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# read the CSV file into a DataFrame
df = pd.read_csv('sales.csv')

# convert the 'cost' column to numeric (just in case)
df['cost'] = pd.to_numeric(df['cost'])

# calculate total sales
total_sales = df['cost'].sum()

# calculate average sale amount
average_cost = round(df['cost'].mean(), 1)

# calculate total sales per day
daily_sales = df.groupby('date')['cost'].sum()

# find the date with the highest sales
max_sales_day = daily_sales.idxmax()
max_sales_value = daily_sales.max()

# print the results
print("Total Sales:", total_sales)
print("Average Sale Cost:", average_cost)
print("Day with Highest Sales:", max_sales_day)
print("Sales on that Day:", max_sales_value)
