function solution(A, B) {
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);

    const multipliedLs = A.map((el, idx) => el * B[idx]);
    const sumOfLs = multipliedLs.reduce((acc, cur) => acc + cur, 0);

    return sumOfLs;
}

A = [1, 4, 2];
B = [5, 4, 4];
console.log(solution(A, B));
