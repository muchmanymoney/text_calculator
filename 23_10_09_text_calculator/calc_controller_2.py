import re
from calc_model_2 import CalcModel
from calc_view import CalcView
from calc_exception import IllegalArgumentException

class CalcController:
    def __init__(self):
        self.__model = CalcModel()
        self.__view = CalcView()

    def insert_formula(self):
        while True:
            formula = input("수학식을 입력해주세요: ")
            # re.split함수를 이용해 식에서 연산기호(+-*/)를 제외한 부분만 남긴다.
            only_num = re.split("[-,+,*,/]", formula)
            try:
                """ 
                onlu_num의 요소들에 숫자가 아닌 문자나 특수문자가 있다면 ERROR를 발생시킨다.
                """
                self.__model.check_only_num(only_num)
                break
            except IllegalArgumentException as e:
                self.__view.show_error_message(e)
        return formula

    def calculate_string_formula(self, formula):   # 입력받은 수식을 계산합니다.
        return self.__model.calculate_text_formula(formula)

    def display_result(self, _formula, result):   # 계산 결과를 출력합니다.
        self.__view.show_result(_formula, result)
