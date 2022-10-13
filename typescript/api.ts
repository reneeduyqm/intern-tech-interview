/**
 * Defines a few basic endpoints for use in creating a request.
 */

export type User = {
  // The name of the user to create
  name: string;
  // The email for the user to create
  email: string;
  // The age for the user to create
  age?: number;
  // An array of friends for the user to create
  friends: string[];
};

export type Database = {
  [id: string]: User;
};

/**
 * Function to retrieve the "database".
 *
 * Parse the `database.json` file.
 * @returns The database representation
 */
export function getDB(): Database {
  return require("../database.json") as Database;
}
const DB = getDB();

type GetResponse = [Database | User | string, 200 | 404];
/**
 * Get function to retrieve any item in the DB.
 *
 * @param _id The ID of the item to get.
 * @returns A tuple that is one of the following forms:
 *
 *   - If successfully retrieved:
 *
 *       The first element is the item or all items in the DB and the second element
 *       is a status code of 200.
 *
 *   - If _id not found:
 *
 *       The first element is an error message and the second element
 *       is a status code of 404.
 */
export function getEndpoint(_id?: string): GetResponse {
  // Retrieve all of the DB
  if (_id == null) {
    return [DB, 200];
  }

  // Retrieve an individual user base on the id
  const item = DB[_id];

  // The user was not found
  if (item == null) {
    return ["Item not found", 404];
  }

  return [item, 200];
}

type PostResponse = [string, 201 | 400];
/**
 * Post function to create a new item and add it to the database.
 *
 * @param body The user to create
 * @returns A tuple that is one of the following forms:
 *   - If successfully created:
 *
 *       The first element is the id of the new item and the second element
 *       is a status code of 201.
 *
 *   - If name not in the body:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 *
 *   - If email not in the body:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 *
 *   - If email has incorrect form:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 *
 *   - If friends list contains an id that does not exist:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 */
export function postEndpoint(body?: Partial<User>): PostResponse {
  // TODO: Your logic goes here
  return ["", 201];
}

type PutResponse = [null | string, 204 | 400 | 404];
/**
 * Put function to update an item in the database.
 *
 * @param _id The ID of the item to update.
 * @param body The body used to update the user.
 * @returns A tuple that is one of the following forms:
 *   - If successfully updated:
 *
 *       The first element is null and the second element
 *       is a status code of 204.
 *
 *   - If name not in the body:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 *
 *   - If email not in the body:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 *
 *   - If email has incorrect form:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 *
 *   - If friends list contains an id that does not exist:
 *
 *       The first element is an error message and the second element
 *       is a status code of 400.
 *
 *   - If user not found:
 *
 *       The first element is an error message and the second element
 *       is a status code of 404.
 */
export function putEndpoint(_id?: string, body?: Partial<User>): PutResponse {
  // TODO: Your logic goes here
  return [null, 204];
}

type DeleteResponse = [null | string, 204 | 404];
/**
 * Delete function to remove an item from the database.
 *
 * When a delete request is sent, the id of the item that is deleted should also be removed
 * from any friends list throughout the database.
 *
 * @param _id The ID of the item to delete.
 * @returns A tuple that is one of the following forms:
 *
 *   - If successfully deleted:
 *
 *       The first element is None and the second element
 *       is a status code of 204.
 *
 *   - If item not found:
 *
 *       The first element is an error message and the second element
 *       is a status code of 404.
 */
export function deleteEndpoint(_id?: string): DeleteResponse {
  // TODO: Your logic goes here
  return [null, 204];
}
type SearchResponse = [User[], 201];
/**
 * Search function to find an item based on a given query.
 *
 * This search is meant to be left to interpretation. Feel free to utilize anything that
 * constitutes a search from the perspective of a query.
 *
 * For example:
 *
 *  - You may want to create a "full text" search:
 *      `search("ado")`
 *      Return all items in the DB that has a value that contains the substr `"ado"`
 *
 *  - Or you may want to do range queries:
 *      `search(("age", ">", 34))`
 *      Return all items in the DB that have an age greater than 34
 *
 *  - Or you may want to search based on insertion time or most frequently retrieved:
 *      `search("frequency")`
 *      Return all items in the DB sorted by the frequency in which they are accessed in the database
 *
 * Any of the above are just examples of the myriad of options you have available to you.
 * Please implement just one solution and describe how to search in the below section.
 *
 * ## TODO: ADD DESCRIPTION OF SEARCH ALGORITHM
 *
 * @param query The query to search with.
 * @returns A tuple where the first element is a list of found documents that match the query and
 *   the second is a status code of 201.
 */
export function searchEndpoint(query: any): SearchResponse {
  // TODO: Your logic goes here
  return [[], 201];
}

/**
 * Construct a list of friends based on a given _id and a distance from that item.
 *
 * > Example Usage:
 * ```typescript
 * // Example Database
 * DB = {
 *     "49bf5290-434b-11ed-89f9-acde48001122": {
 *         "name": "Adonalsium",
 *         "email": "ado.brandosando.net",
 *         "friends": [
 *             "49bf5452-434b-11ed-89f9-acde48001122"
 *         ]
 *     },
 *     "49bf5452-434b-11ed-89f9-acde48001122": {
 *         "name": "Vivenna",
 *         "email": "viv.brandosando.net",
 *         "friends": []
 *     }
 * }
 *
 * // Main Code
 * import { Database, User } from "./api";
 *
 * console.log(graph_search("49bf5290-434b-11ed-89f9-acde48001122", 2))
 * // [
 * //   "49bf5452-434b-11ed-89f9-acde48001122": {
 * //       "name": "Vivenna",
 * //       "email": "viv.brandosando.net",
 * //       "friends": []
 * //   }
 * // ]
 * ```
 *
 * @param _id The id of the item to use as the root document.
 * @param degreesOfFreedom The degrees of freedom from the given node to find.
 * @returns  A tuple where the first element is a list of found documents that are at maximum
 *  `N` degrees of freedom from the given node and the second is a status code of 201.
 */
export function graphSearchEndpoint(_id: string, degreesOfFreedom: number): SearchResponse {
  // TODO: Your logic goes here
  return [[], 201];
}
