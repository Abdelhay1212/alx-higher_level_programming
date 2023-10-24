#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');

const URL = process.argv[2];
const target = "https://swapi-api.alx-tools.com/api/people/18/";

request.get(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const data = JSON.parse(body).results;
  const characters = data[0]['characters'];
  let counter = 0;

  for (char of characters) {
    if (char === target) {
      counter++;
    }
  }

  console.log(counter);
});
