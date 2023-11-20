/*
#list 해당 인덱스의 요소 1개를 제거
let ls = [1, 2, 3, 4, 5];
let idxToRemove = 2;
ls.splice(idxToRemove, 1);

#list 첫 번째 요소 제거
ls.shift();

#list 첫 번째 요소를 제외한 새로운 배열 생성
ls.slice(1);
 */
function solution(people, limit) {
    let left = 0;
    let right = people.length - 1;
    let boats = 0;

    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            left++;
        }
        right--;
        boats++;
    }

    return boats;
}
people = [70, 50, 80, 50, 20];
// people = [70, 50, 80];
limit = 100;

console.log(solution(people, limit));
