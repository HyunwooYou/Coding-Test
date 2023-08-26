/*
 * Title: 짝수와 홀수
 https://school.programmers.co.kr/learn/courses/30/lessons/12937
 */
function solution(num) {
  let answer = '';

  if (num % 2 === 0) {
    answer = 'Even';
  } else {
    answer = 'Odd';
  }
  return answer;
}

// Even
console.log(solution(10));
// Odd
console.log(solution(11));
