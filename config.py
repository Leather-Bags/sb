from os.path import isfile

from yaml import safe_load

if isfile('config.yml'):
    globals().update(safe_load(open('config.yml')))
else:
    with open('config.yml', 'w+') as f:
        pass
