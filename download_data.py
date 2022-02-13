import os
import json
import zipfile
 
kaggle_credentials = json.load(open('./credentials/kaggle.json'))

os.environ['KAGGLE_USERNAME'] = kaggle_credentials['username']
os.environ['KAGGLE_KEY']      = kaggle_credentials['key']
 
from kaggle.api.kaggle_api_extended import KaggleApi
 
dataset = 'kmader/food41'
path = './dataset'
unzipped_dataset_dir_name = '/food'
 
api = KaggleApi()
api.authenticate()

api.dataset_download_files(dataset, path, quiet=False)
 

if not os.path.isdir(path + unzipped_dataset_dir_name):

    print("Extracting ...")

    with zipfile.ZipFile(path + "/food41.zip","r") as zf:
        zf.extractall(path + unzipped_dataset_dir_name)

else :
    print("Found " + unzipped_dataset_dir_name + " folder already extracted")