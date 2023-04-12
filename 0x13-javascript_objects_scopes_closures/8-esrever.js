#!/usr/bin/node
exports.esrever = function (list) {
  let l = 0;
  let r = list.length - 1;
  for (l = 0; l < list.length / 2; l++, r--) {
    [list[l], list[r]] = [list[r], list[l]];
  }
  return list;
};
