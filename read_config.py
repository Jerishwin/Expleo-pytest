from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config.read("./config.ini")
    return config[category][key]