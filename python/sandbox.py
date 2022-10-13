import api

read_result = api.get("49bf5290-434b-11ed-89f9-acde48001122")
create_result = api.post({
    "name": "Vin",
    "email": "vin.brandosando.net",
    "friends": ["49bf5498-434b-11ed-89f9-acde48001122"]
})
update_result = api.put("49bf5290-434b-11ed-89f9-acde48001122", {
    "name": "Vin",
    "email": "vin.brandosando.net",
    "friends": []
})
delete_result = api.delete("49bf5452-434b-11ed-89f9-acde48001122")
graph_result = api.graph_search("49bf5290-434b-11ed-89f9-acde48001122", 2)
