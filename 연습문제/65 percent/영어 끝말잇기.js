/*

[ 가장 먼저 탈락하는 사람의 번호, 몇 번째 차례에서 탈락하지는지 ]
 */
function solution(n, words) {
    let period = 1;
    let number = -1;

    const isValidMatch = (prev, curr) => {
        return prev[prev.length - 1] === curr[0];
    };

    const isNonDuplicate = (words, str, index) => {
        const newLs = [...words].splice(0, index);
        return newLs.indexOf(str) === -1;
    };

    for (let i = 1; i < words.length; i++) {
        if ((i + 1) % n === 1) {
            period++;
        }
        const prev = words[i - 1];
        const curr = words[i];

        if (isValidMatch(prev, curr) && isNonDuplicate(words, curr, i)) {
            continue;
        } else {
            number = (i % n) + 1;
            break;
        }
    }

    if (number === -1) {
        return [0, 0];
    } else {
        return [number, period];
    }
}

n = 2;
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'];

// n = 3;
// words = [
//     'tank',
//     'kick',
//     'know',
//     'wheel',
//     'land',
//     'dream',
//     'mother',
//     'robot',
//     'tank',
// ];

console.log(solution(n, words));
