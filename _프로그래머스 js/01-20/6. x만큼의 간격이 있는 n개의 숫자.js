/*
* Title: x만큼의 간격이 있는 n개의 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12954
*/
const solution = (x, n) => {
    let ls = [];

    for (let i = 1; i < n + 1; i ++) {
        ls.push(i * x);
    }

    return ls;
}

// [2,4,6,8,10]
console.log(solution(2, 5))

// [-4, -8]
console.log(solution(-4, 2))