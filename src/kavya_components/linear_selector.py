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
                                                  ButtonMixin, VueTypeMixin
                                                  )

from py_tailwind_utils import *

class MutableShell_SteppedSliderMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        self.selected_step = None

# def stytags_getter_func(ui_styles = ui_styles):
#     # give a border around selector box
#     return [boxtopo.bd,
#             bd/primary/700,
#             bd/2,
#             bdr.md,
#             pd/x/2,
#             pd/y/1,
#             bg/primary/500,
#             W/fit,
#             space/x/1
#             ]


SteppedSliderBase = MutableDiv_StubWrappedTypeGen("SteppedSlider",
                                                   DivMixin,
                                                   mutableShell_addonMixins = [MutableShell_SteppedSliderMixin],
                                                   staticCore_addonMixins=[VueTypeMixin],
                                                   stytags_getter_func=lambda m=ui_styles: m.sty.stepped_slider,

                                                   )
                               

async def on_step_click(dbref,
                        msg,
                        wp,
                        request,
                        slider_core=None):
    target_of = wp.session_manager.target_of
    slider = target_of(slider_core.id)

    if slider.selected_step is not None:
        slider.selected_step.remove_twsty_tags(
            #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
            #shadow.xl2, boxshadow/red/500
            opacity/100,
            ring/2,
            ring/primary/900
        )
        slider.selected_step.add_twsty_tags(
            #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
            #shadow.xl2, boxshadow/red/500
            opacity/50
        )        
        pass

    slider.selected_step = dbref
    slider.selected_step.remove_twsty_tags(
            #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
            #shadow.xl2, boxshadow/red/500
            opacity/50
        )
    slider.selected_step.add_twsty_tags(
        #bg/white, text/gray/8
        #outlinesty._, outline/blue/9, outline/2
        #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
        #shadow.xl2 , boxshadow/red/500
        opacity/100,
        ring/2,
        ring/primary/900
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
SliderStep = assign_id(MutableHC_StubWrappedTypeGen("SliderStep",
                                                ButtonMixin,
                                                stytags_getter_func=lambda m=ui_styles: m.sty.slider_step,
                                                staticCore_addonMixins = [SafelistMixin, VueTypeMixin],
                                                mutableShell_addonMixins = [ValueSharerMixin]
                                 )
                   )


def event_prehook(on_event_callback):
    assert on_event_callback is not None
    async def hook(dbref, msg, wp, request, on_event_callback = on_event_callback):
        msg["value"] = dbref.app_value
        return await on_event_callback(dbref, msg, wp, request)

    return hook

class _SteppedSlider(SteppedSliderBase):
    svelte_twtags_safelist = [space/x/2, outline / offset / 2, outline / black / 0, outline / 2, outlinesty.double,
                              opacity/100, opacity/95, opacity/50,
                              opacity/90, ring/2, ring/primary/900]
    svelte_extra_classes_safelist = ""
    def __init__(self, *args, num_iter=range(1, 5), **kwargs):
        key = kwargs.get("key")
        async def on_click(*args,  slider_core=self, **kwargs):
            return await on_step_click(*args, slider_core = slider_core, **kwargs)

        with kv.UICtx(f"___{key}"):

            childs = [
                SliderStep(
                    text=f"{i}",
                    value=i,
                    key=f"step_{i}",
                    # on_click=lambda *args, slider_core=self: on_circle_click(
                    #     *args, slider_core=slider_core
                    # ),
                    on_click = on_click,
                    twsty_tags = [opacity/50]

                )
                for i in num_iter
            ]
        super().__init__(
            *args, **kwargs, childs=childs, event_prehook=event_prehook
        )
SteppedSlider  = assign_id(_SteppedSlider)
