#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurece = 0;
  for (const ele of list) {
    if (ele === searchElement) {
      occurece++;
    }
  }
  return occurece;
};
