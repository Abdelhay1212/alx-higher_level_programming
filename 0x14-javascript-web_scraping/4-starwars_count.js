#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');

const URL = process.argv[2];

request.get(URL, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body).results;
    let counter = 0;

    for (let i = 0; i < data.length; i++) {
      const characters = data[i].characters;

      for (const char of characters) {
        if (char.endsWith('/18/')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
