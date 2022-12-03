#!/usr/bin/node
const n = require('./100-data').list;
console.log(n);
console.log(n.map((x, y) => x * y));
