#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response) {
  if (err) {
    console.error('error: ', response.message);
  } else {
    console.log('code: ', response.statusCode);
  }
});
