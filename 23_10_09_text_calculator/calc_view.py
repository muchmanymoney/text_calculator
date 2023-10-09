


class CalcView:

    def show_result(self, _formula, result):
        print(f"{_formula} 식의 결과값은 {result} 입니다.")

    @staticmethod
    def show_error_message(e):
        print(f"식 입력 에러 발생: {e}")
