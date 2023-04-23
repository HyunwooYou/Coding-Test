"""
* Title: 단어 변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""
def solution(begin, target, words):
    answer = 0
    return answer

begin = 'hit'
target = 'cog'
"""
- target 단어가 있는지 확인
 > 없으면 바로 0 return 
-   

begin과 한 글자만 차이는 단어를 바꾸자

"hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

hit 
hot     hot
dot     .   
dog     hog 
lot     .
dog     .
cog     cog 
"""
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))