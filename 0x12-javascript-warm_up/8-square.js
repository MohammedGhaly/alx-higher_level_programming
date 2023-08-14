#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let s = '';
  for (let i = 0; i < num; i++) {
    s += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(s);
  }
}
