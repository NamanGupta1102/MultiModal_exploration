import re

def compute_average_from_tensor_file(file_path):
    """
    Extracts numerical values from tensor lines in a text file,
    computes the sum and returns the average.
    
    :param file_path: Path to the text file containing tensor values.
    :return: Average of extracted values.
    """
    values = []
    pattern = re.compile(r"tensor\(([-+]?[0-9]*\.?[0-9]+)")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                values.append(float(match.group(1)))
    
    if values:
        return sum(values) / len(values)
    else:
        return None  # Return None if no values are found

# Example usage
file_path = "Speciteller_stuff/Domain-Agnostic-Sentence-Specificity-Prediction/predictions.txt"
average = compute_average_from_tensor_file(file_path)
print(f"Average: {average:.4f}" if average is not None else "No valid tensor values found.")
