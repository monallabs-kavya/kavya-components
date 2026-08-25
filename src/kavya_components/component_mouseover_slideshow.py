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
from kavya.htmlcomponents.html_tag_mixins import (VueTypeMixin
                                                  )
from kavya.session_managment.uictx_id_assigner import assign_id
from kavya.htmlcomponents import ui_styles
from kavya.themes.ui_styles import sty
from kavya.htmlcomponents.html_tag_mixins import (DivMixin,
                                                  ButtonMixin
                                                  )

from py_tailwind_utils import *
from .stackd import StackD



# all mutable variable declarations goes here
class SlideShow_MutableShellMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        pass


# SlideShowBase = gen_Div_type(
#     HCType.mutable,
#     "Div",
#     TR.DivMixin,
#     mutable_shell_mixins=[SlideShow_MutableShellMixin],
# )

def stytags_getter_func():
    return []
SlideShowBase = MutableDiv_StubWrappedTypeGen("SlideShowBase",
                                                   DivMixin,
                                                   mutableShell_addonMixins = [SlideShow_MutableShellMixin],
                                                   staticCore_addonMixins=[VueTypeMixin],
                                                   
                                                   stytags_getter_func=stytags_getter_func
                                                   )

async def on_mouseover_action(dbref, msg, wp, request, slideshow=None):
    # a button has been clicked
    # get the spath/id and the value of the button
    target_of = wp.session_manager.target_of
    deck_shell = target_of(slideshow.slide_deck.id)
    slide = slideshow.slides[dbref.value]
    deck_shell.bring_to_front(slide.id)

    pass


class SlideShow(SlideShowBase):
    def __init__(
        self, key, slide_labels, slide_info, height_anchor_label, *args, **kwargs
    ):
        """
        The height_anchor_label controls the height of the resulting slideshow panel.
        We need to give grid panel height since
        """

        doorcards = []
        self.slides = {}

        for sl in slide_labels:
            # create the panel for slide_info
            # The slide needs to be css-mutable
            # as it will hidden/unhidden via deck
            slide = kv.HS.StackV(
                key=f"slide_{sl}",
                childs=[
                    kv.PD.TitledPara(slide_info[sl][0], section_depth=5),
                    kv.PD.Halign(
                        slide_info[sl][1],
                        align="start",
                        twsty_tags=[pd / x / 4],
                    ),
                ],
            )

            # create the corresponding doorcard
            doorcard = kv.AC.Button(
                key=f"{sl}_doorcard",
                twsty_tags=[
                    fc / rose / 300,
                    ta.center,
                    bdr.lg,
                    bd / gray / 300,
                    boxtopo.bd,
                    fw.medium,
                    *hover(*build_gradient_expr(pink / 200, pink / 200, gray / 50)),
                    *build_gradient_expr(pink / 100, pink / 100, gray / 50),
                    shadow / gray / 200,
                    shadow.md,
                ],
                text=slide_info[sl][0],
                value=sl,
                on_click = partial(on_mouseover_action, slideshow=self),
            )
            doorcards.append(doorcard)
            self.slides[sl] = slide

        doorcards_panel = kv.PD.StackG(
            num_cols=1,
            num_rows=2,
            childs=doorcards,
            twsty_tags=[
                W / "1/2",
                gap/2,
                *variant(G / cols / 1, rv="sm"),
                *variant(G / cols / 2, gap/2, rv="md"),
                *variant(G / cols / 3, gap/3, rv="lg"),
            ],
        )

        self.slide_deck = StackD(
            key=f"deck_{key}",
            childs=self.slides.values(),
            twsty_tags=[W / "1/2"],
            height_anchor_key=f"slide_{height_anchor_label}",
        )

        # flx.one because we want both left and right div to expand and occupy
        # equal space
        twsty_tags = conc_twtags(*sty.stackh,
                                 *kwargs.pop("twsty_tags", []),
                                 flxrsz.one
                                 )

        # super().__init__(*args, key=key,
        #                  childs=[StackH_Aligned(doorcards_panel, content_type="mutable"),
        #                          StackH_Aligned(self.slide_deck, content_type="mutable")
        #                          ],
        #                  twsty_tags=twsty_tags,
        #                  **kwargs
        #                  )

        super().__init__(
            *args,
            key=key,
            childs=[doorcards_panel, self.slide_deck],
            twsty_tags=twsty_tags,
            **kwargs,
        )

        # super().__init__(*args, childs=[aligned_doorcards_panel,
        #                                 aligned_slide_deck
        #                                 ],
        #                  twsty_tags=twsty_tags,
        #                  **kwargs
        #                  )

        pass


SlideShow = assign_id(SlideShow)
