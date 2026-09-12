import kavya as kv

import kavya_components as kvx

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
from starlette.testclient import TestClient
app = kv.load_app()

# ========================= create Slot type =========================
class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")
        

_ChildSlot_T = MutableHC_StubWrappedTypeGen("ChildSlot",
                                             SpanMixin,
                                             mutableShellMixins=[TwStyMixin,
                                                                 HCTextMixin,
                                                                 ValueMixin,
                                                                 VueTypeMixin
                                                                 ],
                                             stytags_getter_func=lambda m=ui_styles: m.sty.hinav_childslot 

                                                   )
ChildSlot_T = assign_id(_ChildSlot_T)


# ================================ end ===============================


# ===================== create breadcrumb step_T =====================

_Step_T = MutableHC_StubWrappedTypeGen("Step",
                                             SpanMixin,
                                             mutableShellMixins=[TwStyMixin,
                                                                 HCTextMixin,
                                                                 ValueMixin,
                                                                 VueTypeMixin
                                                                 ],
                                             stytags_getter_func=lambda m=ui_styles: m.sty.hinav_step

                                                   )
Step_T = assign_id(_Step_T)



HierarchyNavigator = kvx.HierarchyNavigator_TF(ChildSlot_T, Step_T)
italian_cuisine_hierarchy = {
    "Cuisine: Italian": {
        "Regions": {
            "Northern Italian cuisine": {
                "Description": "Characterized by less use of olive oil, tomatoes and pasta, and more use of butter, rice, corn (polenta), and cheeses for cream sauces. Includes regions like Lombardy, Piedmont, Veneto, Emilia-Romagna, Liguria.",
                "Dishes": {
                    "Risotto alla Milanese": {
                        "Ingredients": {
                            "Arborio or Carnaroli rice": 1,
                            "Saffron": 1,
                            "Parmesan cheese": 1,
                            "Beef or Chicken stock": 1,
                            "Butter": 1,
                            "Onion or Shallot": 1,
                            "White Wine": 1,
                            "Beef marrow (traditional)": 1
                        },
                        "Techniques": {
                            "Making Soffritto": 1,
                            "Toasting rice (Tostatura)": 1,
                            "Deglazing with wine": 1,
                            "Gradually adding hot stock": 1,
                            "Adding saffron": 1,
                            "Mantecatura (Finishing with butter and Parmesan)": 1
                        },
                        "Utensils": {
                            "Heavy-bottomed pan or pot": 1,
                            "Wooden spoon": 1,
                            "Ladle": 1
                        }
                    },
                    "Osso Buco": {
                        "Description": "Braised veal shanks, often served with Risotto alla Milanese.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Polenta": {
                        "Description": "Boiled cornmeal dish, served soft or allowed to set and then fried or grilled.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Lasagne alla Bolognese": {
                        "Description": "Layered pasta dish with Ragù Bolognese, Béchamel sauce, and Parmesan cheese.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Pesto alla Genovese": {
                        "Description": "Sauce originating from Genoa (Liguria) made with basil, pine nuts, garlic, Parmesan, Pecorino Sardo, and olive oil.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Tiramisu": {
                        "Description": "Coffee-flavored dessert with ladyfingers, mascarpone cheese, eggs, and cocoa. Origins debated, often associated with Veneto.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    }
                }
            },
            "Central Italian cuisine": {
                "Description": "Features simple preparations, emphasizing high-quality local ingredients like olive oil, pecorino cheese, cured meats, legumes, and seasonal vegetables. Includes regions like Tuscany, Umbria, Lazio, Marche.",
                "Dishes": {
                    "Spaghetti alla Carbonara": {
                        "Ingredients": {
                            "Spaghetti or Rigatoni pasta": 1,
                            "Guanciale (cured pork jowl - traditional)  or  Pancetta": 1,
                            "Eggs (yolks often preferred)": 1,
                            "Pecorino Romano cheese": 1,
                            "Black pepper": 1
                        },
                        "Techniques": {
                            "Cooking pasta al dente": 1,
                            "Rendering Guanciale or Pancetta": 1,
                            "Creating sauce emulsion with egg, cheese, pepper, and pasta water off heat": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet for cooking meat": 1,
                            "Bowl for mixing sauce": 1
                        }
                    },
                    "Bistecca alla Fiorentina": {
                        "Description": "Thick-cut T-bone steak (Chianina cattle traditionally) grilled rare.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Saltimbocca alla Romana": {
                        "Description": "Veal cutlets topped with prosciutto and sage, pan-fried.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Pasta Cacio e Pepe": {
                        "Description": "Simple pasta dish with Pecorino Romano cheese and black pepper.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Panzanella": {
                        "Description": "Tuscan bread salad with stale bread, tomatoes, onions, basil, olive oil, and vinegar.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Fettuccine Alfredo (Italian origin: Fettuccine al Burro)": {
                        "Description": "Pasta dish with butter and Parmesan cheese. The cream-heavy version is more Italian-American.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    }
                }
            },
            "Southern Italian cuisine": {
                "Description": "Known for its vibrant flavors, extensive use of olive oil, tomatoes, fresh vegetables (like eggplant, peppers), seafood, and dried pasta shapes. Includes mainland regions like Campania, Puglia, Calabria, Basilicata, and the islands.",
                "Dishes": {
                    "Pizza Margherita": {
                        "Ingredients": {
                            "Pizza dough (flour, water, yeast, salt)": 1,
                            "San Marzano Tomatoes (or other high-quality tomatoes)": 1,
                            "Mozzarella di Bufala Campana (or Fior di Latte Mozzarella)": 1,
                            "Fresh Basil": 1,
                            "Olive oil": 1
                        },
                        "Techniques": {
                            "Kneading and proofing dough": 1,
                            "Stretching and shaping the dough": 1,
                            "Making simple tomato sauce": 1,
                            "Topping and baking (traditionally in a wood-fired oven)": 1
                        },
                        "Utensils": {
                            "Oven (preferably high-temperature)": 1,
                            "Pizza stone or baking steel or sheet": 1,
                            "Pizza peel": 1
                        }
                    },
                    "Pasta alla Puttanesca": {
                        "Ingredients": {
                            "Spaghetti or Linguine pasta": 1,
                            "Tomatoes (canned or fresh)": 1,
                            "Black Olives (Gaeta traditionally)": 1,
                            "Capers": 1,
                            "Garlic": 1,
                            "Anchovies": 1,
                            "Red pepper flakes (optional)": 1,
                            "Olive oil": 1
                        },
                        "Techniques": {
                            "Making a quick, pungent tomato sauce": 1,
                            "Cooking pasta al dente": 1,
                            "Tossing pasta with sauce": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet or Sauté pan for making sauce": 1
                        }
                    },
                    "Parmigiana di Melanzane (Eggplant Parmesan)": {
                        "Description": "Layered dish of fried eggplant slices, tomato sauce, mozzarella, Parmesan, and basil.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Orecchiette con Cime di Rapa": {
                        "Description": "Ear-shaped pasta with broccoli rabe, often includes anchovies and garlic. Signature dish of Puglia.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    }
                },
                "Subregions": {
                     "Sicilian cuisine": {
                        "Description": "Influenced by various cultures (Greek, Arab, Norman, Spanish), featuring unique ingredients like pistachios, almonds, citrus, tuna, swordfish, ricotta, and eggplant.",
                        "Dishes": {
                            "Pasta alla Norma": {
                                "Description": "Pasta (often Maccheroni) with tomatoes, fried eggplant, salted ricotta cheese (Ricotta Salata), and basil.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                            "Arancini": {
                                "Description": "Fried rice balls, usually stuffed with ragù, mozzarella, and peas, or other variations.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                            "Caponata": {
                                "Description": "Sweet and sour eggplant relish with celery, olives, capers, and tomatoes.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                             "Cannoli": {
                                "Description": "Tube-shaped fried pastry shells filled with sweet, creamy ricotta filling.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                            "Cassata Siciliana": {
                                "Description": "Elaborate sponge cake soaked in liqueur or fruit juice, layered with ricotta cheese filling, covered in marzipan and decorated with candied fruit.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                           "Pasta con le Sarde": {
                                "Description": "Pasta dish with sardines, wild fennel, pine nuts, raisins, and saffron.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            }
                        }
                    }
                }
            }
        }
    }
}


async def terminal_node_callback(spath, msg):
    print ('childslot with child selected', spath)
    pass

house = kv.PD.Li(childs = [kv.PC.Div(classes="block transition hover:text-gray-700",
                                             childs = [
                                                 kv.PC.Span(classes="sr-only", text="home"),
                                                 kv.PC.FontAwesomeIcon(label="faHouse",
                                                                       classes="w-5 h-5")
                                                 ]

                                             )
                           

                           ]
                 )

import hinav_sty
with kv.TwStyCtx(hinav_sty): 
    hinav = HierarchyNavigator(italian_cuisine_hierarchy, terminal_node_callback,  house, key="hinav_sbs" , max_steps=20)
                   
wp_endpoint = kv.create_endpoint(key="hinav",
                              childs = [hinav.breadcrumb_panel,
                                        hinav.childslots_panel,
                                        hinav
                                        ],
                              title="Ofjustpy navigator cuisine",
                              twsty_tags=[space/y/4],
                              svelte_bundle_dir="ssr",

                              )


kv.add_route("/", wp_endpoint)
# with TestClient(app) as client:
#     response = client.get("/")
    
#     assert response.status_code == 200
