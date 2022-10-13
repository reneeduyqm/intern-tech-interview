"""Defines a few basic endpoints for use in creating a request."""

import json
import re
from pathlib import Path

base_path = Path(__file__).resolve().parent

def construct_db():
    with open(base_path.parent / "database.json") as f:
        return json.load(f)

DB = construct_db()


def get(_id=None):
    """
    Get function to retrieve any item in the DB.

    :param _id: The ID of the item to get.
    :returns: A tuple that is one of the following forms:

        - If successfully retrieved:

            The first element is the item or all items in the DB and the second element
            is a status code of 200.

        - If _id not found:

            The first element is an error message and the second element
            is a status code of 404.
    """
    # Retrieve all of the DB
    if _id is None:
        return DB, 200

    # Retrieve an individual user based on the id
    item = DB.get(_id, None)

    # The user was not found
    if item is None:
        return 'Item not found', 404
    
    return item, 200


def post(body):
    """
    Post function to create a new item and add it to the database.

    :param body: The body used to create the new item.
        body['name'] The name of the item to create.
        body['email'] The email for the item to create.
        body['friends'] A list of friends for the item to create.
        body['age'] (optional) The age for the item to create.

    Body is a dictionary with this form:
    {
        "name": "<some name>",
        "email": "<some email>",
        "friends": ["<friend-id-1>", "<friend-id-2>"],
        "age": 50
    }

    :returns: A tuple that is one of the following forms:

        - If successfully created:

            The first element is the id of the new item and the second element
            is a status code of 201.

        - If name not in the body:

            The first element is an error message and the second element
            is a status code of 400.

        - If email not in the body:

            The first element is an error message and the second element
            is a status code of 400.

        - If email has incorrect form:

            The first element is an error message and the second element
            is a status code of 400.

        - If friends list contains an id that does not exist:

            The first element is an error message and the second element
            is a status code of 400.

        - If age is not an integer:

            The first element is an error message and the second element
            is a status code of 400.
    """
    # TODO: Your logic goes here
    if 'name' not in body:
        tuple_return = ("Error: name is not in the body", 400)

    if 'email' not in body:
        tuple_return = ("Error: email is not in the body", 400)

    regex = r'\b[a-z]{3}@brandosando.net\b'
    if(re.fullmatch(regex, body['email'])):
        tuple_return = ("Error: email is in incorrect form", 400)

    for friend in body['friends']:
        if friend not in DB.keys():
            tuple_return = ("Error: friends do not present", 400)

    if type(body['age']) != 'int':
        tuple_return = ("Error: age is not an integer", 400)

    if 'friends' not in body:
        tuple_return = ("Error: friends is not in the body", 400)

    else:   
        id_new = DB.keys()[-1]
        tuple_return = (id_new, 201)


    return tuple_return
    


def put(_id, body):
    """
    Put function to update an item in the database.

    :param _id: The ID of the item to update.
    :param body: The body used to update the new item.
        body['name'] The new name for the item.
        body['email'] The new email for the item.
        body['friends'] The new list of friends for the item.
        body['age'] (optional) The new age for the item.

    :returns: A tuple that is one of the following forms:

        - If successfully updated:

            The first element is None and the second element
            is a status code of 204.

        - If name not in the body:

            The first element is an error message and the second element
            is a status code of 400.

        - If email not in the body:

            The first element is an error message and the second element
            is a status code of 400.

        - If email has incorrect form:

            The first element is an error message and the second element
            is a status code of 400.

        - If friends list contains an id that does not exist:

            The first element is an error message and the second element
            is a status code of 400.

        - If user not found:

            The first element is an error message and the second element
            is a status code of 404.
    """
    # TODO: Your logic goes here
    if 'name' not in body:
        tuple_return = ("Error: name is not in the body", 400)

    if 'email' not in body:
        tuple_return = ("Error: email is not in the body", 400)

    regex = r'\b[a-z]{3}@brandosando.net\b'
    if(re.fullmatch(regex, body['email'])):
        tuple_return = ("Error: email is in incorrect form", 400)

    for friend in body['friends']:
        if friend not in DB.keys():
            tuple_return = ("Error: friends do not present", 400)
   
    if _id == None:
        tuple_return = ("Error: friends do not present", 404)


    if type(body['age']) != 'int':
        tuple_return = ("Error: age is not an integer", 400)

    if 'friends' not in body:
        tuple_return = ("Error: friends is not in the body", 400)

    else:   
        tuple_return = (None, 204)


    return tuple_return


def delete(_id):
    """
    Delete function to remove an item from the database.

    When a delete request is sent, the id of the item that is deleted should also be removed
    from any friends list throughout the database.

    :param _id: The ID of the item to delete.
    :returns: A tuple that is one of the following forms:

        - If successfully deleted:

            The first element is None and the second element
            is a status code of 204.

        - If item not found:

            The first element is an error message and the second element
            is a status code of 404.
    """
    # TODO: Your logic goes here
    if _id not in list(DB.keys()):
        tuple_return = ("Error: item not found", 404)
    else:
        tuple_return = (None, 204)

    return tuple_return



def search(query):
    """
    Search function to find an item based on a given query.

    This search is meant to be left to interpretation. Feel free to utilize anything that
    constitutes a search from the perspective of a query.

    For example:
    
        - You may want to create a "full text" search:
        `search("ado")`
        Return all items in the DB that has a value that contains the substr `"ado"`

        - Or you may want to do range queries:
        `search(("age", ">", 34))`
        Return all items in the DB that have an age greater than 34

        - Or you may want to search based on insertion time or most frequently retrieved:
        `search("frequency")`
        Return all items in the DB sorted by the frequency in which they are accessed in the database

    Any of the above are just examples of the myriad of options you have available to you.
    Please implement just one solution and describe how to search in the below section.

    ## TODO: ADD DESCRIPTION OF SEARCH ALGORITHM

    :param query: The query to search with.
    :returns: A tuple where the first element is a list of found documents that match the query and
        the second is a status code of 201.
    """
    # TODO: Your logic goes here
    lst = []
    for i in DB:
        item = DB[i]
        target_email = item["email"]
        if query in target_email:
            lst.append(target_email)
    return (lst, 201)



def graph_search(_id, degrees_of_freedom):
    """
    Construct a list of friends based on a given _id and a distance from that item.

    > Example Usage:
    ```python
    ## Example Database
    DB = {
        "49bf5290-434b-11ed-89f9-acde48001122": {
            "name": "Adonalsium",
            "email": "ado.brandosando.net",
            "friends": [
                "49bf5452-434b-11ed-89f9-acde48001122"
            ]
        },
        "49bf5452-434b-11ed-89f9-acde48001122": {
            "name": "Vivenna",
            "email": "viv.brandosando.net",
            "friends": []
        }
    }

    ## Main Code
    from api import graph_search

    print(graph_search("49bf5290-434b-11ed-89f9-acde48001122", 2))
    # [
    #   "49bf5452-434b-11ed-89f9-acde48001122": {
    #       "name": "Vivenna",
    #       "email": "viv.brandosando.net",
    #       "friends": []
    #   }
    # ]
    ```

    :param _id: The id of the item to use as the root document.
    :param degrees_of_freedom: The degrees of freedom from the given node to find.
    :returns:  A tuple where the first element is a list of found documents that are at maximum
        `N` degrees of freedom from the given node and the second is a status code of 201.
    """
    # TODO: Your logic goes here

    target = DB.get(_id)
    friends = target["friends"]
    res = {key: DB[key] for key in DB.keys() & friends}
    lst = []
    count = 1
    for key, val in res.items():
        if count == 1:
            lst.append(key)
            lst.append(val)
            count += 1
        else:
            if count <= int(degrees_of_freedom):
                lst.append(key)
                lst.append(val)
                count += 1
            else:
                break
    tuple_return = (lst, 201)
    return tuple_return
