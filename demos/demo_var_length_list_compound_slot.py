from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.MHC_types import StackH
import ofjustpy as oj
from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.SHC_types import PassiveComponents as PC, ActiveComponents as AC
from py_tailwind_utils import *
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine.HCType import HCType
from ofjustpy.ui_styles import sty
from ofjustpy import ui_styles
from ofjustpy.Div_TF import gen_Div_type
from ofjustpy.HC_TF import gen_HC_type
from ofjustpy_components import VarLenghtList_TF

class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")

        
SlotBtn_HCType = assign_id(
    gen_HC_type(
        HCType.mutable,
        "Slot",
        TR.SpanMixin,
        staticCoreMixins=[],
        mutableShellMixins=[TR.TwStyMixin, TR.HCTextMixin, ValueMixin], # value, style, and text : all is mutable
        stytags_getter_func=lambda m=ui_styles: m.sty.button,
    )
)

class CompoundSlot_MutableShellMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        pass
    
    @property
    def text(self):
        return "whatever"

    @text.setter
    def text(self, value):
        mutable_span = self.components[0]
        print (mutable_span)
        mutable_span.text = value



__CompoundSlot = gen_Div_type(HCType.mutable,
                             "Div",
                             TR.DivMixin,
                             mutable_shell_mixins=[CompoundSlot_MutableShellMixin],
                             stytags_getter_func=lambda m=ui_styles: m.sty.stackh,

                             )
#classes="rounded-lg border border-2 border-indigo-500/50 px-4 py-1 text-sm font-medium text-indigo-500 uppercase leading-normal hover:bg-gradient-to-bl hover:from-gray-200 hover:to-gray-200 hover:via-gray-100/50 w-52 overflow-x-auto shadow shadow-indigo-200  hover:shadow-md hover:shadow-indigo-300 focus:bg-gradient-to-bl focus:border-indigo-500/50 focus:border",
                                   
class _CompoundSlot(__CompoundSlot):
    
    def __init__(self, *args, **kwargs):
        key = kwargs.get("key")
        childs = [SlotBtn_HCType(key=f"{key}_text",
                                 text=kwargs.pop("text"),
                                 value = kwargs.pop("value")
                                 ),
                  oj.icons.FontAwesomeIcon(label="faTrashCan")

                  ]
        super().__init__(childs = childs, **kwargs,
                         
                         )
        self.add_twsty_tags(jc.around, boxtopo.bd, bdr.lg, bd/2, bd/indigo/"500/50", pd/x/4, pd/y/1, fz.sm, fw.medium,
                            fc/indigo/500, *hover(bg/gradient/"to/bl",
                                                  #to/gray/200,
                                                  #via/gray/"100/50",
                                                  shadow.lg
                                                  )
                            )

        
CompoundSlot = assign_id(_CompoundSlot)
app = oj.load_app()
VarLenghtList = VarLenghtList_TF(SlotType = CompoundSlot)

def on_slot_clicked(dbref, msg, to_ms):
    pass
varlenghtlist = VarLenghtList(key="varlenghtlist",
                              max_slots = 20,
                              on_slot_clicked = on_slot_clicked
                              )

items =  []

async def on_add_item(dbref, msg, to_ms):
    global items
    items.append(str(len(items)))
    ms = to_ms(varlenghtlist)
    print(ms)
    ms.hide_all_slots()
    ms.update_child_panel(items, items)
    pass

add_item_btn =  oj.AD.Button(key="add_item_btn",
                             text="add new item",
                             on_click = on_add_item,
                             twsty_tags = [H/16, W/32]
                             )

async def on_del_item(dbref, msg, to_ms):
    global items
    
    #items.append(str(len(items)))
    items.pop()
    print (items)
    ms = to_ms(varlenghtlist)
    
    print(ms)
    ms.hide_all_slots()
    ms.update_child_panel(items)
    pass

del_item_btn =  oj.AD.Button(key="del_item_btn",
                             text="del item",
                             on_click = on_del_item,
                             twsty_tags = [H/16, W/32]
                             )
             
wp_endpoint = oj.create_endpoint(key="varlistdiv",
                                    childs = [oj.HCCMutable.StackH(childs = [varlenghtlist,
                                                                             oj.PC.StackV(childs = [add_item_btn, del_item_btn]
                                                                                          )

                                                                                          ],
                                                                   twsty_tags= [W/96]
                                                                   )
                                              ],
                                    title="VarLenghtList"
                                    )

oj.add_jproute("/", wp_endpoint)


