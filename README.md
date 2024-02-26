# Python Data Loader. 
##Data manipulate in with Dictioanry and List

This Python script provides functions to load data from a file into either a dictionary or a list, and then output the data along with total, mean, and median calculations.

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
loaded_data_dictionary = load_data_from_file_into_dictionary(filename)
loaded_data_list = load_data_from_file_into_list(filename)

print(loaded_data_dictionary)  # Output data from dictionary
print()

output_data_from_dictionary(loaded_data_dictionary)  # Output data from dictionary
print()

print(loaded_data_list)  # Output data from list
print()

output_data_from_list(loaded_data_list)  # Output data from list
print()

# Output total, mean, and median from the column Price in a dictionary
output_total_mean_median(loaded_data_dictionary, "Price")  
print()

# Output total, mean, and median from the column Price in a list  
output_total_mean_median(loaded_data_list, "Price") 
