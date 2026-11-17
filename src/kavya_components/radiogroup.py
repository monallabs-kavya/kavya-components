
import kavya as kv
from kavya.type_factory.static_type_factory import ActiveDiv_StubWrappedTypeGen
from kavya.htmlcomponents.group_context import set_group, reset_group
from kavya.session_managment.uictx_id_assigner import assign_id
from kavya.htmlcomponents import html_tag_mixins as HTM
from kavya.htmlcomponents import ui_styles
from functools import partial

class DivMixin:
    def __init__(self, *args, **kwargs):
        self.domDict.html_tag = "div"
        self.domDict.class_name = "Div"

        if "value" in kwargs:
            self.domDict["value"] = kwargs.get("value")
            self.htmlRender_attr.append(f'''value="{kwargs.get("value")}"''')
            
        pass


    @property
    def value(self):
        """
        The 'value' attribute of the <data> element specifies the machine-readable value associated with the element.
        """
        return self.domDict.get("value", None)

    @value.setter
    def value(self, val):
        self.htmlRender_attr.remove(f'''value="{self.domDict["value"]}"''')
        self.domDict["value"] = val
        self.htmlRender_attr.append(f'''value="{val}"''')
        

        
_Div = ActiveDiv_StubWrappedTypeGen("Div",
                                      DivMixin,
                                      stytags_getter_func=lambda m=ui_styles: m.sty.div,
                                      addon_mixins=[HTM.VueTypeMixin] 
                                   )
Div = assign_id(_Div)
from kavya.session_managment.uictx_id_assigner import assign_id

def event_prehook(on_event_callback, group_div=None):

    async def hook(dbref, msg, wp, request, on_event_callback = on_event_callback):
        #msg["value"] = dbref.app_value
        #group_div
        # invoke on change on group div
        change_event = group_div.get_event_handler('change')
        # invoke the group_div event with value equal key of the radio button clicked 
        msg["value"] = dbref.key
        return await change_event(group_div, msg, wp, request)
        # no need to call the hook event 
        # print("hook invoked...calling radio_button click")
        # return await on_event_callback(dbref, msg, wp, request)

    return hook

async def on_radio_button_click(dbref, msg, wp, request):

    pass




class  RadioGroup:


    def __init__(self, div_gen = Div, **kwargs):
        """
        div_gen should have value attribute
        """
        self.name = kwargs.pop("name")
        self.group_items = []
        self.childs = []
        self.div = None
        self.div_gen = div_gen
        self.kwargs = kwargs
        # for radioinput/group-items  to call add_component
        self.group_div = self 

        pass 

    # the actual input item that is part of the group 
    def register_item(self, aitem):
        self.group_items.append(aitem)
        pass 

    def add_component(self, child):
        self.childs.append(child)
    def __enter__(self):
        self.token = set_group(self)
        return self 

    def __exit__(self, *args):

 
        for aitem in self.group_items:
            aitem.on('click', on_radio_button_click)
            aitem.prepare_htmlRender()

            pass
        

        self.div  =  self.div_gen(**self.kwargs,
                                  value=5,
                                  childs = self.childs
                                  )

        for aitem in self.group_items:
            aitem.add_prehook(partial(event_prehook, group_div=self.div))


            pass

        
        
        
        # self.div.components = self.childs
        # self.div.add_register_childs()
        
        reset_group(self.token)


        

    

