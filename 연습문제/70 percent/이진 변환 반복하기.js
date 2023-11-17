/*
#console #가지런히 #일정하게 출력
console.log(`${s}\t${newStr}\t${len}`);

#이진 변환
const len = 10
const trans = len.toString(2);

#특정문자열 개수
const s = '101100';
const cnt = s.sp;lit('').filter((e) => e === '0').length;

#replace 정규식 #정규식
const newS = s.replace(/0/g, '');
 */

function solution(s) {
    let varObj = { str: '', len: 0 };
    let cntObj = { zero: 0, change: 0 };

    while (true) {
        if (varObj.str === '1') {
            break;
        }

        cntObj.zero += s.split('').filter((e) => e === '0').length;
        cntObj.change += 1;

        varObj.str = s.replace(/0/g, '');
        varObj.len = varObj.str.length;

        s = varObj.len.toString(2);
    }

    return [cntObj.change, cntObj.zero];
}

s = '110010101001';
console.log(solution(s));
