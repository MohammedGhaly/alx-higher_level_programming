#!/usr/bin/node
const request = require('request');
const args = process.argv;
const URL = args[2];
request(URL, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  let n = 0;
  const results = JSON.parse(res.body).results;
  results.forEach(element => {
    const condition = element.characters.find((ch) => {
      return ch.match(/18/);
    });
    if (condition !== undefined) {
      n++;
    }
  });
  console.log(n);
});
