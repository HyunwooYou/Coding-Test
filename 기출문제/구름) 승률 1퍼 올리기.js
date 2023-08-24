const calc = (num) => Math.floor(num * 100) / 100;

const m = 100;
const n = 80;
const originVal = calc(n / m);

let count = 0;

while (true) {
  count += 1;
  const curVal = calc((n + count) / (m + count));
  if (originVal !== curVal) break;
}

console.log(count);
