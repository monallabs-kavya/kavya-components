from .linear_selector import _SteppedSlider
from kavya.session_managment.uictx_id_assigner import assign_id

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

def recolor_selector_items(color_shade_selector_ms):
    print("callback button called ")
    for idx, k in enumerate(color_shade_selector_ms.components):
        k.add_twsty_tags(bg/color_shades[idx]/500)
    pass

class _ColorShadeSelector(_SteppedSlider):
    svelte_twtags_safelist = [bg/option/500 for option in color_shades
                       ]
    _SteppedSlider.svelte_twtags_safelist = [*svelte_twtags_safelist,
                                *_SteppedSlider.svelte_twtags_safelist
                                ]
    def __init__(self, *args, **kwargs):
        super().__init__(num_iter=range(0, 7),
                         post_mutableshell_create_callback = recolor_selector_items,
                         **kwargs
                         )
        
        pass
    pass


ColorShadeSelector = assign_id(_ColorShadeSelector)
