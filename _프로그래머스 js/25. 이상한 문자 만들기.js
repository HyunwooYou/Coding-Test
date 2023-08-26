/*
* Title: 이상한 문자 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12930
*/
function solution(s) {
  let answer = [];
  const split_s = s.split(' ');

  for (let i = 0; i < split_s.length; i++) {
    const cur_1 = split_s[i];
    const str_ls = Array.from(cur_1);

    for (let j = 0; j < str_ls.length; j++) {
      const cur_2 = str_ls[j];

      if (j % 2 === 0) {
        str_ls[j] = cur_2.toUpperCase();
      } else {
        str_ls[j] = cur_2.toLowerCase();
      }
    }

    answer.push(str_ls.join(''));
  }

  return answer.join(' ');
}

// "TrY HeLlO WoRlD"
console.log(solution('try hello world'));
