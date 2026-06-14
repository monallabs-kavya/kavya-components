from kavya_components import VarLenghtList_TF
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner


app = kv.load_app()
VarLenghtList = assign_id(VarLenghtList_TF())

# def on_slot_clicked(dbref, msg, to_ms):
#     pass
# varlenghtlist = VarLenghtList("varlenghtlist",
#                               max_slots = 20,
#                               on_slot_clicked = on_slot_clicked
#                               )
