def stitch_text_files(file_paths, output_file):
    """
    Stitches multiple text files into one.
    
    :param file_paths: List of paths to text files to be merged.
    :param output_file: Path to the output file where merged content will be saved.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read() + '\n')  # Ensure separation between files
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
# Example usage
file_list = ["room2room_data/tasks/R2R/data/Instructions_R2R_test.txt", 
            "room2room_data/tasks/R2R/data/Instructions_R2R_train.txt", 
            "room2room_data/tasks/R2R/data/Instructions_R2R_val_seen.txt",
            "room2room_data/tasks/R2R/data/Instructions_R2R_val_seen.txt",
            "/projectnb/cs598/projects/VLN_MMML/aa_spoc_data/sentences.txt"
            ]

# stitch_text_files(file_list, "merged_output.txt")
stitch_text_files(file_list, "Speciteller_stuff/Domain-Agnostic-Sentence-Specificity-Prediction/dataset/data/vln.txt")
