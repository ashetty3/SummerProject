import sys
import csv
import numpy as np

def load_error_mapping(file_path):
    error_mapping = {}
    with open(file_path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            error_mapping[row['error_message']] = {
                "explanation": row['explanation'],
                "solution": row['solution']
            }
    return error_mapping

def error_msg_details(error, error_detail: sys, error_mapping):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    base_message = f"Error occurred in file: {file_name}, line: {line_number}, error message: {str(error)}"
    
    error_type = str(error).split(":")[0] + ": " + str(error).split(":")[1].strip()
    if error_type in error_mapping:
        explanation = error_mapping[error_type]["explanation"]
        solution = error_mapping[error_type]["solution"]
    else:
        explanation = "An unexpected error occurred."
        solution = "Check the error message and traceback for more details."

    detailed_message = f"{base_message}\nExplanation: {explanation}\nSuggested Solution: {solution}"
    return detailed_message

def handle_common_errors(error, error_detail: sys, error_mapping):
    error_message = error_msg_details(error, error_detail, error_mapping)
    return error_message

# Load error mapping from CSV
error_mapping = load_error_mapping('c:/Users/Apoorva Shetty/Documents/GitHub/SummerProject/src/error_mapping.csv')

# Example usage
def test_error_handling():
    A = np.random.rand(2, 3)
    B = np.random.rand(4, 2)

    try:
        result = np.dot(A, B)
    except ValueError as e:
        error_message = handle_common_errors(e, sys, error_mapping)
        print(f"ValueError: {error_message}")

#test_error_handling()
