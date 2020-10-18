import math
import re
from collections import Counter


def find_similarity(answer_matches, question_token):
    result = []
    #print(answer_matches)
    for question in question_token:
        temp = []
        for answer_pair in answer_matches:
            temp.append((answer_pair[0], _get_result(answer_pair[1], question)))

        temp.sort(key=lambda x: x[1], reverse=True)

        #print(temp)
        result.append(temp[0][0])
    
    return result

def find_question_similarity(answer_matches, question_token):
    result = []
    #print(answer_matches)
    for question in question_token:
        #print(question)
        temp = []
        for answer_pair in answer_matches:
            temp.append((answer_pair, _get_result(answer_pair, question)))

        temp.sort(key=lambda x: x[1], reverse=True)

        #print(temp)
        result.append(temp[0][0])

        #print(temp)
    print(result)
    return result

def _get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def _get_eucleadean(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    
    temp = [(vec1[x] - vec2[x]**2) for x in intersection]
    print(vec1)
    print(vec2)
    print(intersection)
    print(temp)
    return math.sqrt(sum([(float(vec1[x]) - vec2[x])**2 for x in intersection]))

#Which subgenus do the plains zebra and the mountain zebra belong to?

     #return np.sqrt(np.sum((x - y) ** 2))


def _text_to_vector(text):
    word = re.compile(r"\w+")
    words = word.findall(" ".join(text))
    return Counter(words)


def _get_result(text1, text2):
    vector1 = _text_to_vector(text1)
    vector2 = _text_to_vector(text2)

    cosine_result = _get_cosine(vector1, vector2)
    return cosine_result
