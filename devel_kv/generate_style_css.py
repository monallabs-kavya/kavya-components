from twtags_safelist import get_twtags_safelist
from svelte_bundler import build_ssr_style_css
target_module = "td_varlengthlist"
#target_module = "td_color_shade_selector"
#target_module = "td_linear_selector"
#target_module = "td_color_selector_using_slider"
#target_module = "td_stackd"
#target_module = "td_paginate"
# target_module = "td_dockar"
# target_module = "td_dockar_2"
#target_module = "td_mouseover_slideshow"
#target_module = "td_hierarchy_navigator_try"
build_ssr_style_css(target_module,
                    output_dir="./static/ssr/",
                    
                    )
