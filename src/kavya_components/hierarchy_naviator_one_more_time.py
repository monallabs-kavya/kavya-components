from abc import ABC, abstractmethod
import kavya as kv 

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
from kavya.htmlcomponents.html_tag_mixins import (DivMixin,
                                                  ButtonMixin,
                                                  VueTypeMixin
                                                  )

from py_tailwind_utils import *

class ChildsPanelInterface(ABC):
    @abstractmethod
    def get_child_slots(self):
        pass

    @abstractmethod
    def hide_all_slots(self):
        pass

    @abstractmethod
    def update_child_panel(self):
        pass

# breadcrumb_panel consists of steps 
class BreadcrumbPanelInterface(ABC):
    @abstractmethod
    def get_step_at_idx(self, idx):
        pass

    @abstractmethod
    def update_step_text(self, idx, label_text):
        pass

    @abstractmethod
    def get_max_steps():
        pass

#. HiNavPanel ABC
class HiNavInterface(ABC):
    @abstractmethod
    def update_child_panel(self):
        pass

    @abstractmethod
    def fold(self, fold_idx):
        pass

    @abstractmethod
    def unfold(child_label):
        pass
    
    @abstractmethod
    def stepdown_on_child_select(*args):
        pass
    
class ChildsPanel_MutableShellMixin(ChildsPanelInterface):

    def __init__(self, *args, **kwargs):

        pass
    
    def get_child_slots(self):
        # assuming child  slots are direct childs of panel 
        return self.components

    def hide_all_slots(self):
        for cs in self.get_child_slots():
            cs.add_twsty_tags(noop / hidden)

    def update_child_panel(self, showitem):
        for cs, clabel in zip(self.get_child_slots(),
                              filter(lambda x: x != "_cref", showitem.keys()),
                              ):
            cs.remove_twsty_tags(noop / hidden)
            cs.add_twsty_tags(db.f) # some bug about flex being removed if component is hidden 

            cs.text = clabel
            cs.value = clabel    



#TODO: USE HM.Div 
__ChildsPanel = MutableDiv_StubWrappedTypeGen("HiNavChildPanel",
                                                   DivMixin,
                                                   mutableShell_addonMixins = [ChildsPanel_MutableShellMixin],
                                                   staticCore_addonMixins= [VueTypeMixin],
                                                   
                                                   stytags_getter_func=lambda m=ui_styles: m.sty.hinav_childpanel


                                                )


class BreadcrumbPanel_MutableShellMixin(BreadcrumbPanelInterface):
    def __init__(self, *args, **kwargs):
        
        pass

    #. Assumption : steps are direct and only childs of breadcrumb panel 
    def get_step_at_idx(self, idx):
        return self.components[idx]


    def update_step_text(self, idx, label_text):
        step = self.get_step_at_idx(idx)
        step.text = label_text
        pass

    def get_max_steps(self):
        return len(self.components)
    


#TODO: USE HM.Div 
__BreadcrumbPanel = MutableDiv_StubWrappedTypeGen("HiNavBreadcrumbPanel",
                                                   DivMixin,
                                                   mutableShell_addonMixins = [BreadcrumbPanel_MutableShellMixin],
                                                   staticCore_addonMixins= [VueTypeMixin],
                                                   
                                                   stytags_getter_func=lambda m=ui_styles: m.sty.hinav_breadcrumbpanel


                                                )


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
        # the home icon at index 0 
        self.num_steps = len(self.staticCore.breadcrumb_panel.steps) + 1
        session_manager = kwargs.get("session_manager")

        self.breadcrumb_panel_ms = session_manager.target_of(self.staticCore.breadcrumb_panel.id)
        self.childslots_panel_ms = session_manager.target_of(self.staticCore.childslots_panel.id)

        # make the root open
        step_shell = self.breadcrumb_panel_ms.get_step_at_idx(1)
        step_shell.remove_twsty_tags(noop / hidden)  # root is always open
        self.show_depth = 2
        self.update_child_panel()
        pass

    def update_child_panel(self):
        """
        repopulate the child panel when selected-path gets updated
        """
        self.childslots_panel_ms.hide_all_slots()
        print("updating child panel for show_path = ", self.show_path)
        showitem = dget(self.staticCore.hierarchy, "/" + "/".join(self.show_path))

        self.childslots_panel_ms.update_child_panel(showitem)
        


    def fold(self, fold_idx):
        show_depth = self.show_depth
        print("now folding from ", show_depth -1 , "down to ", fold_idx)
        for idx in range(show_depth-1, fold_idx, -1):

            stepi_shell = self.breadcrumb_panel_ms.get_step_at_idx(idx)
            stepi_shell.add_twsty_tags(noop / hidden)
            self.show_path.pop()
            self.show_depth = self.show_depth - 1
        

        self.update_child_panel()

        pass

    def unfold(self, child_label):
        # the first step is house 
        if self.show_depth == self.num_steps:
            print("already at max_depth")
            return

        step_last_shell = self.breadcrumb_panel_ms.get_step_at_idx(self.show_depth)
        step_last_shell.remove_twsty_tags(noop / hidden)
        step_last_shell.add_twsty_tags(db.f)  # When hiding flex get taken out
        # eop: end-of-path
        self.breadcrumb_panel_ms.update_step_text(self.show_depth, child_label)

        self.show_depth += 1
        self.show_path.append(child_label)
        self.update_child_panel()

        pass

    # these event handlers are added to child slot 
    async def stepdown_on_child_select(self, selected_child_dbref, msg, wp, request):
        selected_child_label = selected_child_dbref.text
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            self.unfold(selected_child_label)
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

    async def update_ui_on_child_mouseenter(self, selected_child_dbref, msg, wp, request):
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

    async def update_ui_on_child_mouseleave(self, selected_child_dbref, msg, wp, request):
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


    async def update_ui_on_child_dblclick(self, selected_child_dbref, msg, wp, request):
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

    async def update_ui_on_child_lockclick(self, selected_child_dbref, msg, wp, request):
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
    

HiNavBase = MutableDiv_StubWrappedTypeGen("HiNavBase",
                                                   DivMixin,
                                                   mutableShell_addonMixins = [HiNav_MutableShellMixin],
                                                   staticCore_addonMixins= [VueTypeMixin],
                                                   stytags_getter_func=lambda m=ui_styles: m.sty.hinav
                                                   

                                                   )

async def on_child_slot_click(dbref, msg, wp, request,  hinav=None):
    """
    when a child  of the head is clicked
    """
    target_of = wp.session_manager.target_of
    hinav_shell = target_of(hinav.id)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.callback_on_child_select(dbref, msg, wp, request)

    pass


def TF(ChildSlot_T, Step_T):
    # ChildSlot_T should be of mutable type with text
    # Step_T should be of mutable type 
    class _ChildsPanel(__ChildsPanel):
        svelte_twtags_safelist = [noop/hidden]
        def __init__(self,
                     on_child_slot_clicked,
                     *args,
                     max_slots=20, 
                     on_child_slot_mouseenter =None,
                     on_child_slot_mouseleave = None,
                     on_child_slot_dblclick = None,
                     **kwargs
                     ):
            with kv.uictx("childspanel"):
                self.childslots = [
                    ChildSlot_T(key=f"slot_{i}",
                                text=str(i),
                                value=i,
                                on_click = on_child_slot_clicked
                                )
                    for i in range(max_slots)
            ]
            for cs_btn in self.childslots:
                if on_child_slot_mouseenter:
                    cs_btn.on('mouseenter', on_child_slot_mouseenter)
                if on_child_slot_mouseleave:
                    cs_btn.on('mouseleave', on_child_slot_mouseleave)
                # TODO: dblclick

                # if on_child_slot_dblclick:
                #     cs_btn.on('dblclick', on_child_slot_dblclick)
            super().__init__(childs = self.childslots, **kwargs
                             )
            pass

    ChildsPanel = assign_id(_ChildsPanel)
    class _BreadcrumbPanel(__BreadcrumbPanel):
        def __init__(self, max_steps, root_step_hc , on_step_click_eh, **kwargs):
            with kv.uictx("breadcrumb"):
                self.steps = [Step_T(key=f"step_{idx}",
                                     value = idx+1,
                                     on_click = on_step_click_eh 
                                     )
                              for idx in range (max_steps)
                              ]
            super().__init__(childs = [root_step_hc, *self.steps], **kwargs)
            pass



    BreadcrumbPanel = assign_id(_BreadcrumbPanel)
    class _HierarchyNavigator(HiNavBase):
        def __init__(self,
                     hierarchy,
                     callback_child_selected,
                     breadcrumb_root_step_hc, 
                     max_slots=20,
                     max_steps=3,
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
            self.max_steps = max_steps
            self.hierarchy = hierarchy
            self.callback_child_selected = callback_child_selected
            self.callback_childslot_mouseenter = callback_childslot_mouseenter
            self.callback_childslot_mouseleave = callback_childslot_mouseleave
            self.callback_childslot_dblclick = callback_childslot_dblclick
            self.callback_childslot_lockclick = callback_childslot_lockclick

            async def on_childslot_clicked_eh(dbref, msg, wp, request, hinav=self):
                target_of = wp.session_manager.target_of
                hinav_shell = target_of(hinav.id)
                # update the breadcrumb with new head and populate the childslots with the current
                # head's child
                await hinav_shell.stepdown_on_child_select(dbref, msg, wp, request)



            self.childslots_panel = ChildsPanel(on_childslot_clicked_eh,
                                              max_slots=max_slots,
                                              key="childpanel", 
                                              # on_child_slot_mouseenter = on_childslot_mouseenter_event_handler,
                                              # on_child_slot_mouseleave = on_childslot_mouseleave_event_handler,
                                              # on_child_slot_dblclick = on_childslot_dblclick_event_handler,
                                              # on_child_slot_lockclick  = on_childslot_lockclick_event_handler
                                              
                                              )
            async def on_step_click_eh(dbref, msg, wp, request,  hinav=self):
                """
                marker on the breadcrumb trail is clicked.
                fold the breadcrumb trail to the marker
                """
                target_of = wp.session_manager.target_of
                hinav_shell = target_of(hinav.id)
                print("start fold at idx = ", dbref.value)
                hinav_shell.fold(dbref.value)
                pass
            
            self.breadcrumb_panel = BreadcrumbPanel( max_steps,
                                                    breadcrumb_root_step_hc,
                                                    on_step_click_eh,
                                                    key="breadcrumb_panel"
                                                    )

            super().__init__(**kwargs)

    return assign_id(_HierarchyNavigator)
