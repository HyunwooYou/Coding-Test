/*
#list 0으로 초기화 #array 0으로 초기화
const ls = new Array(10).fill(0);
 */
function solution(n) {
    let ls = [0, 1];

    for (let i = 2; i < n + 1; i++) {
        const fibo = ls[i - 1] + ls[i - 2];
        ls.push(fibo % 1234567);
    }

    return ls.pop();
}

n = 1500;
console.log(solution(n));
