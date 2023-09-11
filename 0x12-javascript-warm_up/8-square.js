#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let str = '';
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    str += 'X';
  }

  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(str);
  }
}
