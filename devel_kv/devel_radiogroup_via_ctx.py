import kavya as kv

import kavya_components as kvx

from py_tailwind_utils import *

app = kv.load_app()

async def post_init_page_load(wp, session_manager=None):

    print("post init called with form_data initialized")
    assert session_manager is not None
    session_manager.state.form_data = {}
    session_manager.state.form_data["/aform"] = {}
    print("initialized form_data on session_manager.state ", id(session_manager))
    pass


async def radio_group_click(dbref, msg, wp, request):
    pass 
with kvx.RadioGroup(name="sizing_facet", key="sizing_facet_radio_group",
                    twsty_tags=[bg/primary/500, db.f, flxdir.row, space/x/4],
                    on_change = radio_group_click
                    ) as sizing_facet_radio_group:
    size_option = kv.PD.Label(twsty_tags = [db.f, ai.center, space/x/2],
                              childs = [kv.AC.RadioInput(key="size_option",
                                                         checked = False,
                                                         value=noop/size,
                                                         
                                                         ),
                                        kv.PC.P(text="size")
                                        
                                        ],
                              a = sizing_facet_radio_group
                              )

    width_option = kv.PD.Label(twsty_tags = [db.f, ai.center, space/x/2],
                              childs = [kv.AC.RadioInput(key="width_option",
                                                         checked = False,
                                                         value=noop/W,
                                                         
                                                         ),
                                        kv.PC.P(text="width")
                                        
                                        ],
                              a = sizing_facet_radio_group
                              )

    
    pass 


#print("".join(sizing_facet_radio_group.div.to_html_iter()))
async def on_submit_click(dbref, msg, wp, request):
    # put of global variable for test to pick it up
    print("on submit click called: ", dbref.id)
    print(dbref.get_comp_value(request, "/sizing_facet_radio_group"))
    
    pass

submit_btn = kv.AC.Button(key="submit",
                    text="Analyze CSV file",
                    )
myform = kv.AD.Form(key="aform",
                    childs = [sizing_facet_radio_group.div,
                              submit_btn],
                    on_submit=on_submit_click
           )


myform.on('submit', on_submit_click)
wp_endpoint = kv.create_endpoint(key="td_form",
                                 childs = [myform],
                                 title = "Form input and Validation",
                                 svelte_bundle_dir="csr",
                                 post_init_callback = post_init_page_load,
                                 rendering_type="CSR",
                                 

                              )

kv.add_route("/", wp_endpoint)



