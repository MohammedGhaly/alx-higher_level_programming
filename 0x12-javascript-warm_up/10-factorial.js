#!/usr/bin/node

const num = Number(process.argv[2]);
if (isNaN(num) || num === 0) {
  console.log('1');
} else {
  let fact = 1;
  for (let i = num; i > 0; i--) {
    fact = fact * i;
  }
  console.log(fact);
}
