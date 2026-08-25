import kavya as kv

from functools import partial
from kavya.type_factory.mutable_type_factory import (MutableDiv_StubWrappedTypeGen,
                                                     MutableHC_StubWrappedTypeGen,
                                                     )

from kavya.type_factory.mutable_mixins import (ValueSharerMixin
                                               )

from kavya.type_factory.common_mixins import (HCTextMixin,
                                              TwStyMixin
                                               )


from kavya.session_managment.uictx_id_assigner import assign_id
from kavya.htmlcomponents import ui_styles
from kavya.themes.ui_styles import sty
from kavya.htmlcomponents.html_tag_mixins import (DivMixin,
                                                  ButtonMixin,
                                                  SpanMixin, VueTypeMixin
                                                  )

from py_tailwind_utils import *
from .stackd import StackD

from py_tailwind_utils import *


# ============================= defaults =============================
icon_color="bg-primary-500"
ArrowSpan_HCType = kv.htmlcomponents.mutablehc_type_gen("Span",
                                               make_text_mutable=True,
                                               make_twtags_mutable=False)


class BreadcrumbPanel(kv.hccmutable._Div):
    def __init__(self, num_steps, on_click_eh):
        
        
        # first add house as root step with no text
        house = kv.PD.Li(childs = [kv.PD.Div(classes="block transition hover:text-gray-700",
                                             childs = [
                                                 kv.PC.Span(classes="sr-only", text="home"),
                                                 kv.PC.LucideIcon(label="house",
                                                                         #size="20px",
                                                                         width=6,
                                                                         stroke_color=icon_color
                                                                         #extra_classes = f"stroke-{icon_color} fill-{icon_color}",
                                                                         )



                                                 ]

                                             )
                           

                           ]
                 )
        
        self.arrows = [house, 
                       *[kv.AD.Button(
                           key=f"btn{i}",
                           value=i,
                           childs = [kv.PC.LucideIcon(label="triangle-right",
                                                      #size="20px",
                                                      width=6,
                                                      stroke_color=icon_color
                                                      #extra_classes = f"stroke-{icon_color} fill-{icon_color}",
                                                      )

                                     ],
                           classes="bg-white p-0",
                           
                on_click=on_click_eh
            )
            for i in range(1, num_steps)]
        ]
        self.labels = [
            ArrowSpan_HCType(key=f"label{i}", text="", twsty_tags=[mr / x / 0])
            for i in range(num_steps)
        ]
        self.steps = [
            kv.MD.StackH(
                key=f"item{idx}",
                childs=[self.labels[idx], self.arrows[idx]],
                twsty_tags=[
                mr / x / 0,
                noop / hidden,
                pd/2
            ],
        )
            for idx in range(num_steps)
        ]

        crumb_list =  kv.HM.Ul(classes="flex items-center gap-1 text-sm text-gray-600",
                                       childs=[*self.steps]
                                       )
        
        super().__init__(childs = [crumb_list])
        pass
    
    def get_step_at_idx(self, idx):
        return self.steps[idx]
    
    def update_step_text(self, idx, label_text, to_ms):
        label = self.labels[idx]
        label_ms = to_ms(label.id)
        label_ms.text = label_text
    
class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")

        
# ChildSlotBtn_HCType = assign_id(
#     gen_HC_type(
#         HCType.mutable,
#         "Button",
#         TR.SpanMixin,
#         staticCoreMixins=[],
#         mutableShellMixins=[TR.TwStyMixin, TR.HCTextMixin, ValueMixin], # value, style, and text : all is mutable
#         stytags_getter_func=lambda m=ui_styles: m.sty.button,
#     )
# )

def get_childslotbtn_stytags():
    return []
_ChildSlotBtn = MutableHC_StubWrappedTypeGen("ChildSlotBtn",
                                             SpanMixin,
                                             mutableShellMixins=[TwStyMixin,
                                                                 HCTextMixin,
                                                                 ValueMixin,
                                                                 VueTypeMixin
                                                                 ],
                                                   
                                             stytags_getter_func=get_childslotbtn_stytags
                                                   )
ChildSlotBtn = assign_id(_ChildSlotBtn)
# async def on_child_slot_mouseover(dbref, msg, to_mshell):
#     print ("calling on_childslot_mouseover")
#     await self.staticCore.callback_child_selected(terminal_path, msg)
#     pass

class ChildsPanel(kv.HM.Div):
    # modify on_child_slot_clicked shouldn't be the first argument
    def __init__(self,
                 on_child_slot_clicked,
                 *args,
                 max_childs=20,
                 on_child_slot_mouseenter =None,
                 on_child_slot_mouseleave = None,
                 on_child_slot_dblclick = None,
                 **kwargs):
        """
        event handler when childslot is clicked
        """

        
        self.childslots = [
                ChildSlotBtn(
                    key=f"cbtn{i}",
                    text=str(i),
                    value=i,
                    classes="rounded-lg border border-2 border-indigo-500/50 px-4 py-1 text-sm font-medium text-indigo-500 uppercase leading-normal hover:bg-gradient-to-bl hover:from-gray-200 hover:to-gray-200 hover:via-gray-100/50 w-52 overflow-x-auto shadow shadow-indigo-200  hover:shadow-md hower:shadow-indigo-300 focus:bg-gradient-to-bl focus:border-indigo-500/50 focus:border",
                    
                    
                    # twsty_tags=[
                    #     db.f,
                    #     ji.center,
                    #     gap/2,
                    #     bd/blue/500,
                    #     bg/blue/50,
                    #     pd/y/3,
                    #     pd/x/4,
                    #     fc/blue/700
                        
                    # ],
                    extra_classes="border-s-[3px]",
                    
                    on_click=on_child_slot_clicked,
                )
                for i in range(max_childs)
            ]

        for cs_btn in self.childslots:
            if on_child_slot_mouseenter:
                cs_btn.on('mouseenter', on_child_slot_mouseenter)
            if on_child_slot_mouseleave:
                cs_btn.on('mouseleave', on_child_slot_mouseleave)

            if on_child_slot_dblclick:
                cs_btn.on('dblclick', on_child_slot_dblclick)
                    

        menu_box = kv.HM.Div(classes="mt-6 flex-1 space-y-4 h-screen",
                             childs = self.childslots)
        

            
        super().__init__(childs = [menu_box],
                         classes = "flex overflow-y-auto min-w-fit h-screen flex-col justify-between border-e bg-white"
                         #twsty_tags = [max / W / "md", space / y / 2]
                         
                         )
        

    def hide_all_slots(self, target_of):
        for cs in self.childslots:
            shell = target_of(cs.id)
            shell.add_twsty_tags(noop / hidden)

    def update_child_panel(self, showitem, target_of):
        for cs, clabel in zip(
            self.childslots,
            filter(lambda x: x != "_cref", showitem.keys()),
        ):
            cs_shell = target_of(cs.id)
            cs_shell.remove_twsty_tags(noop / hidden)
            cs_shell.add_twsty_tags(db.f) # some bug about flex being removed if component is hidden 

            cs_shell.text = clabel
            cs_shell.value = clabel
            
        pass


# ================================ end ===============================

async def on_childbtn_click(dbref, msg, wp, request,  hinav=None):
    """
    when a child  of the head is clicked
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_select(dbref, msg, target_of)

    pass


async def on_childbtn_mouseover(dbref, msg, wp, request, hinav=None):
    """
    when a child  of the head is clicked
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_mouseover(dbref, msg, target_of)

    pass


async def on_childbtn_mouseenter(dbref, msg, wp, request,  hinav=None):
    """
    when a child  of the head is clicked
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_mouseenter(dbref, msg, target_of)

    pass


async def on_childbtn_mouseleave(dbref, msg, wp, request,  hinav=None):
    """
    when a child  of the head is clicked
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_mouseleave(dbref, msg, target_of)

    pass


async def on_childbtn_dblclick(dbref, msg, wp, request,  hinav=None):
    """
    when a child  of the head is clicked
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_dblclick(dbref, msg, target_of)

    pass

async def on_childbtn_lockclick(dbref, msg, wp, request,  hinav=None):
    """
    when a child  of the head is clicked
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_lockclick(dbref, msg, target_of)

    pass



async def on_arrow_click(dbref, msg, wp, request,  hinav=None):
    """
    marker on the breadcrumb trail is clicked.
    fold the breadcrumb trail to the marker
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)

    hinav_shell.fold(dbref.value, target_of)
    pass






class HiNav_MutableShellMixin:
    # All the state regarding the hinav will be defined
    # here
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        self.show_path = []
        self.arrrow_pos = 0
        self.show_depth = 1
        # if True, then disable navigation
        self.disabled = False
        session_manager = kwargs.get("session_manager")

        def target_of(item_id, stubStore=session_manager.stubStore):
            """
            item is a stub or staticCore
            supports item.id which is spath
            for the item
            """
            return dget(stubStore, item_id).target


        # make the root open
        step_shell = dget(
            session_manager.stubStore, self.staticCore.breadcrumb_panel.get_step_at_idx(0).id
        ).target  # target_of(self.staticCore.steps[0])
        step_shell.remove_twsty_tags(noop / hidden)  # root is always open
        self.update_child_panel(target_of)
        pass

    def update_child_panel(self, target_of):
        """
        repopulate the child panel when selected-path gets updated
        """
        self.staticCore.childpanel.hide_all_slots(target_of)
        showitem = dget(self.staticCore.hierarchy, "/" + "/".join(self.show_path))
        self.staticCore.childpanel.update_child_panel(showitem, target_of)
        


    def fold(self, fold_idx, target_of):
        show_depth = self.show_depth
        
        for i in range(show_depth, fold_idx, -1):

            stepi = self.staticCore.breadcrumb_panel.get_step_at_idx(i-1)
            stepi_shell = target_of(stepi.id)
            stepi_shell.add_twsty_tags(noop / hidden)
            self.show_path.pop()
            self.show_depth = self.show_depth - 1
        

        self.update_child_panel(target_of)

        pass

    def unfold(self, child_label, target_of):
        # # the unseen arrow
        if self.show_depth == self.staticCore.max_depth:
            print("already at max_depth")
            return

        step_last = self.staticCore.breadcrumb_panel.get_step_at_idx(self.show_depth)
        step_shell = target_of(step_last.id)
        step_shell.remove_twsty_tags(noop / hidden)
        step_shell.add_twsty_tags(db.f)  # When hiding flex get taken out
        # eop: end-of-path
        self.staticCore.breadcrumb_panel.update_step_text(self.show_depth, child_label, target_of)

        self.show_depth += 1
        self.show_path.append(child_label)
        self.update_child_panel(target_of)

        pass

    async def update_ui_on_child_select(self, selected_child_dbref, msg, target_of):
        selected_child_label = selected_child_dbref.text
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            self.unfold(selected_child_label, target_of)
            await self.staticCore.callback_child_selected(terminal_path, msg)
        else:
            terminal_path = (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
            await self.staticCore.callback_child_selected(terminal_path, msg)

        pass

    # async def update_ui_on_child_mouseover(self, selected_child_label, msg, target_of):
    #     dval = dget(
    #         self.staticCore.hierarchy,
    #         "/" + "/".join([*self.show_path, selected_child_label]),
    #     )
    #     # on mouseover simply invoke the callback but do not update the child panel
    #     if isinstance(dval, dict):
    #         terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
    #         await self.staticCore.callback_child_selected(terminal_path, msg)
    #     else:
    #         terminal_path = (
    #             f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
    #         )
    #         await self.staticCore.callback_child_selected(terminal_path, msg)

    #     pass

    async def update_ui_on_child_mouseenter(self, selected_child_dbref, msg, target_of):
        selected_child_label = selected_child_dbref.text

        
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        # on mouseover simply invoke the callback but do not update the child panel
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            await self.staticCore.callback_childslot_mouseenter(terminal_path, msg)
        else:
            terminal_path = (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
            await self.staticCore.callback_childslot_mouseenter(terminal_path, msg)

        pass

    async def update_ui_on_child_mouseleave(self, selected_child_dbref, msg, target_of):
        selected_child_label = selected_child_dbref.text
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        # on mouseover simply invoke the callback but do not update the child panel
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            await self.staticCore.callback_childslot_mouseleave(terminal_path, msg)
        else:
            terminal_path = (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
            await self.staticCore.callback_childslot_mouseleave(terminal_path, msg)

        pass


    async def update_ui_on_child_dblclick(self, selected_child_dbref, msg, target_of):
        selected_child_label = selected_child_dbref.text
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        # on mouseover simply invoke the callback but do not update the child panel
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            await self.staticCore.callback_childslot_dblclick(terminal_path, msg)
        else:
            terminal_path = (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
            await self.staticCore.callback_childslot_dblclick(terminal_path, msg)

        pass

    async def update_ui_on_child_lockclick(self, selected_child_dbref, msg, target_of):
        selected_child_label = selected_child_dbref.text
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        # on mouseover simply invoke the callback but do not update the child panel
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            await self.staticCore.callback_childslot_lockclick(terminal_path, msg)
        else:
            terminal_path = (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
            await self.staticCore.callback_childslot_lockclick(terminal_path, msg)

        pass
    
    
    
    
    

# HinavBaseType = gen_Div_type(
#     HCType.mutable, "Div", TR.DivMixin, mutable_shell_mixins=[HiNav_MutableShellMixin]
# )

def slideshowbase_twsty_tags():
    return []

HiNavBase = MutableDiv_StubWrappedTypeGen("HiNavBase",
                                                   DivMixin,
                                                   mutableShell_addonMixins = [HiNav_MutableShellMixin],
                                                   staticCore_addonMixins= [VueTypeMixin],
                                                   
                                                   stytags_getter_func=slideshowbase_twsty_tags
                                                   )



def HierarchyNavigator_TF(breadcrumb_panel_type=BreadcrumbPanel,
                          childpanel_type=ChildsPanel):
    """
    TF: class factory akin to template parametrization and specialization
    
    breadcrumb_panel_type, childpanel_type: should be class that supports oj.htmlcomponent interface
       - childs
       - classes
       - to_json_dict
       - etc.
    
    """
    class HierarchyNavigator(HiNavBase):
        def __init__(self,
                     hierarchy,
                     callback_child_selected,
                     max_childs=20,
                     max_depth=6,
                     *args,
                     callback_childslot_mouseenter = None,
                     callback_childslot_mouseleave = None,
                     callback_childslot_dblclick = None,
                     callback_childslot_lockclick = None,
                     **kwargs,
                     ):
            """
            callback_child_selected: notify caller when a child/member of a node in the hierarchy is selected
            TODO: need a more general way to handle any callback.
            
            """
            # TODO: Don't use MButton; use custom button type where both twsty and text is mutable
            self.max_depth = max_depth
            self.hierarchy = hierarchy
            self.callback_child_selected = callback_child_selected
            self.callback_childslot_mouseenter = callback_childslot_mouseenter
            self.callback_childslot_mouseleave = callback_childslot_mouseleave
            self.callback_childslot_dblclick = callback_childslot_dblclick
            self.callback_childslot_lockclick = callback_childslot_lockclick
            #on_childslot_clicked_event_handler = lambda *args, hinav=self: on_childbtn_click(*args, hinav)
            
            async def on_childslot_clicked_event_handler(*args, hinav=self):
                await on_childbtn_click(*args, hinav)

                
            on_childslot_mouseenter_event_handler = None
            
            if callback_childslot_mouseenter:
                async def on_childslot_mouseenter_event_handler(*args, hinav=self):
                    await on_childbtn_mouseenter(*args, hinav)
                

            on_childslot_mouseleave_event_handler = None
            if callback_childslot_mouseleave:
                async def on_childslot_mouseleave_event_handler(*args, hinav=self):
                    await on_childbtn_mouseleave(*args, hinav)

            on_childslot_dblclick_event_handler = None
            if callback_childslot_dblclick:
                async def on_childslot_dblclick_event_handler(*args, hinav=self):
                    await on_childbtn_dblclick(*args, hinav)


            on_childslot_lockclick_event_handler = None                    
            if callback_childslot_lockclick:
                async def on_childslot_lockclick_event_handler(*args, hinav=self):
                    await on_childbtn_lockclick(*args, hinav)
                
            self.childpanel = childpanel_type(on_childslot_clicked_event_handler,
                                              max_childs=max_childs,
                                              on_child_slot_mouseenter = on_childslot_mouseenter_event_handler,
                                              on_child_slot_mouseleave = on_childslot_mouseleave_event_handler,
                                              on_child_slot_dblclick = on_childslot_dblclick_event_handler,
                                              on_child_slot_lockclick  = on_childslot_lockclick_event_handler
                                              
                                              )
            self.breadcrumb_panel = breadcrumb_panel_type(max_depth,
                                                          lambda *args, hinav=self: on_arrow_click(*args, hinav))

            super().__init__(*args, childs=[], **kwargs)


    HierarchyNavigator = assign_id(HierarchyNavigator)
    return HierarchyNavigator

HierarchyNavigator = HierarchyNavigator_TF()
