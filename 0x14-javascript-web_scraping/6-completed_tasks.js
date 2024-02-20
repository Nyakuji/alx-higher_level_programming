#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completed = {};

    for (const todo of todos) {
      if (todo.completed === true) {
        if (todo.userId in completed) {
          completed[todo.userId]++;
        } else {
          completed[todo.userId] = 1;
        }
      }
    }

    console.log(completed);
  }
});
