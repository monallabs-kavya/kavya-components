import kavya as kv
from kavya.session_managment.uictx_id_assigner import assign_id
from .color_shade_selector import ColorShadeSelector
from kavya.type_factory.mutable_type_factory import (MutableDiv_StubWrappedTypeGen,
                                                     MutableHC_StubWrappedTypeGen,
                                                     )

from kavya.type_factory.mutable_mixins import (ValueSharerMixin
                                               )

from kavya.type_factory.common_mixins import (TwStyMixin
                                               )


from kavya.htmlcomponents import ui_styles
from kavya.htmlcomponents.html_tag_mixins import (DivMixin,
                                                  ButtonMixin
                                                  )

from py_tailwind_utils import *

class MutableShell_LinearSelectorMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        self.selected_circle = None

def stytags_getter_func(ui_styles = ui_styles):
    # give a border around selector box
    return [boxtopo.bd,
            bd/primary/700,
            bd/2,
            bdr.md,
            pd/x/2,
            pd/y/1,
            bg/primary/500,
            W/fit,
            space/x/1
            ]


LinearSelectorBase = MutableDiv_StubWrappedTypeGen("LinearSelector",
                                                   DivMixin,
                                                   mutableShell_addonMixins = [MutableShell_LinearSelectorMixin],
                                                   
                                                   stytags_getter_func=stytags_getter_func
                                                   )
                               

async def on_circle_click(dbref,
                          msg,
                          wp,
                          request,
                          slider_core=None):
    target_of = wp.session_manager.target_of
    slider = target_of(slider_core.id)

    if slider.selected_circle is not None:
        slider.selected_circle.remove_twsty_tags(
            #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
            #shadow.xl2, boxshadow/red/500
            opacity/25
        )
        pass

    slider.selected_circle = dbref
    slider.selected_circle.add_twsty_tags(
        #bg/white, text/gray/8
        #outlinesty._, outline/blue/9, outline/2
        #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
        #shadow.xl2 , boxshadow/red/500
        opacity/25
    )
    # call the slider div registed function
    slider.app_value = dbref.staticCore.value

    pass

class SafelistMixin:
    svelte_twtags_safelist = [mr/st/8]
    svelte_extra_classes_safelist = ""
    def __init__(self, *args, **kwargs):
        pass
    pass
Circle = assign_id(MutableHC_StubWrappedTypeGen("Circle",
                                                ButtonMixin,
                                                stytags_getter_func=lambda m=ui_styles: m.sty.circle,
                                                staticCore_addonMixins = [SafelistMixin],
                                                mutableShell_addonMixins = [ValueSharerMixin]
                                 )
                   )


def event_prehook(on_event_callback):
    assert on_event_callback is not None
    async def hook(dbref, msg, wp, request, on_event_callback = on_event_callback):
        msg["value"] = dbref.app_value
        return await on_event_callback(dbref, msg, wp, request)

    return hook

class _LinearSelector(LinearSelectorBase):
    svelte_twtags_safelist = [space/x/2, outline / offset / 2, outline / black / 0, outline / 2, outlinesty.double, opacity/25]
    svelte_extra_classes_safelist = ""
    def __init__(self, *args, num_iter=range(1, 5), **kwargs):
        key = kwargs.get("key")
        async def on_click(*args,  slider_core=self, **kwargs):
            return await on_circle_click(*args, slider_core = slider_core, **kwargs)

        with kv.uictx(f"___{key}"):

            childs = [
                Circle(
                    text=f"{i}",
                    value=i,
                    key=f"circle_{i}",
                    # on_click=lambda *args, slider_core=self: on_circle_click(
                    #     *args, slider_core=slider_core
                    # ),
                    on_click = on_click

                )
                for i in num_iter
            ]
        super().__init__(
            *args, **kwargs, childs=childs, event_prehook=event_prehook
        )
LinearSelector = assign_id(_LinearSelector)
