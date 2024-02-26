#The official Python documentation on python inbuilt-functions (Python Software Foundation, 2023)
#This function was inspired by the Dictionary Tutorial discussed on GeeksforGeeks website (GeeksforGeeks, 2023) 
from doctest import OutputChecker


def load_data_from_file_into_dictionary(filename: str):
    # Initialize an empty dictionary to store data
    data_dictionary = {}
    # Open the file and read lines
    with open(filename, "r") as file:
        current_column = None
        for line in file:
            # Remove leading and trailing whitespaces from the line
            line = line.strip()
            # Check if the line starts with "COLUMN"
            if line.startswith("COLUMN"):
                # Extract the column name
                current_column = line.split(" ")[1]
                data_dictionary[current_column] = []
            elif line == "END":
                # Skip the terminator string
                continue
            else:
                # Add data to the current column in the dictionary
                data_dictionary[current_column].append(line)
    return data_dictionary


#Implementation inspired by the official Python documentation on the csv module (Python Software Foundation, 2023),
#GeeksforGeeks list datatype (GeeksforGeeks, 2023) and Real Python Tutorial on List (Real Python, 2023)
def load_data_from_file_into_list(filename: str):
    # Initialize an empty list to store data
    data_list = []
    # Open the file and read lines
    with open(filename, "r") as file:
        for line in file:
            # Remove leading and trailing whitespaces from the line
            line = line.strip()
            # Check if the line is the terminator string "END"
            if line == "END":
                continue
            else:
                # Add the line to the list
                data_list.append(line)
    return data_list



#implemented based on the guidance provided by TutorialsPoint on dictionary datatype (TutorialsPoint, 2023)
#GeeksforGeeks tutorial on dictionary (GeeksforGeeks, 2023) and w3school dictioanry datatype (w3school, 2023)
def output_data_from_dictionary(data_table: dict):
    print("Displaying data from dictionary" '\n')
    for column_name, data_entries in data_table.items():
        # Display column name with = above and below
        print(f"{'=' * 30}\n{column_name}\n{'=' * 30}")
        # Display data entries
        for entry in data_entries:
            print(f"{entry}")
            
            

#implemented based on the guidance provided by TutorialsPoint on List datatype (TutorialsPoint, 2023)
#GeeksforGeeks tutorial (GeeksforGeeks, 2023) and Real Python tutorial (Real Python, 2023)
def output_data_from_list(data_table: list):
    print(f"Displaying data from list")
    # Initialize a variable to keep track of the current column
    current_column = None
    # Iterate through the items in the list
    for i, item in enumerate(data_table):
        # Check if the item starts with "COLUMN" all uppercase
        if item.startswith("COLUMN"):
            # Extract the column name
            current_column = item.split(" ")[1]
            # Print a line of = above and bellow the column name
            print(f"\n{'=' * 30}\n{current_column}\n{'=' * 30}")
        else:
            # Print each data item below its respective column name
            print(f"{item}\n" if current_column and i + 1 < len(data_table)
                  and not data_table[i + 1].startswith("COLUMN") else f"{item}", end="")



# The function *output_total_mean_median* was inspired and adapted from ChatGPT (OpenAI 2023) and
# W3School tutorial (W3School,2023)
def output_total_mean_median(data_table, total_column_name: str):
    # Initialize variables
    data_type = None
    column_values = None
    # Check if the data_table is a list or dictionary
    if isinstance(data_table, list):
        data_type = "list"
        # Initialize variables for list extraction
        column_values = []
        extracting_values = False
        for item in data_table:
            if isinstance(item, str) and item.startswith('COLUMN'):
                current_column = item.replace('COLUMN', '').strip()
                extracting_values = current_column == total_column_name
            elif extracting_values:
                try:
                    numerical_value = int(item) if str(
                        item).strip().isdigit() else float(item)
                    column_values.append(numerical_value)
                except ValueError:
                    print(
                        f"One or more values in {total_column_name} could not be converted into numerical values")
    elif isinstance(data_table, dict):
        data_type = "dictionary"
        column_values = data_table.get(total_column_name, None)
        if column_values is None:
            print(f"Column: {total_column_name} could not be found")
            return
        if not isinstance(column_values, list):
            column_values = [column_values]
    else:
        print(f"Invalid data type. Please provide a list or a dictionary.")
        return
    # Check if column values were successfully extracted
    if not column_values:
        print(f"Column: {total_column_name} could not be found")
        return
    # Initialize variables for total, mean, and median
    total = 0
    numerical_values = []
    # Calculate total and collect numerical values
    for value in column_values:
        try:
            numerical_value = int(value) if str(
                value).strip().isdigit() else float(value)
            total += numerical_value
            numerical_values.append(numerical_value)
        except ValueError:
            print(
                f"One or more values in {total_column_name} could not be converted into numerical values")
    # Print total, mean, and median
    print(
        f"Displaying total from column {total_column_name} from {data_type}")
    print(f"Total from column {total_column_name} = {total}")
    if numerical_values:
        mean_value = sum(numerical_values) / len(numerical_values)
        print(f"The mean of column {total_column_name} = {mean_value}")
        sorted_values = sorted(numerical_values)
        n = len(sorted_values)
        median_value = (
            (sorted_values[n // 2] + sorted_values[(n - 1) // 2]) / 2
            if n % 2 == 0
            else sorted_values[n // 2]
        )
        print(f"The median of column {total_column_name} = {median_value}")


#TESTING THE OUTPUTS

filename = 'Data.txt'  # Replace with the actual path to your file
loaded_data_dictionary = load_data_from_file_into_dictionary(filename)
loaded_data_list = load_data_from_file_into_list(filename)

print(loaded_data_dictionary)  # Output data from dictionary
print()

output_data_from_dictionary(loaded_data_dictionary )  # Output data from dictionary
print()

print(loaded_data_list )  # Output data from list
print()

output_data_from_list(loaded_data_list)  # Output data from list
print()

# Output total, mean, and median from the column Price in a dictionary
output_total_mean_median(loaded_data_dictionary, "Price")  
print()

 # Output total, mean, and median from the column Price in a list  
output_total_mean_median(loaded_data_list, "Credit") 




# REFERENCES

# OpenAI (2023). 'output_total_mean_median function Code', ChatGPT [Large language model].
# Available at: https://chat.openai.com [Accessed 30 November 2023].

# TutorialsPoint (2023). 'Python - Data Types'.
# Available at: https://www.tutorialspoint.com/python/python_data_types.htm
# [Accessed 28 November 2023].

# Real Python (2023). 'Python Tutorials on List'.
# Available at: https://realpython.com/python-list/ [Accessed 20 November 2023].

# GeeksforGeeks (2023). 'Python Data Type List & Dictionary'.
# Available at: https://www.geeksforgeeks.org/python-programming-language
# [Accessed 26 November 2023].

# W3Schools (2023). 'Python Tutorial'.
# Available at: https://www.w3schools.com/python/ [Accessed: 20 November 2023].

# Python Software Foundation. (2023) 'The Python Standard Library', Python 3.10 Documentation.
# Available at: https://docs.python.org/3/library/index.html 
# (Accessed: 20 November, 2023)

# GeeksforGeeks. (2023) 'How to open a file using the with statement', GeeksforGeeks.
# Available at: https://www.geeksforgeeks.org/how-to-open-a-file-using-the-with-statement/ 
# (Accessed: 20 November, 2023)