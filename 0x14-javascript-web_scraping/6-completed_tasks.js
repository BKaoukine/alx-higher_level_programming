#!/usr/bin/node

const request = require('request');
const urlToRequest = process.argv[2];
const arrayofusers = {};

request.get(urlToRequest, function (err, response, body) {
  if (err) {
    console.error(`Error: ${err.message}`);
  }
  const data = JSON.parse(body);

  for (const obj of data) {
    if (obj.completed === true) {
      if (arrayofusers[obj.userId]) {
        arrayofusers[obj.userId] += 1;
      } else {
        arrayofusers[obj.userId] = 1;
      }
    }
  }

  console.log(arrayofusers);
});
