#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const filePath = process.argv[3];
const urlToRequest = process.argv[2];

request.get(urlToRequest, function (err, response, body) {
  if (err) {
    console.error(`Error: ${err.message}`);
  } else {
    fs.writeFile(filePath, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
