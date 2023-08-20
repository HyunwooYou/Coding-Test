/*
* Title: 문자열 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12917
*/
const solution = (n) => {
  const strls = Array.from(n);
  strls.sort().reverse();

  return strls.join('');
};

// "gfedcbZ"
console.log(solution('Zbcdefg'));
