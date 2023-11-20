function solution(n, a, b) {
    let ls = new Array(n).fill(0);
    let round = 0;

    ls[a - 1] = 1;
    ls[b - 1] = 1;

    while (true) {
        round++;
        let newLs = [];

        for (let i = 0; i < ls.length; i += 2) {
            newLs.push(ls[i] + ls[i + 1]);
        }

        if (newLs.includes(2)) {
            break;
        }

        ls = newLs;
    }

    return round;
}

n = 8;
a = 4;
b = 7;

console.log(solution(n, a, b));
