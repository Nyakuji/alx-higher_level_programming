#!/usr/bin/node
exports.esrever = function (list) {
  const newEver = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newEver.push(list[i]);
  }
  return newEver;
};
