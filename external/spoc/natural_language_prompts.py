import utils.task_spec_to_instruction as task_utils
import utils.string_utils as string_utils

def read_file_data(file_path, prompts):
    with h5py.File(file_path, 'r') as f:
        for k in f.keys():
            group = f[k]
            decoded = decode_string(group['templated_task_spec'][0])
            prompt = string_utils.get_natural_language_spec("ObjectNavLocalRef", decoded)
            print(prompt)
            stop
            # prompt = construct_prompt(decoded)
            # prompts.append(prompt)
            # print(f'Successfully created prompt {prompt} for {file_path}')
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

# export OBJAVERSE_ANNOTATIONS_DIR=/projectnb/cs598/students/asthar/MultiModal_exploration/external/spoc/objaverse_assets/2023_07_28
# export OBJAVERSE_HOUSES_DIR=/projectnb/cs598/students/asthar/MultiModal_exploration/external/spoc/objaverse_houses/houses_2023_07_28