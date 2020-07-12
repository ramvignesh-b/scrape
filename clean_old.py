import re

def get_question(text):
    questions = []
    ques = ''
    flag = start = 0
    for i in range (0, len(text)):
        if re.search('^Q.', text[i]) or re.search('^[0-9].', text[i]):
            start = 1
        if not start:
            continue
        if flag:
            if re.search('^Q.', text[i]):
                flag = 0
            else:
                continue
        if re.search('^Solution', text[i]):
            questions.append(ques)
            ques = ''
            flag = 1
            continue
        ques += text[i]
    return questions
        