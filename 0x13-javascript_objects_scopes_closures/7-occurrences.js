#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const listlenght = list.length;
  let nofoccurences = 0;
  for (let i = 0; i < listlenght; i++) {
    if (list[i] === searchElement) {
      nofoccurences++;
    }
  }
  return nofoccurences;
};
