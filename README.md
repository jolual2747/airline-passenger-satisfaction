# airline-passenger-satisfaction
Applying some ML classification algorithms to predict airline passenger's satisfaction based on collectec data.



You must run these linux commands to download the dataset from kaggle. Make sure you have a folder named '.kaggle' on the same directory and put your kaggle.json API authentication there, because the module kaggle_download.py will change the default path of this file to the mentioned previously.

## Steps to replicate:

```sh
git clone <ssh code>
pip3 install -r requirements.txt -U
sudo apt-get install unzip
python3 kaggle_download.py
```
When you run the kaggle_download.py it will create a folder called 'datasets' where will be located the .csv files.