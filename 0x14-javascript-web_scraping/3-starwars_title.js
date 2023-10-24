#!/usr/bin/node
/*script that prints the title of a Star Wars movie where the episode number matches a given integer.*/

const request = require('request');

const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request.get(URL, (error, response, body) => {
  console.log(error || JSON.parse(body).title);
});
