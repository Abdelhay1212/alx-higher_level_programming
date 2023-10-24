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

  for (let i = 0; i < data.length; i++) {
    const characters = data[i]['characters'];
    let counter = 0;

    for (char of characters) {
      if (char === target) {
        counter++;
      }
    }
  }

  console.log(counter);
});
