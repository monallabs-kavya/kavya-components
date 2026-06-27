from kavya_components import VarLenghtList_TF
import kavya as kv
from py_tailwind_utils import * 
from kavya_components import VarLenghtList_TF

VarLenghtList = VarLenghtList_TF()
app = kv.load_app()
async def on_slot_clicked(dbref, msg, wp, request):
    pass
varlenghtlist = VarLenghtList(key="varlenghtlist",
                              max_slots = 20,
                              on_slot_clicked = on_slot_clicked
                              )

wp_endpoint = kv.create_endpoint(key="varlistdiv",
                                    childs = [kv.HM.StackH(childs = [varlenghtlist,
                                                                     # kv.PD.StackV(childs = [add_item_btn, del_item_btn]
                                                                     #                      )

                                                                                          ],
                                                                   twsty_tags= [W/96]
                                                                   )
                                              ],
                                    title="VarLenghtList",
                                    svelte_bundle_dir = "ssr",
                                    rendering_type="MutableSSR",
                                    )

kv.add_route("/", wp_endpoint)

