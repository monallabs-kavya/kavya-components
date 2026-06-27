import kavya as kv

# from ofjustpy.MHC_types import (
#     Label as MLabel,
#     HCCMutable,
#     Button as MButton,
#     HCCStatic,
#     StackH as MStackH,
# )
# import ofjustpy as oj
# from ofjustpy.htmlcomponents_impl import assign_id
# from ofjustpy.SHC_types import PassiveComponents as PC, ActiveComponents as AC
# from py_tailwind_utils import *
# from ofjustpy_engine import HC_Div_type_mixins as TR
# from ofjustpy_engine.HCType import HCType
# from ofjustpy.ui_styles import sty
# from ofjustpy import ui_styles
# from ofjustpy.Div_TF import gen_Div_type

# require for arrow button which is special type of mutable
# the text is mutable; but the twsty-tags remains the same

# from ofjustpy.HC_TF import gen_HC_type
# from ofjustpy.htmlcomponents import MDiv

from kavya.type_factory.mutable_type_factory import MutableDiv_StubWrappedTypeGen
from kavya.htmlcomponents import html_tag_mixins as HTM
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.themes import ui_styles
from py_tailwind_utils import noop, hidden
class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")


MSlotBtn_HCType =    kv.mutablehc_type_gen("button",
                                           #HTM.ButtonMixin,
                                           #lambda m=ui_styles: m.sty.button, 
                                           make_text_mutable=True,
                                           make_twtags_mutable=True,
                                           mutableShellMixins=[ValueMixin]
                                           )


# gen_Div_type(HCType.mutable,
#                                    "Button",
#                                    TR.ButtonMixin,
#                                    mutable_shell_mixins=[TR.HCTextMixin,  ValueMixin], # value, style, and text : all is mutable
#                                    stytags_getter_func=lambda m=ui_styles: m.sty.button,
#                                    )
    


class VarListDiv_MutableShellMixin:
    attr_tracked_keys = []
    domDict_tracked_keys  = [noop/hidden]
    def __init__(self, **kwargs):
        self.hide_all_slots()
        
        pass
    
    def hide_all_slots(self):
        for cs in self.components:
            #shell = target_of(cs)
            shell = cs
            shell.add_twsty_tags(noop / hidden)

    #def update_child_panel(self, showitems, values):            
    def update_child_panel(self, showitems, values):
        for cs, clabel, cvalue in zip(self.components,
                                      showitems,
                                      values
                                      ):
            cs_shell = cs #target_of(cs)
            cs_shell.remove_twsty_tags(noop / hidden)
            cs_shell.text = clabel
            cs_shell.value = cvalue
        pass


from kavya.type_factory.mutable_type_factory import MutableDiv_StubWrappedTypeGen
from kavya.htmlcomponents import html_tag_mixins as HTM


def TF(SlotType = MSlotBtn_HCType,
       ContainerMixin = HTM.DivMixin
       ):

    _StubWrappedStaticCore= MutableDiv_StubWrappedTypeGen("VarListDiv",
                                                ContainerMixin,
                                                stytags_getter_func = lambda m=ui_styles: m.sty.varlistdiv,
                                                mutableShell_addonMixins=[VarListDiv_MutableShellMixin]
                                       )

    


    class _VarListDiv(_StubWrappedStaticCore):
        attr_tracked_keys = []
        domDict_tracked_keys  = [noop/hidden]
        svelte_twtags_safelist  = [noop/hidden]        
        def __init__(self, *args,
                     max_slots = 20,
                     slot_event_handlers = None,
                     **kwargs):

            if slot_event_handlers is None:
                slot_event_handlers = {}

            key = kwargs.get("key")
            with kv.uictx(f"VL_{key}"):
                self.slots = [SlotType(key=f"slot_{i}",
                                       text=str(i),
                                       value=i,


                                       extra_classes="hover:border-s-[3px] hover:border-gray-100 border-s-[3px]  border-s-pink-50/10",
                                       **slot_event_handlers


                                       )
                              for i in range(max_slots)
                              ]
                    
            #menu_box = oj.HCCMutable.Div(classes="mt-6 flex-1 space-y-4 flex flex-col p-2", childs = self.slots)

            # twsty_tags = encode_twstr("mt-6 space-y-4 flex flex-col p-2")
            # twsty_tags = conc_twtags(*kwargs.pop("twsty_tags", []), *twsty_tags)
            
            
            super().__init__(
                             childs = self.slots,
                             **kwargs
                             )
    return assign_id(_VarListDiv)

