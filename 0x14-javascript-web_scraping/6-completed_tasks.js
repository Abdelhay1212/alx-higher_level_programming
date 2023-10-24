#!/usr/bin/node
/* script that computes the number of tasks completed by user id */

const request = require('request');

const URL = process.argv[2];

request.get(URL, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const comletedTasks = {};

    todos.forEach(todo => {
      if (todo.completed && comletedTasks[todo.userId] === undefined) {
        comletedTasks[todo.userId] = 1;
      } else if (todo.completed) {
        comletedTasks[todo.userId] += 1;
      }
    });

    console.log(comletedTasks);
  }
});
