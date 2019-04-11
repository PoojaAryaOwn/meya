# -*- coding: utf-8 -*-
from meya import Component

class KeywordsFilter(Component):

    def start(self):
        
        keywords_exit = [
            'Ok', 
            'Okeh',
            'Okey',
            'Okie',
            'Okay!',
            'Okay',
            'Oki',
            'Thanks',
            'Thank you',
            'Thx',
            'Thank',
            'ماشي',
            'شكرا',
            'شكراً,'
            'شكرن',
            'اوك',
            'مشكور',
            'لا شكرا',
            'اوكي',
            'يس'
        ]
        
        keywords_no_action = [
            'Emojis',
            'No thanks',
            'Stop',
            'Oui',
            'Ill think about it',
            'Mercedes', 
            'Marcedes',
            "I don't know",
            'I dont know',
            'Lol',
            'سوف افكر في ذلك',
            'مرسيدس',
            'لا اعرف',
            'لا أعرف',
            'مش عايز', 
            'لا شكرا'
        ]
        
        keywords_start = [
            'Hii',
            'Hello',
            'مرحبا'
        ]
        
        if self.db.flow.get('value') in keywords_exit:
            action = "exit"
        elif self.db.flow.get('value') in keywords_no_action:
            action = "no_action"
        elif self.db.flow.get('value') in keywords_start:
            action = "start"
        else:
            action = "not_found"
            
        return self.respond(action=action)
        
