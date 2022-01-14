from distutils.command.config import config
import os
import configparser
 

class Config:
    config = ''
    config_default_path = ''
    
    def __init__(self, path='/node_bot/app/config.ini'):
        self.config = configparser.ConfigParser()
        self.config_default_path = os.getcwd()+path
        self.config.read(self.config_default_path, encoding='utf-8')
        
    def get(self, section, key):
        return self.config.get(section, key)
    
    def set(self, section, key, value):
        if section not in self.config.sections():
            self.config.add_section(section)
            
        self.config.set(section, key, value)
       
        with open(self.config_default_path, 'w') as configfile:
            self.config.write(configfile)     
       
    
""" 
#test
cfg = Config()
host = cfg.get("database", "host")
host = cfg.set("file", "host", "123")
host = cfg.get("file", "host")
print(host)
 """