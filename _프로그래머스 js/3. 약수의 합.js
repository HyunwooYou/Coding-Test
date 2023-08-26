/*
* Title: 약수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/12928
*/
function solution(num) {
  let answer = 0;

  for (let i = 1; i <= num; i++) {
    if (num % i === 0) {
      answer += i;
    }
  }

  return answer;
}

console.log(solution(10));
