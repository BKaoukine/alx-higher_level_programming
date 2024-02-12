#!/usr/bin/node
const myint = parseInt(process.argv[2]);

if (isNaN(myint)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myint);
}
