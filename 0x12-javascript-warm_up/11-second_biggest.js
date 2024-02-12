#!/usr/bin/node
const numarg = process.argv.length;

if (numarg <= 3) {
  console.log(0);
} else {
  let maxnum;
  let i = 0;
  let j = 1;
  while (i < numarg - 1) {
    if (process.argv[i] > process.argv[j]) {
      maxnum = process.argv[i];
    } else {
      maxnum = process.argv[j];
    }
    i++;
    j++;
  }

  console.log(maxnum);
}
