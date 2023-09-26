#!/usr/bin/node
const path = require('path');
const fs = require('fs');
const args = process.argv;

const p = path.join('.', args[2]);
fs.readFile(p, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
