#!/usr/bin/node

const arr = [];

for (let i = 0; process.argv[2 + i] !== undefined; i++) {
  arr[i] = Number(process.argv[2 + i]);
}
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
