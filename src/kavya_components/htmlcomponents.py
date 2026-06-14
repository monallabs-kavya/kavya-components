
from typing import List, AnyStr, Callable, Any
from .stackd import StackD
from .linear_selector import LinearSelector
import kavya as kv
from py_tailwind_utils import (
    mr,
    x,
    pd,
    y,
    W,
    twmax,
    bg,
    green,
    rose,
    db,
    space,
    jc,
    auto,
    full,
    hidden,
    pink,
    conc_twtags,
    tstr,
    shadow,
    cyan,
    shadow,
    variant,
    gray,
    fc,
    slate,
    bd,
    H,
    top,
    right,
    ppos,
    hidden,
    db,
    ppos,
    screen,
    noop
)
from py_tailwind_utils import (primary
                               )
#from ofjustpy.htmlcomponents_impl import assign_id
# from ofjustpy.htmlcomponents import (
#     Mutable,
#     HCCMutable,
#     ActiveComponents as AC,
#     PassiveComponents as PC,
#     ActiveDivs as AD,
#     HCCStatic,
# )

# from ofjustpy.HC_wrappers import Halign
import itertools

def EnumSelector(key, enumtype, **kwargs):
    enumselect = kv.AD.Select(
        key=key,
        childs=[kv.PC.Option(text=str(_.value), value=str(_.value)) for _ in enumtype],
        **kwargs,
    )
    return enumselect





def BiSplitView(childs: List, hc_types, twsty_tags=[], **kwargs):
    """
    hc_types needs fields
    - part_viewer : component to control how each part of the spilt is
    - full_viewer: to control how the parts are to be stacked


    """
    bg_colors = [bg / primary / 400, bg / primary / 600]
    idx = 0
    parts = [[], []]
    for _ in childs:
        parts[idx % 2].append(_)
        #. TODO: twsty_tags is not part of the core
        # it belongs to mutableShell
        # use post_mutableshell_create_callback
        #_.add_twsty_tags(bg_colors[(int(idx / 2)) % 2])

        idx = idx + 1

    #. part_viewer should be of HCCMutable type

    boxes = [
        hc_types.part_viewer(key="part1", childs=parts[0], twsty_tags=[W / "5/12", space / y / 2]),
        hc_types.part_viewer(key="part2", childs=parts[1], twsty_tags=[W / "5/12", space / y / 2]),
    ]

    # TODO: use hccmutable so that key is not required
    return hc_types.full_viewer(key="full_viewer", 
        childs=boxes, twsty_tags=[db.f, jc.center, space / x / 4, *twsty_tags], **kwargs
    )


# # from ofjustpy.MHC_types import Label as MLabel, StackD
def chunks(iterable, size):
    """Generate adjacent chunks of data"""
    it = iter(iterable)
    return iter(lambda: tuple(itertools.islice(it, size)), ())


def Paginate(
    key,
    childs,
    page_container_gen,
    num_pages=10,
    chunk_size=100,
    twsty_tags=[],
    stackd_tags=[H / screen],
    **kwargs,
):
    """
    There is a bug/gotcha w.r.t height of the stackD because
    stackD uses relative/absolute positioning.
    Specify exact height of the stackD used in the paginate section.
    """
    page_containers = [
        page_container_gen(cid, childs=achunk, twsty_tags=[W / full])
        for cid, achunk in enumerate(chunks(childs, chunk_size))
    ]

    all_pages = StackD(
        key=f"{key}_stackD",
        childs=page_containers,
        twsty_tags=stackd_tags,
        height_anchor_key=page_containers[0].key,
    )

    async def on_page_select(dbref, msg, wp, request):
        target_of = wp.session_manager.target_of
        selected_page = page_containers[int(msg["value"])]
        shell_deck = target_of(all_pages.id)
        shell_deck.bring_to_front(selected_page.id)

        pass

    page_selector = kv.HM.Halign(LinearSelector(
                                     key=f"{key}_selector",
                                     num_iter=range(len(page_containers)),
                                     on_click=on_page_select,
                                     twsty_tags = []
                                 ),
                                 key="halign",
                                 )

    return kv.HM.StackV(key="paginate_top",
        childs=[page_selector, all_pages], twsty_tags=twsty_tags, **kwargs
    )


# # ============================== Dockbar =============================


# def on_undock_click(undock_btn, msg, target_of, dockbar=None):
#     # undock the target; make it visible
#     #dock_shell = target_of(dockbar.wrapped_components[msg.value])
#     dock_shell = target_of(dockbar.wrapped_components[undock_btn.value])
#     dock_shell.remove_twsty_tags(noop/hidden)

#     # disable the undock_btn
#     undock_btn.disabled = True


#     pass


# def on_dock_click(dock_btn, msg, target_of, dockbar=None):
#     key = dock_btn.value
    
#     #dock_shell = target_of(dockbar.wrapped_components[msg.value])
#     dock_shell = target_of(dockbar.wrapped_components[dock_btn.value])
#     dock_shell.add_twsty_tags(noop/hidden)
#     shell_undock_btn = target_of(dockbar.undock_btns[key])
#     # print("dock it: changes on undock button: ",  type(shell_undock_btn.domDict), " ", type(shell_undock_btn.attrs))

    
#     # print("dock it: changes on undock button: ",  shell_undock_btn.domDict, " ", shell_undock_btn.attrs)
        
#     # This expression doesn't invoke the __setitem__ for the onekeyDict:
#     # Don't know why 
#     shell_undock_btn.disabled = False

#     # print("dock it: changes on undock button: ",  shell_undock_btn.domDict, " ", shell_undock_btn.attrs)
#     # print("dock it: changes on undock button: ",  [_ for _ in shell_undock_btn.domDict.get_changed_history()], " ",
#     #       [_ for _ in shell_undock_btn.attrs.get_changed_history()]
#     #       )

#     pass


# class UndockButtonMixin:
#     """
#     In addition to changes to classes,
#     UndockButton has changes to attribute

#     """
#     attr_tracked_keys = ['disabled']
#     domDict_tracked_keys = []
    
#     def __init__(self, *args, **kwargs):
#         self.attrs.disabled = True

#     @property
#     def disabled(self):
#         return self.attrs.get("disabled", None)

#     @disabled.setter
#     def disabled(self, value):
#         if value is not None:
#             self.attrs["disabled"] = value
#         elif "value" in self.attrs:
#             del self.attrs["value"]


# from ofjustpy_engine import HC_Div_type_mixins as TR
# from ofjustpy.ui_styles import sty
# from ofjustpy import ui_styles
# from ofjustpy.HC_TF import HCType, gen_HC_type
# from ofjustpy_engine import mutable_TF_impl as mutable_TF_mixins

# UndockButton = assign_id(
#     gen_HC_type(
#         HCType.mutable,
#         "Button",
#         TR.ButtonMixin,
#         stytags_getter_func=lambda m=ui_styles: m.sty.undock_button,
#         mutableShellMixins = [UndockButtonMixin, TR.TwStyMixin],
#         mutableShell_addonMixins=[
#             mutable_TF_mixins.StaticCoreSharer_ValueMixin,
#         ],
#         staticCoreMixins = [TR.HCTextMixin]
#     )
# )


# class Dockbar:
#     def __init__(
#         self, dockable_items, dock_labels, *args, wdiv_type=HCCStatic.Div, **kwargs
#     ):
#         """
#         assuming that the item being docked are static items.
#         If they are Mutable then use general mutable Mutable.Div
#         for wdiv_type

#         """
#         undock_btn_sty = kwargs.get(
#             "undock_btn_sty",
#             [
#                 #shadow.xl,
#                 #bg / cyan / 5,
#                 #shadow / cyan / "500/50",
#                 *variant(
#                     bg / gray / 400,
#                     fc / slate / 500,
#                     bd / slate / 200,
#                     shadow.none,
#                     rv="disabled",
#                 ),
#             ],
#         )

#         # components that need to be docked/undocked
#         self.wrapped_components = {}
#         self.undock_btns = {}
#         dockit_handler = lambda *args, dockbar=self: on_dock_click(
#             *args, dockbar=dockbar
#         )
#         undockit_handler = lambda *args, dockbar=self: on_undock_click(
#             *args, dockbar=dockbar
#         )
#         for idx, (di, dock_label) in enumerate(zip(dockable_items, dock_labels)):
#             key = str(idx)
#             undock_btn = UndockButton(
#                 key=f"undockbtn_{key}",
#                 text=dock_label,
#                 disabled=True,
#                 value=key,
#                 twsty_tags=undock_btn_sty,
#                 on_click=undockit_handler,
#             )

#             # dock_btn = AC.Button(
#             #     key=f"dock_{key}",
#             #     text="-",
#             #     value=key,
#             #     twsty_tags=[bg / pink / 1, W / 6, H / 6, top / 1, right / 1, absolute],
#             #     on_click=dockit_handler,
#             # )
#             with oj.TwStyCtx(oj.ui_styles.un):
#                 dock_btn = AD.Button(key=f"dock_{key}", twsty_tags=[W/3, H/1, bg/rose/500, top / 1, right / 1, ppos.absolute], value=key,  on_click=dockit_handler)
                
#             wrapped_component = wdiv_type(
#                 key=f"wrap_{key}", childs=[di, dock_btn], twsty_tags=[ppos.relative]
#             )

#             self.undock_btns[key] = undock_btn
#             self.wrapped_components[key] = wrapped_component

