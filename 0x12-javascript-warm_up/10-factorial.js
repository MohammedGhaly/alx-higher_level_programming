#!/usr/bin/node

function factorial (n) {
  if (n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

const num = Number(process.argv[2]);
if (isNaN(num) || num === 0) {
  console.log('1');
} else {
  console.log(factorial(num));
}

