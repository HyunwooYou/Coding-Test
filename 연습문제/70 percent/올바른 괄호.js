function solution(s) {
    const stack = [];
    const pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
    };

    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        if (pairs[char]) {
            stack.push(char);
        } else {
            const lastOpen = stack.pop();

            if (pairs[lastOpen] !== char) {
                return false;
            }
        }
    }

    return stack.length === 0;
}

s = '(())()';
console.log(solution(s));
