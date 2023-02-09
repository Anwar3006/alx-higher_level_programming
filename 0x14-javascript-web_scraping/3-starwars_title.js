#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const Link = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(Link, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
