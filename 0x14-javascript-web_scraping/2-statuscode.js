#!/usr/bin/node

const request = require('request');
url_link = process.argv[2];

request(url_link, (err, response, body) => {
    if (err) { 
        console.log(err);
    }
    else {
        console.log("code: " + response.statusCode);
    }
});
