/*
* Title: 콜라츠 추측
https://school.programmers.co.kr/learn/courses/30/lessons/12943
*/
const solution = (num) => {
    let val = 0;
    let answer = 0;

    while (true) {
        if (num === 1) {
            answer = val;
            break;
        }
        if (val === 500) {
            answer = -1;
            break;
        }
        val += 1;
        if (num % 2 === 0) {
            num = num / 2;
        } else {
            num = num * 3 + 1;
        }
    }

    return answer;
}

console.log(solution(6));
console.log(solution(16));