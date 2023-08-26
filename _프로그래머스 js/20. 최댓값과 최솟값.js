/*
* Title: 최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939
*/
function solution(s) {
  const numls = s.split(' ').map((str) => Number(str));
  const min = Math.min(...numls);
  const max = Math.max(...numls);

  return `${min} ${max}`;
}

console.log(solution('1 2 3 4'));
