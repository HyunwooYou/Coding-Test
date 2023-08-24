/*
* Title: JadenCase 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
*/
const solution = (s) => {
  s = s.split(' ');
  let ls = [];

  for (let i = 0; i < s.length; i++) {
    let new_str = '';
    const cur_1 = s[i];

    for (let j = 0; j < cur_1.length; j++) {
      const cur_2 = cur_1[j];
      const cal_1 = cur_2.charCodeAt(0) - 48;

      if (0 < cal_1 && cal_1 <= 9) {
        new_str += cur_2;
      } else if (j === 0) {
        new_str += cur_2.toUpperCase();
      } else {
        new_str += cur_2.toLowerCase();
      }
    }

    ls.push(new_str);
  }

  return ls.join(' ');
};

// "3people Unfollowed Me"
console.log(solution('3people unFollowed me'));

// "For The Last Week"
console.log(solution('for the last week'));
