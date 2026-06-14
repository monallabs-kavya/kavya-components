from functools import partial
import kavya as kv
 
from kavya.type_factory.mutable_type_factory import (MutableDiv_StubWrappedTypeGen,
                                                     MutableHC_StubWrappedTypeGen,
                                                     )
from kavya.htmlcomponents.html_tag_mixins import (DivMixin,
                                                  ButtonMixin
                                                  )
from kavya.session_managment.uictx_id_assigner import assign_id
from .color_shade_selector_using_linear_selector import ColorShadeSelector
from .linear_selector import LinearSelector

from py_tailwind_utils.skui_tags import (primary,
                                         secondary,
                                         tertiary,
                                         success,
                                         warning,
                                         surface,
                                         error
                                         
                                         )
from py_tailwind_utils import *
color_shades = [primary,
                 secondary,
                 tertiary,
                 success,
                 warning,
                 surface,
                 error
                 
                 ]

color_gradient = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]


class MutableShell_CSMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []

    def __init__(self, *args, **kwargs):
        self.mcs_value = None
        self.scs_value = None
        self.cs_value = None
        # at begining neither mcs, or scs are clicked
        self.component_clicked = None
        pass

    def update_slider(self, colortag_idx):
        """
        scs: the shade selector
        """

        # ColorSelector has 2 components
        # 1: mcs
        # 2: scs
        colortag = color_shades[colortag_idx]
        scs = self.components[1]

        for shade_btn in scs.components:
            shid = int(shade_btn.value)
            new_color = bg / colortag /             color_gradient[shid]
            shade_btn.add_twsty_tags(new_color)

            
def stytags_getter_func():
    return []

                              
async def on_mcs_change(dbref, msg, wp, request, cs_core=None):
    """
    the select drop down
    """
    target_of = wp.session_manager.target_of
    cs_shell = target_of(cs_core.id)
    cs_shell.mcs_value = msg["value"]
    cs_shell.component_clicked = "mcs"
    
    pass


async def on_scs_click(dbref, msg, wp, request,  cs_core=None):
    """
    state update when shade is choosen in the selector
    """
    target_of = wp.session_manager.target_of
    cs_shell = target_of(cs_core.id)
    cs_shell.scs_value = int(msg["value"])

    cs_shell.component_clicked = "scs"
    pass


def CS_event_prehook(on_event_callback):
    async def hook(cs_shell, msg, wp, request):

        if cs_shell.component_clicked == "mcs":
            cs_shell.update_slider(cs_shell.mcs_value)

        if cs_shell.component_clicked == "scs":
            cs_shell.cs_value = twcc2hex[cs_shell.mcs_value][
                onetonine[cs_shell.scs_value]
            ]
        msg["value"] = cs_shell.cs_value
        # call the user registered event handler
        return await on_event_callback(cs_shell, msg, wp, request)

    return hook

ColorSelectorBase = MutableDiv_StubWrappedTypeGen("ColorSelectorBase",
                                                  DivMixin,
                                                  mutableShell_addonMixins = [MutableShell_CSMixin],
                                                  stytags_getter_func=stytags_getter_func
                                                  )

class _ColorSelector(ColorSelectorBase):
    svelte_twtags_safelist = [bg/cn/shid  for cn in color_shades for shid in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]]

    svelte_extra_classes_safelist = ""
    def __init__(self, *args, **kwargs):
        # there are two childs
        # one main-color-selector (which is select hc)
        # and other shades-color-selector (which is slider)

        key = kwargs.get("key")
        with kv.uictx(f"___{key}"):
            self.mcs = ColorShadeSelector(
                key="mcs",
                on_click = partial(on_mcs_change, cs_core=self)

                # lambda *args, cs_core=self: on_mcs_change(
                #     *args, cs_core=cs_core
                # )                    
            )

            self.scs = LinearSelector(key="scs",
                                      num_iter=range(1, 11),
                                      on_click=partial(on_scs_click, cs_core=self)
                                      )

        childs = [self.mcs, self.scs]

        super().__init__(
            *args, **kwargs, childs=childs,
            event_prehook=CS_event_prehook
        )

ColorSelector = assign_id(_ColorSelector)
