/*
* Title: 피보나치 수
https://school.programmers.co.kr/learn/courses/30/lessons/12945
*/
const solution = (n) => {
  let ls = [0, 1];

  for (let i = 2; i < n + 1; i++) {
    const fibo = ls[i - 1] + ls[i - 2];
    ls.push(fibo % 1234567);
  }

  return ls.pop();
};

// 5
console.log(solution(5));

// 55
console.log(solution(10));
