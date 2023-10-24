#!/usr/bin/node
/*script that prints the title of a Star
Wars movie where the episode number matches a given integer.*/

const request = require('request');

ID = process.argv[2];
URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request.get(URL).on('response', (response) => {
  const jsonObject = JSON.parse(response);
  console.log(jsonObject['title']);
});
