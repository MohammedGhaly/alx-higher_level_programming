#!/usr/bin/node
const args = process.argv;
const URL = args[2];
const request = require('request');
request(URL, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', res.statusCode);
});
