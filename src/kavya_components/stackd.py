import kavya as kv
from kavya.session_managment.uictx_id_assigner import assign_id
from kavya.type_factory.mutable_type_factory import (MutableDiv_StubWrappedTypeGen,
                                                     MutableHC_StubWrappedTypeGen,
                                                     )

from kavya.htmlcomponents import ui_styles
from kavya.htmlcomponents.html_tag_mixins import (DivMixin, VueTypeMixin,
                                                  )

from py_tailwind_utils import *

class StackDMixin:
    """
    create visual stack over components. Only one component is visible.
    The deck components have to be mutable.
    height_anchor_key: The key of the component which will determine the
    height of the deck.This is required to keep the height unchanged
    when it is shuffled.
    """

    svelte_twtags_safelist = [#W/full, not required
                       H/twmax,
                       overflow.auto,
                       ppos.absolute,
                       lv.iv]
    
        
    attr_tracked_keys = []
    domDict_tracked_keys = []

    def __init__(self, *args, **kwargs):
        height_anchor_key = kwargs.get("height_anchor_key")

        for dbref in self.components:
            if dbref.staticCore.key == height_anchor_key:
                dbref.add_twsty_tags(#W / full,
                                     H / twmax
                                     )
            else:
                dbref.add_twsty_tags( H / twmax, #W / full, 
                    overflow.auto,
                    ppos.absolute)
            dbref.add_twsty_tags(lv.iv)
        self.selected_card_spath = self.components[0].id
        selected_dbref = self.spathMap[self.selected_card_spath]
        selected_dbref.remove_twsty_tags(lv.iv)

    def bring_to_front(self, spath):
        """
        spath: the target component which needs to be brought in front
        """
        
        tapk = spath
        if tapk in self.spathMap.keys():
            # hide the current front
            self.spathMap[self.selected_card_spath].add_twsty_tags(lv.iv)
            # make the selected card visible
            selected_dbref = self.spathMap[tapk]
            selected_dbref.remove_twsty_tags(lv.iv)
            self.selected_card_spath = tapk

        else:
            logger.debug(
                f"debug: deck  does not have card {spath}..skipping bring to front"
            )
        pass


class StackDSvelteSafelist:
    """
    """
    svelte_twtags_safelist = [W/full, H/twmax, overflow.auto, ppos.absolute, lv.iv]

    def __init__(self, *args, **kwargs):
        pass

def stytags_getter_func():
    return [db.f, flxrsz.one, ppos.relative]


_StackD = MutableDiv_StubWrappedTypeGen("StackD",
                                        DivMixin,
                                        mutableShell_addonMixins = [StackDMixin],
                                        staticCore_addonMixins = [StackDSvelteSafelist, VueTypeMixin],
                                        stytags_getter_func=stytags_getter_func
                                        )
_StackD.svelte_twtags_safelist = [W/full, H/twmax, overflow.auto, ppos.absolute, lv.iv]
StackD = assign_id(_StackD)
