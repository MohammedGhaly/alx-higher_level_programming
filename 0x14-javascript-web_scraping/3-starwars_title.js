#!/usr/bin/node
const args = process.argv;
const id = args[2];
const request = require('request');
const URL =
  `https://swapi-api.alx-tools.com/api/films/${id}/`;
request(URL, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(res.body).title);
});
