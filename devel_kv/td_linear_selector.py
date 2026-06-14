from kavya_components import LinearSelector

async def on_click(*args):
    print("on_click executed with args = ", args)
    pass

linear_selector = LinearSelector(key="linear_selector",
                                 num_iter=range(0,8),
                                 on_click = on_click
                                 )

from py_tailwind_utils import *

import kavya as kv
from addict import Dict



app = kv.load_app()

wp_endpoint = kv.create_endpoint(key="mutableDiv_SSRPage",
                                 childs = [linear_selector
                                           # hello_btn,
                                           #       tb_1,
                                           #       tb_2
                                           
                                           ],
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 svelte_bundle_dir = "ssr"
                                 )
kv.add_route("/", wp_endpoint)
