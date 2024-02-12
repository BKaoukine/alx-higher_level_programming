#!/usr/bin/node
const numarg = process.argv.length;

if (numarg <= 3) {
  console.log(0);
} else {
  let maxnum = parseInt(process.argv[2]);
  let i = 2;
  while (i < numarg) {
    if (maxnum < parseInt(process.argv[i])) {
      maxnum = parseInt(process.argv[i]);
    }
    i++;
  }

  console.log(maxnum);
}
