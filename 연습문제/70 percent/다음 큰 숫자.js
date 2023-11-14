function solution(n) {
    const getOneCnt = (num) => {
        const convertToBinary = num.toString(2);
        return convertToBinary.split('').filter((e) => e === '1').length;
    };

    let plus = 0;
    let oneCnt = {
        n: getOneCnt(n),
        current: 0,
    };
    let answer = 0;

    while (true) {
        plus += 1;
        const newNum = n + plus;
        oneCnt.current = getOneCnt(newNum);

        if (oneCnt.n === oneCnt.current) {
            answer = newNum;
            break;
        }
    }

    return answer;
}

n = 78;
console.log(solution(n));
