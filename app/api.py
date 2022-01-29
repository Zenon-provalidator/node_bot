#chain api ( rpc , lcd .. )
import config
import requests
import json

class Api :
    cfg = ''
    
    def __init__(self):
        self.cfg = config.Config()

    def getDataFromUrl(self, url):
        data = requests.get(url)
        return data.text
    
    def getRpcLatestBlockHeight(self, coinName):
        url = self.cfg.getValue('rpc', coinName) + '/status'
        jsonObj = json.loads(self.getDataFromUrl(url))
        return jsonObj['result']['sync_info']['latest_block_height']
    
    def getExternRpcLatestBlockHeight(self, coinName):
        url = self.cfg.getValue('rpc-extern', coinName) + '/status'
        jsonObj = json.loads(self.getDataFromUrl(url))
        return jsonObj['result']['sync_info']['latest_block_height']
        
    
    
    
api = Api()
print(api.getRpcLatestBlockHeight('osmosis'))