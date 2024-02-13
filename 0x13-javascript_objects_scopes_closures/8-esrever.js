#!/usr/bin/node

exports.esrever = function (list) {
  let listlenght = list.length - 1;
  let i = 0;
  while (i < listlenght) {
    const tmp = list[i];
    list[i] = list[listlenght];
    list[listlenght] = tmp;

    i++;
    listlenght--;
  }

  return list;
};
