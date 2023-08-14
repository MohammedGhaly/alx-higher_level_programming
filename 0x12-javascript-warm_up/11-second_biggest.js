#!/usr/bin/node

const arr = [];

for (let i = 0; process.argv[2 + i] !== undefined; i++) {
  arr[i] = Number(process.argv[2 + i]);
}
if (arr.length === 0 || arr.length === 1) {
  console.log('0');
} else {
  arr.sort();
  console.log(arr[arr.length - 2]);
}
