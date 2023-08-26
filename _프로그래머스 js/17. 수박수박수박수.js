/*
* Title: 수박수박수박수
https://school.programmers.co.kr/learn/courses/30/lessons/12922
*/
function solution(n) {
  let val = '수박'.repeat(Math.floor(n / 2));

  if (n % 2 === 1) {
    val += '수';
  }

  return val;
}

// "수박수"
console.log(solution(3));
