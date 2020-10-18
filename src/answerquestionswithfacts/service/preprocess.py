from .stopwords import stop_words, punctuations

# Check if Answer matches in Sentense and return matching pair
def _get_answer_matches(paragraph, answers):

    ans_distinct_count = set()
    answer_matches = []

    for sentense in paragraph:
        for answer in answers:
            if answer in sentense:
                answer_matches.append((answer, _removeStopWords(sentense.split())))
                ans_distinct_count.add(answer)

    return answer_matches, len(ans_distinct_count)


def check_answers_and_get_answer_sentence_matches(paragraph, answers):

    answer_matches, i = _get_answer_matches(paragraph, answers)

    if i == len(answers):
        return answer_matches
    else:
        raise ValueError(
            "Basic Check on the input fact failed: Answers aren't part of the Paragraph. Please re-check"
        )


# Check and Tokenize Questions
def check_questions_and_get_question_tokens(questions):
    return _get_question_token(questions)


def _check_words_in_question(question):
    question = _removeStopWords(question)
    if len(question) < 2:
        raise ValueError(
            "Basic Check on Question pattern failed: Ideally any question would have atleast one word with Subject or Object. Please re-check"
        )
    else:
        return question


def _get_question_token(questions):

    question_token = []
    i = 0

    while i < len(questions):
        temp_question_token = []
        for ques in filter(None, questions[i].split(" ")):  # Words in a question
            temp_question_token.append(ques)

        question_token.append(
            _check_words_in_question(_removeStopWords(temp_question_token))
        )

        i += 1

    return question_token


def _removeStopWords(text):
    keywords = []
    for t in text:
        if t in stop_words or t in punctuations:
            pass
        else:
            keywords.append(t.encode("ascii", errors="ignore").decode())
    return keywords
