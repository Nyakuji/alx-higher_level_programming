#!/usr/bin/node
const numOfArguments = process.argv.length - 2;

if (numOfArguments === 0){
	console.log('No arguments');
} else if (numOfArguments === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
