/*
* Title: 시저 암호
https://school.programmers.co.kr/learn/courses/30/lessons/12926
*/
const solution = (s, n) => {
  let ls = [];

  const ord = (str) => str.charCodeAt(0);

  const is_alphabet = (ord_str) => {
    const lower_case = ord('a') <= ord_str && ord_str <= ord('z');
    const upper_case = ord('A') <= ord_str && ord_str <= ord('Z');

    return lower_case || upper_case;
  };

  for (let i = 0; i < s.length; i++) {
    const ord_cur = ord(s[i]);

    // space
    if (ord_cur === ord(' ')) {
      ls.push(' ');
      continue;
    }

    // not alphabet
    if (!is_alphabet(ord_cur)) {
      continue;
    }

    const ord_moved = ord_cur + n;

    if (is_alphabet(ord_moved)) {
      ls.push(String.fromCharCode(ord_moved));
    } else {
      const z_to_a = ord_moved - 26;
      ls.push(String.fromCharCode(z_to_a));
    }
  }

  return ls.join('');
};

// "BC"
console.log(solution('AB', 1));

// "e F d"
console.log(solution('a B z', 4));
