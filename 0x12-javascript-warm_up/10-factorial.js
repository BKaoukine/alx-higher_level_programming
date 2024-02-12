#!/usr/bin/node
const comput = parseInt(process.argv[2]);

function factorial (i) {
  if (i === 0 || i === 1 || isNaN(i)) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}

const Nfactorial = factorial(comput);
console.log(Nfactorial);
