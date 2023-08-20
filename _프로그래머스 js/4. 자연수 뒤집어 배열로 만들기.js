/*
* Title: 자연수 뒤집어 배열로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12932
*/
const solution = (num) => {
  const ls = Array.from(String(num), Number);
  ls.reverse();
  return ls;
};

// [5, 4, 3, 2, 1]
console.log(solution(12345));
