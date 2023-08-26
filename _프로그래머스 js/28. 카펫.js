/*
* Title: 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/428421111
*/
function solution(brown, yellow) {
  let ans_i = 3;
  let ans_j = 3;

  for (let i = yellow; i >= 1; i--) {
    if (yellow % i !== 0) {
      continue;
    }

    ans_i = i;
    ans_j = yellow / i;

    if ((ans_i + 2) * 2 + ans_j * 2 === brown) {
      break;
    }
  }

  return [ans_i + 2, ans_j + 2];
}

// [4, 3]
console.log(solution(10, 2));

// [5, 4]
console.log(solution(14, 6));
