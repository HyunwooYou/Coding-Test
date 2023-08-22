/**
 100
 80
 */
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let count = 0;
rl.on('line', function (line) {
  count++;
  input.push(Number(line));

  if (count === 2) {
    rl.close();
  }
}).on('close', function () {
  console.log(input);
  process.exit();
});
