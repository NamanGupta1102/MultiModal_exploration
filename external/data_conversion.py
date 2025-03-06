## Imports
import h5py
import numpy as np
import os
import ast

def decode_string(task):
    # Decode the bytes to string
    decoded = np.trim_zeros(task).tobytes().decode('utf-8')
    # print(decoded)
    return decoded

def construct_prompt(data):
    data = ast.literal_eval(data)
    # print('Data: ', type(data))
    target_object = data['synsets'][0].split('.')[0].lower()
    target_object = (' ').join(target_object.split('_'))
    reference_objects = [s.split('.')[0] for s in data['reference_synsets']]
    
    if len(reference_objects) == 1:
        reference_phrase = (' ').join(reference_objects[0].split('_'))
    elif len(reference_objects) == 2:
        reference_phrase = f"{(' ').join(reference_objects[0].split('_'))} and {(' ').join(reference_objects[1].split('_'))}"
    else:
        reference_phrase = ", ".join((' ').join(reference_objects[:-1].split('_'))) + f", and {(' ').join(reference_objects[-1].split('_'))}"
    
    prompt = f"Find the {target_object} {data['reference_type']} the {reference_phrase}."
    return prompt

def read_file_data(file_path, prompts):
    with h5py.File(file_path, 'r') as f:
        for k in f.keys():
            group = f[k]
            decoded = decode_string(group['templated_task_spec'][0])
            prompt = construct_prompt(decoded)
            prompts.append(prompt)
            print(f'Successfully created prompt {prompt} for {file_path}')
    return prompts


if __name__=="__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd())))))
    PATH_TO_DATA = os.path.join(BASE_DIR, 'projects', 'VLN_MMML', 'aa_spoc_data', 'fifteen', 'ObjectNavLocalRef', 'train')
    prompts = []
    # Iterate through immediate subfolders in the train folder
    for subfolder in os.listdir(PATH_TO_DATA):
        subfolder_path = os.path.join(PATH_TO_DATA, subfolder)
        
        # Check if it's a directory
        if os.path.isdir(subfolder_path):
            # Look for HDF5 files in the subfolder
            for file in os.listdir(subfolder_path):
                if file.endswith('.hdf5') or file.endswith('.h5'):
                    file_path = os.path.join(subfolder_path, file)
                    prompts = read_file_data(file_path, prompts)
    # Open the file in write mode and write each sentence
    with open('train_sentences.txt', "w") as file:
        for sentence in prompts:
            file.write(sentence + "\n")

    print(f"Sentences have been saved")
    