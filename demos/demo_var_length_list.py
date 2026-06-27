import kavya as kv
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from py_tailwind_utils import * 
from kavya_components import VarLenghtList_TF
#from ofjustpy_components.variable_length_list_TF import SlotBtn_DivType

# class SlotBtnWithIcon(SlotBtn_DivType):
#     def __init__(self, **kwargs):
#         print ("HHHHHHHHHHHHHH")
#         super().__init__(childs=[oj.PC.Span(key="X", text="HHHH")],
#                          **kwargs
#                          )
        
#         pass
    
#     pass

# SlotBtnWithIcon_idgen = assign_id(SlotBtnWithIcon)
app = kv.load_app()
#VarLenghtList = VarLenghtList_TF(SlotType = SlotBtnWithIcon_idgen)
VarLenghtList = VarLenghtList_TF()


async def on_slot_clicked(dbref, msg, wp, request):
    pass
varlenghtlist = VarLenghtList(key="varlenghtlist",
                              max_slots = 20,
                              on_slot_clicked = on_slot_clicked
                              )

items =  []

async def on_add_item(dbref, msg, wp, request):
    global items
    items.append(str(len(items)))
    to_ms = wp.session_manager.target_of
    ms = to_ms(varlenghtlist.id)
    ms.hide_all_slots()
    ms.update_child_panel(items, items)
    pass

add_item_btn =  kv.AD.Button(key="add_item_btn",
                             text="add new item",
                             on_click = on_add_item,
                             twsty_tags = [H/16, W/32]
                             )

async def on_del_item(dbref, msg, wp, request):
    global items
    to_ms = wp.session_manager.target_of
    #items.append(str(len(items)))
    items.pop()
    ms = to_ms(varlenghtlist.id)
    ms.hide_all_slots()
    ms.update_child_panel(items, items)
    pass


del_item_btn =  kv.AD.Button(key="del_item_btn",
                             text="del item",
                             on_click = on_del_item,
                             twsty_tags = [H/16, W/32]
                             )

wp_endpoint = kv.create_endpoint(key="varlistdiv",
                                    childs = [kv.HM.StackH(childs = [varlenghtlist,
                                                                     kv.PD.StackV(childs = [add_item_btn, del_item_btn]
                                                                                          )

                                                                                          ],
                                                                   twsty_tags= [W/96]
                                                                   )
                                              ],
                                    title="VarLenghtList",
                                    svelte_bundle_dir = "ssr",
                                    rendering_type="MutableSSR",
                                    )

kv.add_route("/", wp_endpoint)

