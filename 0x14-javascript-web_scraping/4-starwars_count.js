#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');

const URL = process.argv[2];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  data = JSON.parse(body).get('results');
  console.log(data[0]['characters'][0]);
});
