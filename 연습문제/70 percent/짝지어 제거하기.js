/*
#pop()
const stack = []
stack.pop() / stack[-1] => undefeind 값으로 보여짐
 */
function solution(s) {
    const stack = [];

    for (const str of s) {
        stack.push(str);

        if (stack[stack.length - 1] === stack[stack.length - 2]) {
            stack.pop();
            stack.pop();
        }
    }

    return stack.length === 0 ? 1 : 0;
}

s = 'baabaa';
// s = 'cdcd';
console.log(solution(s));
