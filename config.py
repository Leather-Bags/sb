from yaml import safe_load
from os.path import isfile

if isfile('config.yml'):
    globals().update(safe_load(open('config.yml')))
else:
    with open('config.yml', 'w+') as f:
        pass
