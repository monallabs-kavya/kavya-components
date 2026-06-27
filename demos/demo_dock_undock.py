"""
drop down color not working in firefox
"""

from py_tailwind_utils import *
import kavya as kv
from addict_tracking_changes import Dict
import kavya_components as kvx
from py_tailwind_utils import space, y
import macropy.activate
import dummy_company_section_domain_components 
app = kv.load_app()
def on_btn_click(dbref,msg):
    pass

grid_usp, undock_btns_bar,  info_box_container = dummy_company_section_domain_components.GridUSP()

info_boxes = dummy_company_section_domain_components.info_cards()

#undock_btns_bar = dummy_company_section_domain_components.undock_btns_bar()

# span1  = oj.AC.Textarea(key="targetSpan1",
#                         text="a text area with lots of lots of text",
#                         pcp=[bg/green/1, pd/2]
#                      )
# span2  = oj.AC.Textarea(key="targetSpan2",
#                        text="another text area with lots of lots of text",
#                        pcp=[bg/blue/1, pd/2]
#                        )

            
# dockbar  = Dockbar([span1, span2, *info_boxes],
#                    ["Item1", "Item2", "Item3", "Item4" ],
#                    )
dockbar = kvx.Dockbar(info_boxes,
                   [
                      "Technology Solutions",
                      "Financial Services",
                      "Healthcare Innovations",
                      "Green Energy Solutions",
                      "Retail and Consumer Goods",
                      "Transportation and Logistics",
                      "Real Estate Development",
                      "Digital Marketing",
                      "Education and Training",
                      "Entertainment and Media",
                      "Food and Beverage"
                  ]

                  )

# undock_btn_panel = oj.Halign(oj.HCCMutable.Div(key = "undock_btn_panel",
#                                      childs = dockbar.undock_btns.values(),
#                                      twsty_tags=[space/x/4]
#                                                ),
#                              content_type="mutable"
#                              )

info_box_container.childs.extend(dockbar.wrapped_components.values())

undock_btns_bar.childs.extend(dockbar.undock_btns.values())

# wrapped_item_panel = oj.Halign(oj.HCCMutable.Div(
#                                        childs = dockbar.wrapped_components.values(),
#                                        twsty_tags=[space/y/4]
#                                        ),
#                                content_type="mutable"
#                                )




# dock_undock_tlc = oj.Mutable.Div(key="dock_undock",
#                                        childs = [undock_btn_panel,
#                                                  wrapped_item_panel
#                                                  ],
#                                        twsty_tags=[space/y/4]
#                                        )

# dock_undock_container = oj.Mutable.Container(key="dock_undock_container",
#                                              childs = [dock_undock_tlc]
#                                              )



wp_endpoint = kv.create_endpoint(key="dock_undock",
                                    childs = [
                                              grid_usp
                                              ],
                                    title="Docking/Undocking",
                                    rendering_type="MutableSSR",
                                    svelte_bundle_dir="ssr"
                                    )

kv.add_route("/", wp_endpoint)



