#!/usr/bin/node
/* script that writes a string to a file */

const fs = require('fs');

const pathFile = process.argv[2];
const content = process.argv[3];

fs.writeFile(pathFile, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
