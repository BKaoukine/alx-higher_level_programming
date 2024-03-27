#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request.get(apiUrl, function (err, response, body) {
  if (err) {
    console.error(`Error: ${err.message}`);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.results.length; i++) {
      for (let j = 0; j < data.results[i].characters.length; j++) {
        if (data.results[i].characters[j] === charId) {
          count += 1;
        }
      }
    }
    console.log(`${count}`);
  }
});
