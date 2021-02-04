
from typing import List

def slice_queries(text: str):
    wildcard_f = 0
    wildcard_b = len(text)
    text_f = 0
    text_b = len(text)

    for i in range(len(text)):
        if text[i] == "?":
            wildcard_f = i
            break

    for i in range(len(text)):
        if text[::-1][i] == "?":
            wildcard_b = i
            break
    
    if wildcard_f == 0:
        text_f = wildcard_b
    elif wildcard_b == len(text):
        text_b = wildcard_f

    return (text_f, text_b)

def solution(words: List[str], queries: List[str]):
    answer: List[int] = []
    for query in queries:
        result = 0
        text_f, text_b = slice_queries(query)
        for word in words:
            if len(word) == len(query):
                continue
            if word[text_f:text_b] == query[text_f:text_b]:
                result += 1
        answer.append(result)

    return answer
