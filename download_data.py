import os
import json
 
kaggle_credentials = json.load(open('./credentials/kaggle.json'))

os.environ['KAGGLE_USERNAME'] = kaggle_credentials['username']
os.environ['KAGGLE_KEY']      = kaggle_credentials['key']
 
from kaggle.api.kaggle_api_extended import KaggleApi
 
dataset = 'kmader/food41'
path = './dataset'
 
api = KaggleApi()
api.authenticate()
 
api.dataset_download_files(dataset, path, quiet=False)
