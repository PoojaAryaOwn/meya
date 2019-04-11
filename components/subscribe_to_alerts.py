# -*- coding: utf-8 -*-
import requests
from meya import Component


class SubscribeToAlerts(Component):

    def start(self):

        #url = 'https://mercedesbenzme.slz.io/api/v1/bot/subscribe'
        url = 'https://chat.mercedesbenzme.com/api/v1/bot/subscribe'

        data = {
            'fb_user_id': self.db.user.user_id,
            'first_name': self.db.user.get('first_name'),
            'last_name': self.db.user.get('last_name'),
            'locale': self.db.user.get('locale'),
            'timezone': self.db.user.get('timezone'),
            'gender': self.db.user.get('gender'),
            'active': self.db.flow.get('active_subscription')
        }
        headers = {
            'cache-control': 'no-cache',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxODQ3MzgyMDk1IiwibmFtZSI6Ik1CIEFQSSIsImlhdCI6MTUxNjIzOTAyMn0.XdNFMh3GBXP9ytmfRSTPFsSeDkA6jjz61pq-zZaPM9E',
            'accept': 'application/json'
        }
        response = requests.post(
            url=url,
            headers=headers,
            json=data
        )

        if (response.status_code == requests.codes.ok):
            return self.respond(message=None, action="success")

        return self.respond(message=None, action="fails")
        

