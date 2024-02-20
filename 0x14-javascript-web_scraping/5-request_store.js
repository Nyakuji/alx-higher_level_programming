#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const FileName = process.argv[3];

request
  .get(apiUrl)
  .pipe(fs.createWriteStream(FileName));
