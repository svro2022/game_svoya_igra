from data import questions


def _draw_field_category(category_title, questions_in_category):
    """
    Отрисовывает вопросы в категории в формате 100 200 300
    :param questions_in_category:
    :return:
    """

    result = category_title.ljust(15)

    for price, question_data in questions_in_category.items():
        if question_data['asked']:
            result += " " * 5
        else:
            result += price.ljust(5)

    return result


def draw_field(questions):
    """
    Отрисовывает игровое поле в формате
    CAT_1       100  200  300
    CAT_2       100  200  300
    """
    result = ""

    for key, value in questions.items():
        # Делегируем отрисовку ряда функции
        result += _draw_field_category(key, value)
        result += "\n\n"

    return result


def parse_input(user_input, questions) -> tuple | None:
    """
    Проверяет есть ли на игровом поле такой вопрос и можем ли мы его использовать
    :param user_input:
    :param questions:
    :return:
    """

    if user_input.count(" ") != 1:
        return None

    category, price = user_input.title().strip().split(" ")

    if category not in questions:
        return None

    if not price.isdigit():
        return None

    category_questions = questions[category]

    if price not in category_questions:
        return None

    if category_questions[price]["asked"]:
        return None

    return category, price


def count_rounds_of_questions(questions):
    rounds = 0
    for category in questions.values():
        rounds += len(category)
    return rounds


def get_question(category, price):
    """
    Возвращает вопрос по категории и цене
    :param category: строка категории
    :param price: строка ценф
    :return: текст вопроса
    """

    question_data = questions[category][price]
    return question_data["question"]


def check_answer(category, price, answer, questions):
    """
    Проверяет правильность ответа по категории, цене и ответу
    :param category: строка категории
    :param price: строка цены
    :param answer: строка ответа
    :param questions: данные оюб игровом поле
    :return:
    """

    question_data = questions[category][price]

    return answer.lower() == question_data["answer"].lower()


def mark_question_done(category, price,questions):
    """
    :param category: строка категории
    :param price: строка цены
    :param questions: игровое поле
    :return: None
    """

    questions[category][price]["asked"] = True


# print(check_answer("Животные", "100", "собака", questions))
