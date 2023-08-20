/*
* Title: 하샤드 수
https://school.programmers.co.kr/learn/courses/30/lessons/12947
*/

const solution = (x) => {
    const arr = Array.from(String(x), Number);
    const sum = arr.reduce((a, b) => a + b, 0);
    let answer = true;

    if (x % sum !== 0) {
        answer = false;
    }

    return answer;
}

// true
console.log(solution(10))

// false
console.log(solution(13))