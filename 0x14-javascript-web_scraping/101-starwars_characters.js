#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */

const request = require('request');

const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

async function makeRequest(URL) {
  return new Promise((resolve) => {
    request.get(URL, (error, response, body) => {
      if (!error) {
        resolve(body);
      }
    });
  });
}

async function getCharacters() {
  const data = await makeRequest(URL);
  const characters = JSON.parse(data).characters;

  for (const character of characters) {
    const data = await makeRequest(character);
    const name = JSON.parse(data).name;
    console.log(name);
  }
}

getCharacters();
