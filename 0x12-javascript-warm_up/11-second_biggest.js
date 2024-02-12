#!/usr/bin/node
const numarg = process.argv.length;

if (numarg <= 3) {
  console.log(0);
} else {
  let maxnum;
  let i = 0;
  let j = 1;
  while (i < numarg - 1) {
    if (parseInt(process.argv[i]) > parseInt(process.argv[j])) {
      maxnum = parseInt(process.argv[i]);
    } else {
      maxnum = parseInt(process.argv[j]);
    }
    i++;
    j++;
  }

  console.log(maxnum);
}
