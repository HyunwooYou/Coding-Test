/*
* Title: 두 정수 사이의 합
https://school.programmers.co.kr/learn/courses/30/lessons/12912
*/
const solution = (a, b) => {
    const min = Math.min(a, b);
    const max = Math.max(a, b);
    let sum = 0;

    for (let n = min; n <= max; n ++) {
        sum += n;
    }

    return sum;
}

console.log(solution(5, 3))