#!/usr/bin/node
const MyVar = process.argv[2];
let S = '';
if (isNaN(MyVar) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < MyVar; i++) {
    S += 'X';
  }
  for (let i = 0; i < MyVar; i++) {
    console.log(S);
  }
}
