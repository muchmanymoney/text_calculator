from calc_controller_2 import CalcController


class CalcApplication:
    def __init__(self):
        self.__ctrl = CalcController()

    def execute(self):
        _formula = self.__ctrl.insert_formula()    #문자열 수식을 입력 받습니다.
        result = self.__ctrl.calculate_string_formula(_formula)   # 문자열 계산 결과를 얻습니다.
        self.__ctrl.display_result(_formula, result)   # 계산 결과 display


if __name__ == "__main__":
    CalcApplication().execute()


