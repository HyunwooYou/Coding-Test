function solution(n) {
    let cnt = 0;

    while (true) {
        if (n % 2 === 0) {
            n /= 2;
        } else {
            n--;
            n /= 2;
            cnt++;
        }

        if (n === 0) {
            break;
        }
    }

    return cnt;
}

n = 5000;
console.log(solution(n));
