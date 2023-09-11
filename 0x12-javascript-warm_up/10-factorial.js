#!/usr/bin/node
function factorial (num) {
  if (num === 0) {
    return (1);
  }
  return (factorial(num - 1) * num);
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  const fact = factorial(process.argv[2]);
  console.log(fact);
}
