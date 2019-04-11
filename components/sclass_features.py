import requests
from meya import Component
from meya.cards import TextWithButtons, Button


class SCLassFeatures(Component):

    def start(self):
        
        ## Full feature list
        full_ft_list = [ 'Sound', 'Touch', 'Smell', 'Sight' ]
        
        ## Get current feature list from the flow scope
        ft_list = self.db.flow.get('sclass_ft_list')
        
        ## If there is no feature list in the flow scope set it as the full list
        if (ft_list == 'starting'):
            ft_list = full_ft_list
            
        ## Get current feature
        current_ft = self.db.flow.get('sclass_ft')
        print current_ft
        
        ## Get message for the current feature (var current_ft_message = message)
        current_ft_message, entity = self.cms.get("s_class_leaflet", "msg_ft_"+current_ft.lower())
        msg_next_sense, entity = self.cms.get("s_class_leaflet", "msg_next_sense")
        msg_next_step, entity = self.cms.get("s_class_leaflet", "msg_next_step")
        
        ## Remove current feature from the list of flow scope
        ft_list.remove(current_ft)
        
        ## Set new features list to the flow scope
        self.db.flow.set('sclass_ft_list', ft_list)
        
        ## Set buttons
        buttons = []
        for item in ft_list:
            element = Button(
                text=item, 
                action='self',
                data=({'sclass_ft': item})
            )
            buttons.append(element)
            
        ## Add "next step" button if there is less than 2 buttons
        if (len(buttons) < 3):
            next_step_message, entity = self.cms.get("s_class_leaflet", "msg_take_to_next_step")
            buttons.append(Button(text=next_step_message, flow='s_class_leaflet_04'))
            
        print len(buttons)
            
        ## Complete he current message with the right sentence
        if (len(buttons) == 1):
            ft_complete_message = current_ft_message + msg_next_step
        else:
            ft_complete_message = current_ft_message + msg_next_sense
        
        ## Create Card component
        card = TextWithButtons(
            text=ft_complete_message,
            buttons=buttons
        )
        
        ## Create message itself
        message = self.create_message(card=card)
        
        ## Return the respond object
        return self.respond(message=message, action="next")