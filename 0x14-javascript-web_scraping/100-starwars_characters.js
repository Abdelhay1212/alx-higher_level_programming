#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */

const request = require('request');

const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request.get(URL, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;

    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (!error) {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
});
