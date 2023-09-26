#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
const p = args[3];
const URL = args[2];

request(URL, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(p, res.body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
