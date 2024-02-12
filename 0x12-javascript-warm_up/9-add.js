#!/usr/bin/node
function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  const sum = a + b;
  console.log(sum);
}

add(process.argv[2], process.argv[3]);
