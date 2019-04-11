# -*- coding: utf-8 -*-
import requests
from meya import Component


class PauseBot(Component):

    def start(self):
        #url = "https://mercedesbenzme.slz.io/api/v1/bot/pause/"+unicode(self.db.user.user_id)
        url = "https://chat.mercedesbenzme.com/api/v1/bot/pause"+unicode(self.db.user.user_id)
        headers = {
            'cache-control': 'no-cache',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxODQ3MzgyMDk1IiwibmFtZSI6Ik1CIEFQSSIsImlhdCI6MTUxNjIzOTAyMn0.XdNFMh3GBXP9ytmfRSTPFsSeDkA6jjz61pq-zZaPM9E',
            'accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        return self.respond(message=None, action=None)
