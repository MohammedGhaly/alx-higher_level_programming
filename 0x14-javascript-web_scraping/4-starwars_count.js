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
    if (element.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      n++;
    }
  });
  console.log(n);
});
