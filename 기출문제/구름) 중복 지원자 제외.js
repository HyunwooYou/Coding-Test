// 첫번째 인덱스 값인 5는 배열의 크기
const input = [5, 2, 3, 4, 3, 6];
const ls = input.slice(1);
const result = []

ls.sort();
ls.unshift(-1)
ls.push(-1)

for (let i = 1; i < ls.length - 1; i++) {
    const prev = ls[i - 1];
    const curr = ls[i]
    const next = ls[i + 1]

    if (prev !== curr && curr !== next) {
        result.push(curr)
    }
}

console.log(result);
