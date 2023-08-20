/*
* Title: 가운데 글자 가져오기
https://school.programmers.co.kr/learn/courses/30/lessons/12903
*/
const solution = (s) => {
  let answer = '';
  const len = s.length;

  if (len % 2 === 0) {
    answer = s[len / 2 - 1] + s[len / 2];
  } else {
    answer = s[parseInt(String(len / 2))];
  }

  return answer;
};

// "c"
console.log(solution('abcde'));

// "we"
console.log(solution('qwer'));
