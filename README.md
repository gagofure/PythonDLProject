# Python Data Structure (Dictionary and List)

## Introduction

This Python script takes in a file containing data in a specific format(Data.txt) and provides functions to load data from a file into either a dictionary or a list, and then output the data in a formatted way along with total, mean, and median calculations for a specific column in the data(it has be a number column).

## Usage

1. **Load Data from File into Dictionary**: 
    - `load_data_from_file_into_dictionary(filename: str) -> dict`: This function loads data from a file into a dictionary.

2. **Load Data from File into List**:
    - `load_data_from_file_into_list(filename: str) -> list`: This function loads data from a file into a list.

3. **Output Data from Dictionary**:
    - `output_data_from_dictionary(data_table: dict)`: This function outputs data from a dictionary.

4. **Output Data from List**:
    - `output_data_from_list(data_table: list)`: This function outputs data from a list.

5. **Output Total, Mean, and Median**:
    - `output_total_mean_median(data_table, total_column_name: str)`: This function calculates and outputs the total, mean, and median of a specific column in either a dictionary or a list.

## How to Use

1. Replace `'Data.txt'` with the actual path to your data file.
2. Call the appropriate functions to load and output the data as needed.

## Example

```python
filename = 'Data.txt'  # Replace with the actual path to your file
loaded_data_dictionary = load_data_from_file_into_dictionary(filename)  # Load data from file into dictionary
loaded_data_list = load_data_from_file_into_list(filename)  # Load data from file into list

print(loaded_data_dictionary)  # Output data from dictionary

output_data_from_dictionary(loaded_data_dictionary)  # Output data from dictionary

print(loaded_data_list)  # Output data from list

output_data_from_list(loaded_data_list)  # Output data from list

# Output total, mean, and median from the column Price in a dictionary
output_total_mean_median(loaded_data_dictionary, "Price")  

# Output total, mean, and median from the column Price in a list 
output_total_mean_median(loaded_data_list, "Price")
