#!/usr/bin/node
const numArg = process.argv.length;
if (numArg === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
