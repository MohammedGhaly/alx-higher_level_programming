#!/usr/bin/node
const request = require('request');
const args = process.argv;
const URL = args[2];

request(URL, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const dic = {};
  const res = JSON.parse(response.body);
  res.forEach(element => {
    if (element.completed) {
      dic[element.userId] = (dic[element.userId] ?? 0) + 1;
    }
  });
  console.log(dic);
});
