# Overview

This repository houses all of the code necessary to answer the Intern interview questions for the Data Lifecycle Management team at LLNL.

## Submitting a Response

Responding to this technical interview will involve creating a fork of the project under your github account. To learn more about forking checkout [these docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

You will have 3 days to respond. Access will be granted at 8 AM PST on October 10th, and all code should be finalized by 11:59 PM PST, October 12th.

We expect you to have clean, concise, readable code that is well documented and efficient. Feel free to use Google to the best of your ability to help in answering the questions, if you do use Google, please make a note about where you used it as a comment in the code.

## Problem Statement

Create PUT, POST, and DELETE methods for an API.

In addition create utility functions SEARCH and GRAPH_SEARCH for the API.

This can be done in either Python or in Typescript (do not do both). Depending on your language chosen, you should modify the files in the proper language directory (`python` for Python, `typescript` for Typescript).

### Expectations

Each function in `api` file has a docstring that outlines the desired end state of each request. Please be considerate of edge cases that may not be described to you (especially in the `search` and `graph_search` functions).

We have already outlined for you the entire GET request.

Each endpoint (except for GET) should be filled out to the best of your ability after the section that states **Your logic goes here**.

Keep in mind that the "database" in this case is just a `.json` file (`database.json`). This file should retain the state of the database when making updates. For example, if I run the `post` command, a new entry should be added to the `database.json` file. This "write out" should be handled by you as the developer.

### Example Requests

You can find an example set of requests in the `sandbox` file. Feel free to use this file in your testing throughout the development process. This file will not be used in your evaluation, so make as many changes to it as you see fit.

### Requirements

#### Submitting a response in Python

In order to run this code it is required that you have Python 3.6 or above installed on your computer.

Before running the code ensure that you have the correct requirements by following these commands:

`cd intern-tech-interview/python`
`pip install -r requirements.txt`

To run the code, you can type `python sandbox.py`.

#### Submitting a response in Typescript

In order to run this code it is required that you have Node installed on your computer.

To setup the project, run the following commands:

`cd intern-tech-interview/typescript`
`npm i`

To run the code, you can type `ts-node sandbox.ts`.


### Running tests

We have provided to you a few test cases to run against the code you write. These are outlined in `test_api`. If you are using Python, we have also included `pytest` as a requirement in `requirements.txt`. You can run tests by typing the command `pytest` in your terminal. If you are using Typescript, we included `jest` as a requirement in `package.json`. You can run tests by typing the command `npm test` in your terminal.

> Note: These tests **will** fail on the first run of the program. Once you have written your endpoints ensure that the tests pass before finalizing your code.

Please keep in mind that in the evaluation of the given code we will be running these tests to ensure that the code written works as expected.

Feel free to add your own tests as you see fit.
