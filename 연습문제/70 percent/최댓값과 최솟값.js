function solution(s) {
    const ls = s.split(' ');
    const min = Math.min(...ls);
    const max = Math.max(...ls);

    return `${min} ${max}`;
}

s = '1 2 3 4';
console.log(solution(s));
// 1 2 3 4
