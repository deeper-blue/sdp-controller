"""Manages config file. Import this to get access to a python object containing the config"""
import yaml

# not using a with statement here since we need to deal with the file not found case
try:
    f = open('config.yaml', 'r')
    yaml_raw = f.read()
    config = yaml.load(yaml_raw)
except FileNotFoundError:
    # default values
    config = {
        'robot': {
            'ip': '192.168.105.116',
            'port': 64432
        },
        'controller': {
            'id': 'CHANGE_ME',
            'version': '0.0.1'
        }
    }
    print("Config file not found, using default values")
finally:
    f.close()
