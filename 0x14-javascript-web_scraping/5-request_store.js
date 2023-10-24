#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file */

const fs = require('fs');
const request = require('request');

const URL = process.argv[2];
const pathFile = process.argv[3];

request.get(URL, (error, response, body) => {
    if (!error) {
        fs.writeFile(pathFile, body, 'utf8', (err) => {
            if (err) {
                console.error(err);
            }
        });
    }
});
