from kavya_components import ColorSelector

import kavya as kv

from py_tailwind_utils import *

async def on_click(*args, **kwargs):
    print("event handler for color select event ")
    pass
color_selector = ColorSelector(key="color_selector", on_click = on_click)

app = kv.load_app()

wp_endpoint = kv.create_endpoint(key="mutableDiv_SSRPage",
                                 childs = [color_selector
                                           #
                                           #       tb_1,
                                           #       tb_2
                                           
                                           ],
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 svelte_bundle_dir = "ssr"
                                 )
kv.add_route("/", wp_endpoint)

