#!/usr/bin/node
if (process.argv.length < 3) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (max < parseInt(process.argv[i])) {
      max = parseInt(process.argv[i]);
    }
  }

  let sec_max = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (sec_max < parseInt(process.argv[i]) && parseInt(process.argv[i]) !== max) {
      sec_max = parseInt(process.argv[i]);
    }
  }

  console.log(sec_max);
}
