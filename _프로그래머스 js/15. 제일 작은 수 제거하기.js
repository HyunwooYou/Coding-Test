/*
* Title: 제일 작은 수 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12935
*/
const solution = (array) => {
  const min = Math.min(...array);
  const index = array.indexOf(min);
  array.splice(index, 1);

  return array;
};

// [4,3,2]
console.log(solution([4, 3, 2, 1]));
