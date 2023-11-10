function solution(s) {
  const step1 = s.toLowerCase();
  const step2 = (str) => str.charAt(0).toUpperCase() + str.slice(1);
  const ls = step1.split(' ').map(step2);

  return ls.join(' ');
}

s = '3people unFollowed me';
console.log(solution(s));
