#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (max < parseInt(process.argv[i])) {
      max = parseInt(process.argv[i]);
    }
  }

  let secMax = parseInt(process.argv[2]) === max
    ? parseInt(process.argv[3])
    : parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (secMax < parseInt(process.argv[i]) && parseInt(process.argv[i]) !== max) {
      secMax = parseInt(process.argv[i]);
    }
  }

  console.log(secMax);
}
