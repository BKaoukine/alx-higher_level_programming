#!/usr/bin/node
const sqSize = parseInt(process.argv[2]);
if (isNaN(sqSize)) {
  console.log('Missing size');
}

for (let i = 0; i < sqSize; i++) {
  let xstr = '';
  for (let j = 0; j < sqSize; j++) {
    xstr += 'X';
  }
  console.log(xstr);
}
