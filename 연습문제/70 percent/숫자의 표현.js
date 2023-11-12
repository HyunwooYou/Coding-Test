/*
#소수점내림
Math.floor(7.8)
 */
function solution(n) {
    let cnt = 0;

    for (let i = 1; i <= n / 2; i++) {
        let sum = 0;

        for (let j = i; j <= n; j++) {
            sum += j;

            if (sum > n) {
                break;
            }
            if (sum === n) {
                cnt += 1;
                break;
            }
        }
    }

    return cnt + 1;
}

const n = 15;
console.log(solution(n));
