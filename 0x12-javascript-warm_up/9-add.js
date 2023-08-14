#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const n1 = Math.floor(Number(process.argv[2]));
const n2 = Math.floor(Number(process.argv[3]));

if (isNaN(n1) || isNaN(n2)) {
  console.log('NaN');
} else {
  add(n1, n2);
}
