#!/usr/bin/node
const { argv } = require('node:process');
const numOfArguments = argv.length - 2;
if (numOfArguments === 0) {
  console.log("No argument");
} else if (numOfArguments === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
