function areBracketsBalanced(input) {
  const stack = [];
  const brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  };

  for (let i = 0; i < input.length; i++) {
    const char = input[i];

    if (brackets[char]) {
      // 여는 괄호인 경우 스택에 추가
      stack.push(char);
    } else {
      // 닫는 괄호인 경우 스택에서 가장 최근에 추가된 괄호를 꺼내와 짝이 맞는지 확인
      const lastBracket = stack.pop();
      if (brackets[lastBracket] !== char) {
        // 짝이 맞지 않으면 괄호가 불균형한 것으로 판단
        return false;
      }
    }
  }

  // 모든 괄호가 짝이 맞을 때만 스택이 비어있을 것임
  return stack.length === 0;
}

// 테스트
console.log(areBracketsBalanced('()')); // true
console.log(areBracketsBalanced('{[()]}')); // true
console.log(areBracketsBalanced('{[(])}')); // false
console.log(areBracketsBalanced('([)]')); // false
