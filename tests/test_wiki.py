# -*- coding: utf-8 -*-

import pytest
import sys

sys.path.append("src/answerquestionswithfacts")
import wiki
from service.qualifier import find_similarity
from service.preprocess import check_answers_and_get_answer_sentence_matches, check_questions_and_get_question_tokens


"""         ********* Input 1 **********     """
paragraph1 = "Zebras are several species of African equids (horse family) united by their distinctive black and white stripes. Their stripes come in different patterns, unique to each individual. They are generally social animals that live in small harems to large herds. Unlike their closest relatives, horses and donkeys, zebras have never been truly domesticated. There are three species of zebras: the plains zebra, the Grévy's zebra and the mountain zebra. The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more horse-like. All three belong to the genus Equus, along with other living equids. The unique stripes of zebras make them one of the animals most familiar to people. They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills. However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. Grévy's zebra and the mountain zebra are endangered. While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century – though there is currently a plan, called the Quagga Project, that aims to breed zebras that are phenotypically similar to the quagga in a process called breeding back."
questions1 = "Which Zebras are endangered? \
\n What is the aim of the Quagga Project? \
\n Which animals are some of their closest relatives? \
\n Which are the three species of zebras? \
\n Which subgenus do the plains zebra and the mountain zebra belong to?"
answers1 = "subgenus Hippotigris;the plains zebra, the Grévy's zebra and the mountain zebra;horses and donkeys;aims to breed zebras that are phenotypically similar to the quagga;Grévy's zebra and the mountain zebra"

correct_answers1 = "Grévy's zebra and the mountain zebra;aims to breed zebras that are phenotypically similar to the quagga;horses and donkeys;the plains zebra, the Grévy's zebra and the mountain zebra;subgenus Hippotigris"


"""         ********* Input 2 **********     """
paragraph2 = "Welsh national identity emerged among the Celtic Britons after the Roman withdrawal from Britain in the 5th century, and Wales is regarded as one of the modern Celtic nations. Llywelyn ap Gruffydd's death in 1282 marked the completion of Edward I of England's conquest of Wales, though Owain GlyndÅµr briefly restored independence to what was to become modern Wales, in the early 15th century. The whole of Wales was annexed by England and incorporated within the English legal system, under the Laws in Wales Acts 1535â€“1542. Distinctive Welsh politics developed in the 19th century. Welsh Liberalism, exemplified in the early 20th century by Lloyd George, was displaced by the growth of socialism and the Labour Party. Welsh national feeling grew over the century; Plaid Cymru was formed in 1925 and the Welsh Language Society in 1962. Established under the Government of Wales Act 1998, the National Assembly for Wales holds responsibility for a range of devolved policy matters. At the dawn of the Industrial Revolution, development of the mining and metallurgical industries transformed the country from an agricultural society into an industrial nation; the South Wales coalfield's exploitation caused a rapid expansion of Wales' population. Two-thirds of the population live in south Wales, mainly in and around Cardiff (the capital), Swansea and Newport, and in the nearby valleys. Now that the country's traditional extractive and heavy industries have either gone or are in decline, Wales' economy depends on the public sector, light and service industries and tourism. Wales' 2010 Gross Value Added (GVA) was Â£45.5 billion (Â£15,145 per head); 74.0 per cent of the average for the UK total, the lowest GVA per head in Britain."
questions2 = "When did the Welsh national identity emerge among the Celtic Britons? \
\n What was Welsh Liberalism displaced by? \
\n How much of the population lives in south Wales? \
\n What does Wales' economy now depend on? \
\n When was Plaid Cymru formed?"
answers2 = "Two-thirds;after the Roman withdrawal from Britain in the 5th century;the growth of socialism and the Labour Party;1925;the public sector, light and service industries and tourism"

correct_answers2 = "after the Roman withdrawal from Britain in the 5th century;the growth of socialism and the Labour Party;Two-thirds;the public sector, light and service industries and tourism;1925"

"""         ********* Input 3 **********     """
wrong_question = "What is this"


def test_answer_validation():
    sentense_list = ["HDDs are a type of non-volatile storage, retaining stored data even when powered off.", "The primary characteristics of an HDD are its capacity and performance."]
    answer_list = ["capacity and performance", "non-volatile storage"]

    answer_check = [('non-volatile storage', ['HDDs', 'type', 'non-volatile', 'storage,', 'retaining', 'stored', 'data', 'even', 'powered', 'off.']), ('capacity and performance', ['The', 'primary', 'characteristics', 'HDD', 'capacity', 'performance.'])]
    assert check_answers_and_get_answer_sentence_matches(sentense_list, answer_list) == answer_check

def test_question_validation():
    questions = ["What type of storage is HHDs?", "Whare are the primary characteristics of an HDD?"]

    answer_check = [['What', 'type', 'storage', 'HHDs?'],['Whare', 'primary', 'characteristics', 'HDD?']]
    assert check_questions_and_get_question_tokens(questions) == answer_check

def test_find_similarity():
    answer_matches = [('non-volatile storage', ['HDDs', 'type', 'non-volatile', 'storage,', 'retaining', 'stored', 'data', 'even', 'powered', 'off.']), ('capacity and performance', ['The', 'primary', 'characteristics', 'HDD', 'capacity', 'performance.'])]
    question_token = [['What', 'type', 'storage', 'HHDs?'],['Whare', 'primary', 'characteristics', 'HDD?']]

    answer_check = ["non-volatile storage", "capacity and performance"]
    assert find_similarity(answer_matches, question_token) == answer_check

def test_solve_puzzle():
    assert wiki.solve_puzzle(paragraph1, questions1, answers1) == correct_answers1
    assert wiki.solve_puzzle(paragraph2, questions2, answers2) == correct_answers2


def test_wrong_answer_input():
    with pytest.raises(Exception) as e:
        assert wiki.solve_puzzle(paragraph2, questions2, answers1)
    assert (
        str(e.value)
        == "Basic Check on the input fact failed: Answers aren't part of the Paragraph. Please re-check"
    )


def test_wrong_question_input():
    with pytest.raises(Exception) as e:
        assert wiki.solve_puzzle(paragraph2, wrong_question, answers2)
    assert (
        str(e.value)
        == "Basic Check on Question pattern failed: Ideally any question would have atleast one word with Subject or Object. Please re-check"
    )
