/*
* Title: 나누어 떨어지는 숫자 배열
https://school.programmers.co.kr/learn/courses/30/lessons/12910
*/
const solution = (array, divisor) => {
  let ls = [];

  for (let i = 0; i < array.length; i++) {
    const cur = array[i];

    if (cur % divisor === 0) {
      ls.push(cur);
    }
  }
  if (ls.length === 0) {
    ls.push(-1);
  }

  return ls;
};

// [5, 10]
console.log(solution([5, 9, 7, 10], 5));
