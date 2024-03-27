#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(apiUrl, function (err, response, body) {
  if (err) {
    console.error(`Error: ${err.message}`);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
