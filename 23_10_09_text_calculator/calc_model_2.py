import re

from calc_exception import IllegalArgumentException


class CalcModel:
    def __init__(self):
        pass

    @staticmethod
    def check_only_num(only_num):  # 식에서 연산기호를 제외한 부분이 숫자로만 되어있는지 확인
        for num in only_num:
            if num.isdigit() == False:
                raise IllegalArgumentException("[ERROR] 숫자와 연산기호 외에는 사용할 수 없습니다.")


    def calculate_text_formula(self, formula):
        only_num = re.split("[-,+,*,/]", formula)   # re.split함수를 이용해 식에서 연산기호(+-*/)를 제외한 숫자만 남긴다.
        only_operator = formula    # 입력받은 식에서 위의 코드의 결과를 제외시킨 연산자를 얻기 위해
        _result = only_num[0]  # 두번째 for문에서는 only_num[1]부터 들어가므로 only_num[0]을 미리 넣어준다.
        only_operator_2 = self.make_only_operator(only_num, only_operator)
        result_2 = self.compute_formula(_result, only_operator_2, only_num)
        return result_2

    @staticmethod
    def make_only_operator(only_num, only_operator):
        for num in only_num:
            """
            수식에서 숫자를 공백으로 대체하면 연산기호만 남는다
            """
            only_operator = only_operator.replace(num, '')
        return only_operator

    @staticmethod
    def compute_formula(_result, only_operator_2, only_num):
        """
        문자열의 순서대로 계산하는 메소드
        """
        for i in range(len(only_operator_2)):
            _result = str(eval(_result + only_operator_2[i] + only_num[i+1]))
        return _result



