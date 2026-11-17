import macropy.activate
import os
from page_style_editor import target_wp
from twtags_safelist import (get_csr_components, 
                             get_twtags_safelist
                             )
from svelte_bundler import build_ssr_style_css
from svelte_bundler.csr import  build_csr_svelte_bundle


import logging

if os:
    try:
        os.remove("app.log")
    except:
        pass

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"    
logging.basicConfig(filename="app.log", level=logging.ERROR, format=FORMAT)      
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


target_module = "devel_radiogroup_via_ctx"

build_csr_svelte_bundle(target_module,
                        deploy_websocket_manager=True,
                        enable_skui_theme_selector=True,
                        enable_edit_dom  = True, 
                        enable_inbrowser_exec=False)


