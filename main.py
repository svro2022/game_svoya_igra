import utils
from data import questions

rounds_total = utils.count_rounds_of_questions(questions)

answers_given = 0
answers_correct = 0
answers_incorrect = 0

while answers_given < rounds_total:

    print(utils.draw_field(questions))

    user_input_raw = input()

    user_input = utils.parse_input(user_input_raw, questions)

    if user_input is None:
        print("Такого вопроса нет или он использован, попробуйте еще раз!")
        continue

    category, price = user_input

    question_text = utils.get_question(category, price)

    print(question_text)

    user_attempt = input()

    if utils.check_answer(category, price, user_attempt, questions):
        print("Ответ верный")
    else:
        print("Ответ неверный")

    utils.mark_question_done(category, price, questions)



    #
    # if utils.check_answer(category, price, )
    #
    # # Отметить вопрос заданным
