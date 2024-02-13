#!/usr/bin/node

let i = 0;

exports.logMe = function (item) {
  const indextoword = {};
  indextoword[item] = ++i;

  for (const word in indextoword) {
    console.log(indextoword[word] + ': ' + word);
  }
};
