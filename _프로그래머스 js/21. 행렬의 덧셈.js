/*
* Title: 행렬의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/12950
*/
const solution = (arr1, arr2) => {
  const row_len = arr1.length;
  const col_len = arr1[0].length;
  const ls = [];

  for (let i = 0; i < row_len; i++) {
    let new_col_ls = [];

    for (let j = 0; j < col_len; j++) {
      new_col_ls.push(arr1[i][j] + arr2[i][j]);
    }

    ls.push(new_col_ls);
  }

  return ls;
};

// [[4,6],[7,9]]
console.log(
  solution(
    [
      [1, 2, 5],
      [2, 3, 1],
    ],
    [
      [3, 4, 2],
      [5, 6, 3],
    ],
  ),
);
