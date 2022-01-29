#chain api ( rpc , lcd .. )
import config

class Api :
    cfg = ''
    
    def __init__(self):
        self.cfg = config.Config()

    def getRpcData(self):
        osm = self.cfg.getValue("rpc","osmosis")
        print(osm)
    
    
    
api = Api()
api.getRpcData()    