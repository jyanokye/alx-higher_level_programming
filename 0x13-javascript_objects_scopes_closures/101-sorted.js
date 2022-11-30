#!/usr/bin/node
const dict = require('./101-data').dict;
const n = {};
for (const i in dict) {
  if (n[dict[i]] === undefined) {
    n[dict[i]] = [];
  }
  n[dict[i]].push(i);
}
console.log(n);
