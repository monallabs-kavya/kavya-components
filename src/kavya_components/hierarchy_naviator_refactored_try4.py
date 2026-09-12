# from ofjustpy.MHC_types import (
#     Label as MLabel,
#     HCCMutable,
#     Button as MButton,
#     HCCStatic,
#     StackH as MStackH,
# )
# import ofjustpy as oj
# from ofjustpy.htmlcomponents_impl import assign_id
# from ofjustpy.SHC_types import PassiveComponents as PC, ActiveComponents as AC
# from py_tailwind_utils import *
# from ofjustpy_engine import HC_Div_type_mixins as TR
# from ofjustpy_engine.HCType import HCType
# from ofjustpy.ui_styles import sty
# from ofjustpy import ui_styles
# from ofjustpy.Div_TF import gen_Div_type

from functools import partial

# require for arrow button which is special type of mutable
# the text is mutable; but the twsty-tags remains the same

#from ofjustpy.HC_TF import gen_HC_type

from abc import ABC, abstractmethod

class BreadcrumbPanelInterface(ABC):
    @abstractmethod
    def get_step_at_idx(self, idx):
        pass

    @abstractmethod
    def update_step_text(self, idx, label_text, to_ms):
        pass

    @abstractmethod
    def get_max_steps():
        pass
    
class ChildsPanelInterface(ABC):
    @abstractmethod
    def get_childslots(self):
        pass

    @abstractmethod
    def hide_all_slots(self, target_of):
        pass

    @abstractmethod
    def update_child_panel(self, showitem, target_of):
        pass



# ================================ end ===============================



async def on_arrow_click(dbref, msg, target_of, hinav=None):
    """
    marker on the breadcrumb trail is clicked.
    fold the breadcrumb trail to the marker
    """
    hinav_shell = target_of(hinav)
    print("calling fold on ", dbref.value)
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

        def target_of(item, stubStore=session_manager.stubStore):
            """
            item is a stub or staticCore
            supports item.id which is spath
            for the item
            """
            return dget(stubStore, item.id).target


        # make the root open
        step_shell = dget(session_manager.stubStore,
                          self.staticCore.breadcrumb_panel.get_step_at_idx(0).id
                          ).target  # target_of(self.staticCore.steps[0])
        step_shell.remove_twsty_tags(noop / hidden)  # root is always open
        self.update_child_panel(target_of)
        pass

    def update_child_panel(self, target_of):
        """
        repopulate the child panel when selected-path gets updated
        """
        self.staticCore.childslots_panel.hide_all_slots(target_of)
        showitem = dget(self.staticCore.hierarchy, "/" + "/".join(self.show_path))
        self.staticCore.childslots_panel.update_child_panel(showitem, target_of)
        


    def fold(self, fold_idx, target_of):
        show_depth = self.show_depth
        for i in range(show_depth, fold_idx, -1):

            stepi = self.staticCore.breadcrumb_panel.get_step_at_idx(i-1)
            stepi_shell = target_of(stepi)
            print("hide crumb at ", stepi_shell, " ", stepi_shell.domDict, " ", stepi_shell.staticCore.domDict)
            stepi_shell.add_twsty_tags(noop / hidden)
            self.show_path.pop()
            self.show_depth = self.show_depth - 1
        

        self.update_child_panel(target_of)

        pass

    def unfold(self, child_label, target_of):
        # # the unseen arrow
        if self.show_depth == self.staticCore.max_steps:
            print("already at max_depth")
            return

        step_last = self.staticCore.breadcrumb_panel.get_step_at_idx(self.show_depth)
        step_shell = target_of(step_last)
        step_shell.remove_twsty_tags(noop / hidden)
        step_shell.add_twsty_tags(db.f)  # When hiding flex get taken out
        # eop: end-of-path
        self.staticCore.breadcrumb_panel.update_step_text(self.show_depth, child_label, target_of)

        self.show_depth += 1
        self.show_path.append(child_label)
        self.update_child_panel(target_of)

        pass

    def get_terminal_path(self, selected_child_label):
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        # on mouseover simply invoke the callback but do not update the child panel
        if isinstance(dval, dict):
            return  f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
        else:
            return  (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
        
    async def update_ui_on_child_select(self, selected_child_dbref, msg, target_of):
        terminal_path = self.get_terminal_path(selected_child_dbref.text)
        if '_cref' in terminal_path[-5:]:
            self.unfold(selected_child_dbref.text,
                        target_of
                        )
        await self.staticCore.callback_childslot_eh('on_click',
                                                    terminal_path,
                                                    msg
                                                    )

        pass


        
    async def update_ui_on_child_mouseenter(self, selected_child_dbref, msg, target_of):
        await self.staticCore.callback_childslot_eh('on_mouseenter',
                                                    self.get_terminal_path(selected_child_dbref.text),
                                                    msg
                                                    )

        pass
    

        
    async def update_ui_on_child_mouseleave(self, selected_child_dbref, msg, target_of):
        await self.staticCore.callback_childslot_eh('on_mouseleave',
                                                    self.get_terminal_path(selected_child_dbref.text),
                                                    msg
                                                    )            

        pass


        
    async def update_ui_on_child_dblclick(self, selected_child_dbref, msg, target_of):
        selected_child_label = selected_child_dbref.text
        await self.staticCore.callback_childslot_eh('on_dblclick',
                                                    self.get_terminal_path(selected_child_dbref.text),
                                                    msg
                                                    )            
        pass



    async def update_ui_on_child_lockclick(self, selected_child_dbref, msg, target_of):
        

        await self.staticCore.callback_childslot_eh('on_lockclick',
                                                    self.get_terminal_path(selected_child_dbref.text),
                                                    msg
                                                    )            
        pass


    async def update_ui_on_child_mouseover(self, selected_child_dbref, msg, target_of):
        await self.staticCore.callback_childslot_eh('on_mouseover',
                                                    self.get_terminal_path(selected_child_dbref.text),
                                                    msg
                                                    )            
        pass    
    
    
    
    
    

HinavBaseType = gen_Div_type(
    HCType.mutable, "Div", TR.DivMixin, mutable_shell_mixins=[HiNav_MutableShellMixin]
)


# childslot event handlers
async def on_childslot_click(dbref, msg, target_of, hinav=None):
    """
    when a child  of the head is clicked
    """
    hinav_shell = target_of(hinav)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_select(dbref, msg, target_of)

    pass


async def on_childslot_mouseover(dbref, msg, target_of, hinav=None):
    """
    when a child  of the head is clicked
    """
    hinav_shell = target_of(hinav)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_mouseover(dbref, msg, target_of)

    pass


async def on_childslot_mouseenter(dbref, msg, target_of, hinav=None):
    """
    when a child  of the head is clicked
    """
    hinav_shell = target_of(hinav)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_mouseenter(dbref, msg, target_of)

    pass


async def on_childslot_mouseleave(dbref, msg, target_of, hinav=None):
    """
    when a child  of the head is clicked
    """
    hinav_shell = target_of(hinav)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_mouseleave(dbref, msg, target_of)

    pass


async def on_childslot_dblclick(dbref, msg, target_of, hinav=None):
    """
    when a child  of the head is clicked
    """
    hinav_shell = target_of(hinav)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_dblclick(dbref, msg, target_of)

    pass

async def on_childslot_lockclick(dbref, msg, target_of, hinav=None):
    """
    when a child  of the head is clicked
    """
    hinav_shell = target_of(hinav)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    await hinav_shell.update_ui_on_child_lockclick(dbref, msg, target_of)

    pass


class _HierarchyNavigator(HinavBaseType):
    def __init__(self,
                 hierarchy,
                 childslot_event_handlers,
                 childslots_panel_gen,
                 breadcrumb_panel_gen,
                 *args,
                 **kwargs,
                 ):
        """
        childslots_panel_gen: is a function that takes as input event_handlers and returns a ChildSlotsPanel
        childslot_event_handlers: a dict of event handlers to be attached to the childslots
        breadcrumb_panel_gen: takes as input arrow_eh and returns breadcrumb_panel. Subclass of BreadcrumbPanelMixin
        """
        self.hierarchy = hierarchy
        # udeh : user defined event handler
        self.childslot_udeh = childslot_event_handlers

        # internal event handlers
        childslot_ieh = {
            'on_click': partial(on_childslot_click, hinav=self),
            'on_mouseover': partial(on_childslot_mouseover, hinav=self),
            'on_mouseenter': partial(on_childslot_mouseenter, hinav=self),
            'on_mouseleave': partial(on_childslot_mouseleave, hinav=self),
            'on_dblclick': partial(on_childslot_dblclick, hinav=self),
            'on_lockclick': partial(on_childslot_lockclick, hinav=self),
        }


        key = kwargs.get('key')
        childs_uictx = kwargs.get("childs_uictx", f"panels_{key}")
        with oj.uictx(childs_uictx):
            self.childslots_panel = childslots_panel_gen("childslots", childslot_ieh)
            self.breadcrumb_panel = breadcrumb_panel_gen("breadcrumbs", partial(on_arrow_click, hinav=self),
                                                         )
        self.max_steps = self.breadcrumb_panel.get_max_steps()


        super().__init__(*args, childs=[], **kwargs)


    async def callback_childslot_eh(self, event_type, terminal_path, msg):
        if event_type in self.childslot_udeh:
            await self.childslot_udeh[event_type](terminal_path, msg)
            



HierarchyNavigator = assign_id(_HierarchyNavigator)
