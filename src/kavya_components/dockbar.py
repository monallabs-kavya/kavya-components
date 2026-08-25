import kavya as kv

from functools import partial
from kavya.type_factory.mutable_type_factory import (MutableDiv_StubWrappedTypeGen,
                                                     MutableHC_StubWrappedTypeGen,
                                                     )

from kavya.type_factory.mutable_mixins import (ValueSharerMixin
                                               )

from kavya.type_factory.common_mixins import (HCTextMixin,
                                              TwStyMixin
                                               )

from kavya.session_managment.uictx_id_assigner import assign_id
from kavya.htmlcomponents import ui_styles
from kavya.htmlcomponents.html_tag_mixins import (DivMixin,
                                                  ButtonMixin,
                                                  VueTypeMixin
                                                  )

from py_tailwind_utils import *


async def on_undock_click(undock_btn, msg, wp, request,  dockbar=None):
    # undock the target; make it visible
    #dock_shell = target_of(dockbar.wrapped_components[msg.value])
    target_of = wp.session_manager.target_of
    dock_shell = target_of(dockbar.wrapped_components[undock_btn.value].id)
    dock_shell.remove_twsty_tags(noop/hidden)

    # disable the undock_btn
    undock_btn.disabled = True


    pass
on_undock_click.svelte_twtags_safelist = [noop/hidden]
async def on_dock_click(dock_btn, msg, wp, request, dockbar=None):
    target_of = wp.session_manager.target_of
    key = dock_btn.value
    
    #dock_shell = target_of(dockbar.wrapped_components[msg.value])
    dock_shell = target_of(dockbar.wrapped_components[dock_btn.value].id)
    dock_shell.add_twsty_tags(noop/hidden)
    shell_undock_btn = target_of(dockbar.undock_btns[key].id)
    # print("dock it: changes on undock button: ",  type(shell_undock_btn.domDict), " ", type(shell_undock_btn.attrs))

    # print("dock it: changes on undock button: ",  shell_undock_btn.domDict, " ", shell_undock_btn.attrs)
        
    # This expression doesn't invoke the __setitem__ for the onekeyDict:
    # Don't know why 
    shell_undock_btn.disabled = False

    # print("dock it: changes on undock button: ",  shell_undock_btn.domDict, " ", shell_undock_btn.attrs)
    # print("dock it: changes on undock button: ",  [_ for _ in shell_undock_btn.domDict.get_changed_history()], " ",
    #       [_ for _ in shell_undock_btn.attrs.get_changed_history()]
    #       )

    pass
    

class UndockButtonMixin:
    """
    In addition to changes to classes,
    UndockButton has changes to attribute

    """
    attr_tracked_keys = ['disabled']
    domDict_tracked_keys = []
    
    def __init__(self, *args, **kwargs):
        self.attrs.disabled = True

    @property
    def disabled(self):
        return self.attrs.get("disabled", None)

    @disabled.setter
    def disabled(self, value):
        if value is not None:
            self.attrs["disabled"] = value
        elif "value" in self.attrs:
            del self.attrs["value"]



_UndockButton = MutableHC_StubWrappedTypeGen("UndockButton",
                                             ButtonMixin,
                                             staticCoreMixins = [HCTextMixin, VueTypeMixin],
                                             mutableShellMixins = [UndockButtonMixin,
                                                                   TwStyMixin],
                                             mutableShell_addonMixins = [ValueSharerMixin],
                                             stytags_getter_func=lambda m=ui_styles: m.sty.undock_button
                                        )


UndockButton = assign_id(_UndockButton)

class Dockbar:
    def __init__(self,
                 dockable_items,
                 dock_labels,
                 *args,
                 wdiv_type=kv.HS.Div,
                 **kwargs
                 ):
        """
        assuming that the item being docked are static items.
        If they are Mutable then use general mutable Mutable.Div
        for wdiv_type
        """
        undock_btn_sty = kwargs.get(
            "undock_btn_sty",
            [
                shadow.xl,
                bg / primary / 500,
                shadow / success / 200,
                *variant(
                    bg / success / 100,
                    fc / success / 900,
                    bd / slate / 500,
                    shadow.none,
                    rv="disabled",
                ),
            ],
        )

        # components that need to be docked/undocked
        self.wrapped_components = {}
        self.undock_btns = {}
        # partial
        dockit_handler = partial(on_dock_click, dockbar=self)
        dockit_handler.svelte_twtags_safelist =  [noop/hidden]
        undockit_handler = lambda *args, dockbar=self: on_undock_click(
            *args, dockbar=dockbar
        )
        for idx, (di, dock_label) in enumerate(zip(dockable_items, dock_labels)):
            key = str(idx)
            undock_btn = UndockButton(
                key=f"undockbtn_{key}",
                text=dock_label,
                disabled=True,
                value=key,
                twsty_tags=undock_btn_sty,
                on_click=undockit_handler,
            )

            # dock_btn = AC.Button(
            #     key=f"dock_{key}",
            #     text="-",
            #     value=key,
            #     twsty_tags=[bg / pink / 1, W / 6, H / 6, top / 1, right / 1, absolute],
            #     on_click=dockit_handler,
            # )
            with kv.TwStyCtx(kv.themes.unsty):
                dock_btn = kv.AD.Button(key=f"dock_{key}",
                                        twsty_tags=[W/3, H/1, bg/rose/500, top / 1, right / 1, ppos.absolute],
                                        value=key,
                                        on_click=dockit_handler)
                
            wrapped_component = wdiv_type(
                key=f"wrap_{key}", childs=[di, dock_btn], twsty_tags=[ppos.relative]
            )

            self.undock_btns[key] = undock_btn
            self.wrapped_components[key] = wrapped_component



