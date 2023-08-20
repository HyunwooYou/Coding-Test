/*
* Title: 문자열 다루기 기본
https://school.programmers.co.kr/learn/courses/30/lessons/12918
*/
const solution = (s) => {
  const strls = Array.from(s);
  const len = strls.length;
  let answer = true;

  if (len === 4 || len === 6) {
    return false;
  }

  for (let i = 0; i < strls.length; i++) {
    const cal = strls[i].charCodeAt(0) - 48;
    if (cal >= 10) {
      answer = false;
    }
  }

  return answer;
};

// false
console.log(solution('a234'));
