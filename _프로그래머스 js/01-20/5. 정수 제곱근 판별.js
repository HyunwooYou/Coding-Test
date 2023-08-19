/*
* Title: 정수 제곱근 판별
https://school.programmers.co.kr/learn/courses/30/lessons/12934
*/
const solution = (num) => {
  let answer = 0;
  const sqrt = Math.sqrt(num)
  
  if (Number.isInteger(sqrt)) {
    answer = (sqrt + 1) ** 2
  } else {
    answer = -1
  }
  
  return answer;
}

// 144
console.log(solution(121))
// -1
console.log(solution(3))