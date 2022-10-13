/**
 * Tests for api.ts
 */
import * as api from "./api";
import { Database, User } from "./api";

let TEST_DB: Database;
beforeEach(() => {
  TEST_DB = require("../database.json");
  jest.spyOn(api, "getDB").mockImplementation(() => TEST_DB);
});

test("getEndpoint succeeds when retrieving all users", () => {
  const [user, status] = api.getEndpoint();

  expect(status).toEqual(200);
  expect(user).toEqual(TEST_DB);
});

test("getEndpoint succeeds when retrieving one user", () => {
  const userID = Object.keys(TEST_DB)[0];

  const [user, status] = api.getEndpoint(userID);

  expect(status).toEqual(200);
  expect(user).toEqual(TEST_DB[userID]);
});

test("getEndpoint fails when user is not found", () => {
  const [msg, status] = api.getEndpoint("does_not_exist");

  expect(status).toEqual(404);
  expect(msg).toMatch(/not found/);
});

test("postEndpoint succeeds when creating a new user.", () => {
  const originalUserCount = Object.keys(TEST_DB).length;
  const body = {
    name: "Waxillium",
    email: "wav@brandosando.net",
    friends: [],
    age: 25,
  };

  const [userID, status] = api.postEndpoint(body);

  expect(status).toEqual(201);
  expect(TEST_DB).toHaveProperty(userID);
  expect(Object.keys(TEST_DB)).toHaveLength(originalUserCount + 1);
});

test.each([
  [{}, 400, "body"],
  [{ email: "wax@brandosando.net" }, 400, "name"],
  [{ name: "wax" }, 400, "email"],
  [{ email: "wax@brandosando.net", name: "wax" }, 400, "friends"],
  [{ email: "wax@brandosando", name: "wax", friends: [] }, 400, "incorrect form"],
  [{ email: "wax@brandosando.net", name: "wax", friends: ["bad name"] }, 400, "not present"],
])(
  "postEndpoint fails with invalid data",
  (body: Partial<User>, statusCode: number, message: string) => {
    const [msg, status] = api.postEndpoint(body);
    expect(msg).toMatch(message);
    expect(status).toEqual(statusCode);
  }
);

test("putEndpoint succeeds when updating a new user.", () => {
  const body = { name: "Siri", email: "sir@brandosando.net", friends: [] };
  const userID = Object.keys(TEST_DB)[0];

  const [msg, status] = api.putEndpoint(userID, body);

  expect(msg).toBeNull();
  expect(status).toEqual(204);
  expect(body).toEqual(TEST_DB[userID]);
});

test.each([
  [0, {}, 400, "body"],
  [0, { email: "wax@brandosando.net" }, 400, "name"],
  [0, { name: "wax" }, 400, "email"],
  [0, { email: "wax@brandosando.net", name: "wax" }, 400, "friends"],
  [null, { name: "Siri", email: "sir@brandosando.net", friends: [] }, 400, "not found"],
  [0, { email: "wax@brandosando", name: "wax", friends: [] }, 400, "incorrect form"],
  [0, { email: "wax@brandosando.net", name: "wax", friends: ["bad name"] }, 400, "not present"],
])(
  "putEndpoint fails with invalid data",
  (_idIndex: number | null, body: Partial<User>, statusCode: number, message: string) => {
    let _id: string;
    if (_idIndex === null) {
      _id = "bad_id";
    } else {
      _id = Object.keys(TEST_DB)[_idIndex];
    }

    const [msg, status] = api.putEndpoint(_id, body);
    expect(msg).toMatch(message);
    expect(status).toEqual(statusCode);
  }
);

test("deleteEndpoint succeeds", () => {
  const originalUserCount = Object.keys(TEST_DB).length;
  const userID = Object.keys(TEST_DB)[0];

  const [msg, status] = api.deleteEndpoint(userID);

  expect(msg).toBeNull();
  expect(status).toEqual(204);
  expect(TEST_DB[userID]).toBeFalsy();
  expect(Object.keys(TEST_DB)).toHaveLength(originalUserCount - 1);
});

test.each([[null, 404, "not found"]])(
  "deleteEndpoint fails",
  (_id: null | string, statusCode: number, message: string) => {
    const [msg, status] = api.deleteEndpoint();

    expect(msg).toMatch(message);
    expect(status).toEqual(statusCode);
  }
);
