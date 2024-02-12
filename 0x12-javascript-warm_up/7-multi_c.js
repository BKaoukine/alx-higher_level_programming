#!/usr/bin/node
const nOccurences = parseInt(process.argv[2]);
if (isNaN(nOccurences)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < nOccurences; i++) {
  console.log('C is fun');
}
