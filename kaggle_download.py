import os
os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.getcwd(),'.kaggle') # to change where the kaggle.json file is located
commands= ['kaggle datasets download -d teejmahal20/airline-passenger-satisfaction', \
    'unzip \*.zip -d datasets && rm *.zip']

for command in commands:
    os.system(command)

    