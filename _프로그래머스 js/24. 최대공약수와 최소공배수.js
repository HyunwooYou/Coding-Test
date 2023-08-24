/*
* Title: 최대공약수와 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12940
*/
const solution = (n, m) => {
  const greatest_common_divisor = (x, y) => {
    let _x = x;
    let _y = y;

    while (_y) {
      const tmp_x = _x;
      const tmp_y = _y;
      _x = tmp_y;
      _y = tmp_x % tmp_y;
    }

    return _x;
  };

  const least_common_multiple = (x, y) => {
    return (x * y) / greatest_common_divisor(x, y);
  };

  const num_1 = greatest_common_divisor(n, m);
  const num_2 = least_common_multiple(n, m);

  return [num_1, num_2];
};

// [3, 12]
console.log(solution(3, 12));

// [1, 10]
console.log(solution(2, 5));
