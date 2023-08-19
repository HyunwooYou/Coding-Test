/**
 * Title: 평균 구하기
 https://school.programmers.co.kr/learn/courses/30/lessons/12944
 */
const solution = (array) => {
  const sum = array.reduce((a, b) => a + b, 0);
  const count = array.length

  return sum / count;
}

// 4
console.log(solution([1, 2, 3, 4, 5, 6, 7]))