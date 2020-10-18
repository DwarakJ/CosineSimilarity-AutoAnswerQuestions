from IComprehension import Comprehension
from service.preprocess import (
    check_answers_and_get_answer_sentence_matches,
    check_questions_and_get_question_tokens,
    _removeStopWords
)
from service.qualifier import find_similarity,find_question_similarity


class wiki(Comprehension):
    def __init__(self, para, ques, ans):
        self.paragraph = para.split(".")
        self.questions = [i for i in ques.split("\n")]
        self.answers = [j for j in ans.split(";")]

    def validate_input(self) -> bool:

        self.answer_matches = check_answers_and_get_answer_sentence_matches(
            self.paragraph, self.answers
        )
        self.question_tokens = check_questions_and_get_question_tokens(self.questions)

        if self.answer_matches and self.question_tokens:
            return True
        else:
            return False

    def getQuestionMaches(self):
        
        sentenses = []
        for sentense in self.paragraph:
            sentenses.append(_removeStopWords(str(sentense).split()))
        
        #print(sentenses)
        
        self.question_tokens = check_questions_and_get_question_tokens(self.questions)

        self.result = find_question_similarity(sentenses, self.question_tokens)

    def process_data(self) -> list:
        self.result = find_question_similarity(self.answer_matches, self.question_tokens)

    def get_results(self):
        return ";".join(self.result)


def solve_puzzle(paragraphs, questions, answers):
    w = wiki(paragraphs, questions, answers)

    w.getQuestionMaches()

    #w.get_results()

"""     if w.validate_input():
        w.process_data()

        result = w.get_results()

        return result """

paragraph1 = "Zebras are several species of African equids (horse family) united by their distinctive black and white stripes. Their stripes come in different patterns, unique to each individual. They are generally social animals that live in small harems to large herds. Unlike their closest relatives, horses and donkeys, zebras have never been truly domesticated. There are three species of zebras: the plains zebra, the Grévy's zebra and the mountain zebra. The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more horse-like. All three belong to the genus Equus, along with other living equids. The unique stripes of zebras make them one of the animals most familiar to people. They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills. However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. Grévy's zebra and the mountain zebra are endangered. While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century – though there is currently a plan, called the Quagga Project, that aims to breed zebras that are phenotypically similar to the quagga in a process called breeding back."
questions1 = "Which Zebras are endangered? \
\n What is the aim of the Quagga Project? \
\n Which animals are some of their closest relatives? \
\n Which are the three species of zebras? \
\n Which subgenus do the plains zebra and the mountain zebra belong to?"
answers1 = "subgenus Hippotigris;the plains zebra, the Grévy's zebra and the mountain zebra;horses and donkeys;aims to breed zebras that are phenotypically similar to the quagga;Grévy's zebra and the mountain zebra"

correct_answers1 = "Grévy's zebra and the mountain zebra;aims to breed zebras that are phenotypically similar to the quagga;horses and donkeys;the plains zebra, the Grévy's zebra and the mountain zebra;subgenus Hippotigris"

solve_puzzle(paragraph1, questions1, answers1)