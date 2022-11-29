#!/usr/bin/node
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
