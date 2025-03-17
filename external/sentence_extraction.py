"""
Extract the sentences from the outputs of the models, i.e. from the logs.txt file logged by wandb
"""

import os
def extract_goal_sentences(input_file, output_file):
    """
    Extract goal sentences from a table in a file and write them to another file.
    
    Parameters:
    input_file (str): Path to the input file.
    output_file (str): Path to the output file.
    """
    
    # Initialize variables
    start_extracting = False
    extracted_goals = []
    
    try:
        # Open the input file and read its content
        with open(input_file, 'r') as file:
            lines = file.readlines()
        table_borders = 0
        # Extract the goal sentences
        for line in lines:
            if line.startswith('|') and 'goal' in line.lower():
                start_extracting = True  # Start extracting after the header row
                continue
            if start_extracting:
                if line.startswith('|'):
                    # Extract the goal column (assuming it is the first column)
                    columns = line.split('|')
                    goal = columns[1].strip()  # Adjusted to correctly extract the goal column
                    if goal:  # Ensure it's not an empty string
                        print(goal)
                        extracted_goals.append(goal)
                if line.startswith('+----'):
                    table_borders+=1
                if table_borders==2:
                    break   # Stop extracting at the end of the table
                    
        # Write the extracted goals to the output file
        with open(output_file, 'w') as output:
            for goal in extracted_goals:
                output.write(goal + '\n')
                
        print(f"Goal sentences extracted and written to {output_file}")
        
    except FileNotFoundError:
        print(f"File {input_file} not found.")


if __name__=="__main__":
    # folder_path = os.path.join(os.getcwd(),"spoc", "tmp_log", "OnlineEval-revision-chores-small-training_run_id=SigLIP-ViTb-3-double-det-CHORES-S-eval_dataset=-eval_subset=minival-shuffle=True-sampling=sample","03_15_2025_11_33_18_497149")
    # external/spoc/tmp_log/OnlineEval-revision-chores-small-training_run_id=SigLIP-ViTb-3-double-det-CHORES-S-eval_dataset=-eval_subset=minival-shuffle=True-sampling=sample/03_15_2025_11_33_18_497149
    # Example usage
    # external/spoc/tmp_log/OnlineEval-revision-chores-small-training_run_id=SigLIP-ViTb-3-double-det-CHORES-S-eval_dataset=-eval_subset=minival-shuffle=True-sampling=sample/03_15_2025_11_33_18_497149/wandb/3r54SMCv
    # input_file = os.path.join(folder_path, "wand_db", "3r54SMCv","logs.txt")
    input_file = "/projectnb/cs598/students/asthar/MultiModal_exploration/external/spoc/tmp_log/OnlineEval-revision-chores-small-training_run_id=SigLIP-ViTb-3-double-det-CHORES-S-eval_dataset=-eval_subset=minival-shuffle=True-sampling=sample/03_15_2025_11_33_18_497149/wandb/3r54SMCv/logs.txt"
    output_file = 'goal_sentences.txt'
    extract_goal_sentences(input_file, output_file)

