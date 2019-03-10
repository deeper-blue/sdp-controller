import requests
import json

class Requester():
    def __init__(self, board_id,board_version):
        self.board_id=board_id
        self.board_version=board_version
        self.registerController()

    def registerController(self):
        URL ='http://negativei2-server.herokuapp.com/controllerregister'
        PARAMS = {'board_version':self.board_version,'board_id':self.board_id}
        r = requests.post(URL,PARAMS)
        return r

    def sendResponse(self,ply_count):
        URL ='http://negativei2-server.herokuapp.com/controllerpoll'
        PARAMS = {'board_id':self.board_id,'ply_count':ply_count}
        r=requests.post(URL,PARAMS)
        return r
