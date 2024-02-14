#!/usr/bin/node
const importedlist = require('./100-data.js').list;

let i = 0;

const computedlist = importedlist.map((x) => x * i++);

console.log(importedlist);
console.log(computedlist);
