#!/usr/bin/node

const fs = require('fs');
const data = process.argv[3];
const destination = process.argv[2];

fs.writeFile(destination, data, (err) => {
  if (err) {
    console.log(err);
  }
});
