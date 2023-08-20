/*
* Title: 핸드폰 번호 가리기
https://school.programmers.co.kr/learn/courses/30/lessons/12948
*/
const solution = (phone_number) => {
  const len = phone_number.length;
  const head = Array(len - 4).fill('*');
  const tailor = phone_number.substring(len - 4);

  return `${head.join('')}${tailor}`;
};

// "*******4444"
console.log(solution('01033334444'));
