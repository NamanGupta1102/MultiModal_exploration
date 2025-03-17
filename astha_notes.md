## On SCC when encountering pip issues:

1. Create virtual environment
2. Run the following command to download and run the get-pip.py file. This is done to upgrade pip so I can create a cache folder for it
```
curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o get-pip.py
python get-pip.py
```
3. After that, run
```pip config set global.cache-dir ~/.cache/pip```

Then pip should start working normally in the environment

## Installation dependancy issues
This can occur due to older versions of python being used. Make sure you're using at least python 3.9

To change your version, add a module for python3.9.9 when starting the server

## Installing data from students directory
```
python -m scripts.download_training_data --save_dir ../../../../../projects/VLN_MMML/aa_spoc_data --types fifteen --task_types ObjectNavLocalRef ObjectNavDescription
```