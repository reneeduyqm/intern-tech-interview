import * as api from "./api"

const readResult = api.getEndpoint("49bf5290-434b-11ed-89f9-acde48001122");
const createResult = api.postEndpoint({
    "name": "Vin",
    "email": "vin.brandosando.net",
    "friends": ["49bf5498-434b-11ed-89f9-acde48001122"]
});
const updateResult = api.putEndpoint("49bf5290-434b-11ed-89f9-acde48001122", {
    "name": "Vin",
    "email": "vin.brandosando.net",
    "friends": []
});
const deleteResult = api.deleteEndpoint("49bf5452-434b-11ed-89f9-acde48001122");
const graphResult = api.graphSearchEndpoint("49bf5290-434b-11ed-89f9-acde48001122", 2);
