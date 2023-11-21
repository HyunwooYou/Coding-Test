/*
#최대공약수 #최소공배수 #유클리드호제법
// greatest common divisor
const gcd = (x, y) => {
    while (y !== 0) {
        let temp = y;
        y = x % y;
        x = temp;
    }
    return x;
}
// least common multiple
const lcm = (x, y) => {
    return (x * y) / gcd(x, y);
}
 */
function solution(arr) {
    // greatest common divisor
    const gcd = (x, y) => {
        while (y !== 0) {
            let temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    };

    // least common multiple
    const lcm = (x, y) => {
        return (x * y) / gcd(x, y);
    };

    for (let i = 1; i < arr.length; i++) {
        arr[i] = lcm(arr[i - 1], arr[i]);
    }

    return arr[arr.length - 1];
}

// 2, 3, 7
arr = [2, 6, 8, 14];
console.log(solution(arr));
