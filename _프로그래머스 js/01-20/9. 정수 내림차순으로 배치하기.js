/*
* Title: 정수 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12933
*/
const solution = (n) => {
    const strls = Array.from(String(n), Number);
    strls.sort().reverse();

    return String(strls);
}

// 873211
console.log(solution(118372))