/*
#charAt #lambda:map 앞자리 문자를 대문자로
str.charAt(0).toUpperCase() + str.slice(1);
 */
function solution(s) {
    const loweredStr = s.toLowerCase();

    const capitalizeFirstLetter = (str) => {
        return str.charAt(0).toUpperCase() + str.slice(1);
    };

    const ls = loweredStr.split(' ').map(capitalizeFirstLetter);

    return ls.join(' ');
}

s = '3people unFollowed me';
console.log(solution(s));
