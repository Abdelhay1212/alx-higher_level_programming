#!/usr/bin/node
/* script that display the status code of a GET request */

const request = require("request")

const URL = process.argv[2];

request.get(URL).on('response', (response) => {
	console.log(`code: ${response.statusCode}`);
});
