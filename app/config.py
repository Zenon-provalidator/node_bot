from distutils.command.config import config
import os
import configparser
 

class Config:
    config = ''
    config_default_path = ''
    
    def __init__(self, path='/app/config.ini'):
        self.config = configparser.ConfigParser()
        self.config_default_path = os.getcwd()+path
        print(self.config_default_path)
        self.config.read(self.config_default_path, encoding='utf-8')
        
    def getValue(self, section, key):
        return self.config.get(section, key)
    
    def setValue(self, section, key, value):
        if section not in self.config.sections():
            self.config.add_section(section)
            
        self.config.set(section, key, value)
       
        with open(self.config_default_path, 'w') as configfile:
            self.config.write(configfile)
    
    def removeKey(self, section, key):
        self.config.remove_option(section, key)
        
        with open(self.config_default_path, 'w') as configfile:
            self.config.write(configfile)
        
    def removeSection(self, section):
        self.config.remove_section(section)
        
        with open(self.config_default_path, 'w') as configfile:
            self.config.write(configfile)
        
       
    
''' 
# test
cfg = Config()
host = cfg.getValue("database", "host")
cfg.setValue("file", "host", "123")
print(host)

cfg.removeSection("database2")
cfg.removeKey("file", "host2")

 '''