#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
const vals = Object.values(dict);
const set = [...new Set(vals)];

for (const item of set) {
  newDict[item] = [];
}

for (const val in dict) {
  for (const key in newDict) {
    if (dict[val] === parseInt(key)) {
      newDict[key].push(val);
    }
  }
}
console.log(newDict);
