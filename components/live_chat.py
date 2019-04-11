# -*- coding: utf-8 -*-
import requests
from meya import Component


class LiveChat(Component):

    def start(self):
        # url = 'https://mercedesbenzme.slz.io/api/v1/bot/live-chat'
        # url = 'https://e8cacae9.ngrok.io/api/v1/bot/live-chat' | assuming the same code is hosted here as hosted in https://mercchat.pubcom.one/
        url = 'https://chat.mercedesbenzme.com/api/v1/bot/live-chat'

        data = {
            'first_name': self.db.user.get('first_name'),
            'last_name': self.db.user.get('last_name'),
            'bot_id': self.db.user.bot_id,
            'user_id': self.db.user.user_id,
            'locale': self.db.user.get('locale'),
            'timezone': self.db.user.get('timezone'),
            'gender': self.db.user.get('gender')
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
        response_json = response.json()
        
        if(response_json.has_key('status')):
            status = response_json['status']
            text, ent1 = self.cms.get('other', 'live_chat_'+status)
            message = self.create_message(text=text)
            return self.respond(message=message, action="next")
        
        message = self.create_message(text="Oops... Something went wrong! Please, try again later!")
        return self.respond(message=message, action="next")