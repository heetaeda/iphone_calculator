import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
#import sympy as sp

# from_class = uic.loadUiType("/home/yoon/ws/PyQt/src/calculator_copy.ui")[0]
from_class = uic.loadUiType("../iphone_calculator/ui/calculator_copy.ui")[0]

# 화면 클래스 구상
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Calculator')

        self.is_init = True  # 현재 초기 상태인지 나타나는 변수
        self.operator_cnt = -1  # 연산자 버튼 누르는 횟수
        self.digit_result = '0'  # result_screen 에 나타나는 값
        self.equal_cnt = 0
        self.is_new_input = True  # 새로운 숫자 입력 여부
        self.is_last_input_operator = False  # 마지막 입력이 연산자인지 여부

        #self.digit_clear_flag = False
        #self.operator_clear_flag = False

        # 입력 된 계산식 저장하는 리스트
        self.calc_list = []

        # 버튼 색상 관련 번수
        self.operator_btn_color_change = """
                QPushButton {
                                background-color: white;  /*흰색 배경*/
                                border-radius: 25px;  /* 버튼이 동그랗게 보이도록 반지름 설정 */
                                width: 50px;  /* 가로 크기 */
                                height: 50px;  /* 세로 크기, 가로와 동일하게 설정 */
                                color: #FFD700;  /* 글자 색상 */
                                font-size: 27px;  /* 글자 크기 */
                                font-weight: bold;  /* 글자 두께를 굵게 */
                            }
                            """

        self.operator_btn_color_reset = """
                QPushButton {
                                background-color: #FFD700;  /* 진한 회색 배경 */
                                border-radius: 25px;  /* 버튼이 완전히 동그랗게 보이도록 반지름 설정 */
                                width: 50px;  /* 가로 크기 */
                                height: 50px;  /* 세로 크기, 가로와 동일하게 설정 */
                                color: white;  /* 글자 색상 */
                                font-size: 23px;  /* 글자 크기 */
                                font-weight: bold;  /* 글자 두께를 굵게 */
                            }
                            """

        # result_screen 값을 오른쪽에서 정렬 후 글자 크기 지정
        self.result_screen.setAlignment(Qt.AlignRight)
        self.result_screen.setText(str(self.digit_result))
        self.result_screen.setStyleSheet("QLineEdit { font-size: 24px; }")

        # 덧셈 버튼 클릭 시
        self.plus_color_changed = False  # 버튼 색상 플래그
        self.plus_btn.clicked.connect(lambda: self.operator_btn_Clicked('+'))

        # 뺄셈 버튼 클릭 시
        self.minus_color_changed = False  # 버튼 색상 플래그
        self.minus_btn.clicked.connect(lambda: self.operator_btn_Clicked('-'))

        # 곱셈 버튼 클릭 시
        self.multiply_color_changed = False  # 버튼 색상 플래그
        self.multiply_btn.clicked.connect(lambda: self.operator_btn_Clicked('*'))

        # 나눗셈 버튼 클릭 시
        self.divide_color_changed = False  # 버튼 색상 플래그
        self.divide_btn.clicked.connect(lambda: self.operator_btn_Clicked('/'))

        # = 버튼 클릭 시
        self.equal_btn.clicked.connect(self.equal_btn_Clicked)

        # 소수점 버튼 클릭시
        self.decimal_point.clicked.connect(self.decimal_point_Clicked)

        # 초기화 버튼 클릭시
        self.clear_btn.clicked.connect(self.clear_btn_Clicked)

        # 부호 변환 버튼 클릭시
        self.convert_op.clicked.connect(self.convert_op_Clicked)

        # 각 숫자 버튼 클릭 연결
        self.digit_0.clicked.connect(lambda: self.digit_zero_Clicked('0'))
        self.digit_1.clicked.connect(lambda: self.digit_Clicked('1'))
        self.digit_2.clicked.connect(lambda: self.digit_Clicked('2'))
        self.digit_3.clicked.connect(lambda: self.digit_Clicked('3'))
        self.digit_4.clicked.connect(lambda: self.digit_Clicked('4'))
        self.digit_5.clicked.connect(lambda: self.digit_Clicked('5'))
        self.digit_6.clicked.connect(lambda: self.digit_Clicked('6'))
        self.digit_7.clicked.connect(lambda: self.digit_Clicked('7'))
        self.digit_8.clicked.connect(lambda: self.digit_Clicked('8'))
        self.digit_9.clicked.connect(lambda: self.digit_Clicked('9'))


    def digit_zero_Clicked(self, digit):
        self.btn_color_Reset()
        '''if self.is_init != True:
            self.clear_btn.setText('C')'''

        if self.is_new_input == True:  # 새롭게 입력해야 하는 경우
            if self.is_init == True:  # 초기 상태일 경우
                if self.digit_result == '0':
                    return  # 0 이 클릭되면 안되므로 그냥 return 후 빠져나옴.
                else:
                    self.digit_result = '0'
            
            else:  # 초기 상태가 아닐 경우 즉, 0 이 우선은 하나 입력되야 하는 경우
                self.digit_result = digit  # 0
                self.clear_btn.setText('C')

            self.is_new_input == False  # 이어서 입력되도록 넘어감.

        else:  # selif.is_new_input == True 즉, 이어서 입력해야 하는 경우
            self.is_init == False
            self.digit_result += digit
    
        self.result_screen.setText(str(self.digit_result))
        self.is_last_input_operator = False  # 마지막 입력이 연산자가 아님

        # 각 리셋 변수 초기화
        '''if self.digit_clear_flag == True and self.operator_clear_flag == False:
            self.digit_clear_flag = False
        if self.operator_clear_flag == True and self.digit_clear_flag == False:
            self.operator_clear_flag = False'''


    def digit_Clicked(self, digit):
        self.btn_color_Reset()
        self.clear_btn.setText('C')

        if self.is_new_input == True:  # 새롭게 입력해야 하는 경우
            if '-' in self.digit_result[0]:  # 이미 - 가 있다면
                if self.digit_result[1] == '0':
                    self.digit_result = '-' + digit
                else:
                    self.digit_result = digit
            
            else:
                self.digit_result = digit


            self.is_new_input = False
            self.is_init = False  # 초기 상태가 해제

        else: 
            cur_digit = self.result_screen.text()

            #self.is_init = False  # 초기 상태가 아님
            self.digit_result += digit

        self.result_screen.setText(str(self.digit_result))  # 결과 화면에 표시
        self.is_last_input_operator = False  # 마지막 입력이 연산자가 아님

        # 각 리셋 변수 초기화
        '''if self.digit_clear_flag == True and self.operator_clear_flag == False:
            self.digit_clear_flag = False
        if self.operator_clear_flag == True and self.digit_clear_flag == False:
            self.operator_clear_flag = False'''


    # 중간 계산 함수
    def interim_Calculator(self):
        if self.operator_cnt < 3:
            self.digit_result = '0'
            return

        # 덧셈이나 뺄셈일 때 이전에 입력된 모든 연산을 수행
        if self.calc_list[-1] in ['+', '-']:
            last_digit_idx = 0  # 맨 처음 숫자부터 선택 
            interim_list = self.calc_list[last_digit_idx:self.operator_cnt]
            interim_str = ''.join(interim_list)

            self.digit_result_num = round(eval(interim_str), 8)

            if int(self.digit_result_num) == self.digit_result_num:  # 정수형으로 나타낼 수 있는데 실수형으로 나타내진 경우
                self.digit_result_num = int(self.digit_result_num)

            self.digit_result = str(self.digit_result_num)  # digit_result 는 문자열로 변환시킴
            self.result_screen.setText(str(self.digit_result))

            # calc_list 업데이트
            del self.calc_list[last_digit_idx:self.operator_cnt]
            self.calc_list.insert(last_digit_idx, str(self.digit_result_num))

            self.operator_cnt = 1  # cnt 1 로 초기화

        # 곱셈 혹은 나눗셈일 때
        elif self.calc_list[-1] in ['*', '/']:
            last_digit_idx = self.operator_cnt - 3  # 이전 숫자부터 선택 
            interim_list = self.calc_list[last_digit_idx:self.operator_cnt]
            interim_str = ''.join(interim_list)
            if not self.calc_list[self.operator_cnt - 2] in ['*', '/']:  # 이전 연산자가 곱셈이나 나눗셈이 아닐 경우 cnt초기화 안되고 cnt = 5 가 될 것이다.
                self.digit_result = self.calc_list[self.operator_cnt - 1]
                self.result_screen.setText((self.digit_result))  # 이전 클릭된 숫자 보여줌
            else:
                self.digit_result_num = round(eval(interim_str), 8)
                if int(self.digit_result_num) == self.digit_result_num:  # 정수형으로 나타낼 수 있는데 실수형으로 나타내진 경우
                    self.digit_result_num = int(self.digit_result_num)

                self.digit_result = str(self.digit_result_num)  # digit_result 는 문자열로 변환시킴
                self.result_screen.setText(str(self.digit_result))

                # calc_list 업데이트
                del self.calc_list[last_digit_idx:self.operator_cnt]
                self.calc_list.insert(last_digit_idx, str(self.digit_result_num))
                self.operator_cnt -= 2
                
        # 부호 변환을 위해 self.digit_result 를 0 으로 초기화
        self.digit_result = '0'


    def btn_color_Changed(self, btn):
        if btn == '+':
            if self.plus_color_changed == False:
                self.plus_btn.setStyleSheet(self.operator_btn_color_change)            
                self.plus_color_changed = True

        elif btn == '-':
            if self.minus_color_changed == False:
                self.minus_btn.setStyleSheet(self.operator_btn_color_change)
                self.minus_color_changed = True

        elif btn == '*':
            if self.multiply_color_changed == False:
                self.multiply_btn.setStyleSheet(self.operator_btn_color_change)
                self.multiply_color_changed = True

        else:
            if self.divide_color_changed == False:
                self.divide_btn.setStyleSheet(self.operator_btn_color_change)
                self.divide_color_changed = True


    def btn_color_Reset(self):
        if self.plus_color_changed:
            self.plus_btn.setStyleSheet(self.operator_btn_color_reset)  # 원래 색상으로 되돌림
            self.plus_color_changed = False
            
        elif self.minus_color_changed:
            self.minus_btn.setStyleSheet(self.operator_btn_color_reset)  # 원래 색상으로 되돌림
            self.minus_color_changed = False

        elif self.multiply_color_changed:
            self.multiply_btn.setStyleSheet(self.operator_btn_color_reset)  # 원래 색상으로 되돌림
            self.multiply_color_changed = False

        elif self.divide_color_changed:
            self.divide_btn.setStyleSheet(self.operator_btn_color_reset)  # 원래 색상으로 되돌림
            self.divide_color_changed = False   
            

    def operator_btn_Clicked(self, signal):
        self.is_init = False
        if self.is_last_input_operator == True:
            return
        
        self.operator_cnt += 2
        cur_digit = self.result_screen.text()
        self.calc_list.append((cur_digit))

        if signal == '+':
            self.calc_list.append('+')
             # 버튼 색상 바꾸기
            if self.plus_color_changed == False:
                self.plus_btn.setStyleSheet(self.operator_btn_color_change)
                self.plus_color_changed = True

        elif signal == '-':
            self.calc_list.append('-')
            # 버튼 색상 바꾸기
            if self.minus_color_changed == False:
                self.minus_btn.setStyleSheet(self.operator_btn_color_change)
                self.minus_color_changed = True

        elif signal == '*':
            self.calc_list.append('*')
            # 버튼 색상 바꾸기
            if self.multiply_color_changed == False:
                self.multiply_btn.setStyleSheet(self.operator_btn_color_change)
                self.multiply_color_changed = True
        
        else:
            self.calc_list.append('/')
            # 버튼 색상 바꾸기
            if self.divide_color_changed == False:
                self.divide_btn.setStyleSheet(self.operator_btn_color_change)
                self.divide_color_changed = True

        self.is_new_input = True  # 새로운 숫자 입력 여부
        self.is_last_input_operator = True  # 마지막 입력이 연산자

        self.interim_Calculator()


    def decimal_point_Clicked(self):
        self.clear_btn.setText('C')
        self.btn_color_Reset()
        self.is_last_input_operator = False  # 마지막 입력이 연산자가 아님
        #display_digit = self.result_screen.text()
        if '.' not in self.digit_result:  # 현재 값에 소수점이 없는 경우
            self.digit_result = self.digit_result + '.'  # 소수점을 추가
            self.is_new_input = False  # 새로운 입력이 아님을 표시
            # '=' 버튼을 눌러 계산 결과가 나타나있는 상태에서
            if self.is_init == True and self.operator_cnt == -1:  # 초기 상태에서 
                self.digit_result = '0' + '.'
                self.is_new_input = False

        else:
            self.digit_result = self.digit_result  # 소수점이 이미 있는 경우 현재 숫자를 유지
            # '=' 버튼을 눌러 계산 결과가 나타나있는 상태에서
            if self.is_init == True and self.operator_cnt == -1:
                self.digit_result = '0' + '.'
                self.is_new_input = False
        
        self.result_screen.setText(str(self.digit_result))  # 결과 화면에 표시
    

    def equal_btn_Clicked(self):
        if self.is_last_input_operator == False:  # 마지막 입력이 연산자가 아닌 경우 즉, 숫자로 끝난 경우
            self.calc_list.append(self.digit_result)  # 현재 숫자를 계산식에 추가
            self.calc_str = ''.join(self.calc_list)  # 문자열로 변환
    
            self.digit_result_num = (round(eval(self.calc_str), 8))

            if int(self.digit_result_num) == self.digit_result_num:  # 정수형으로 나타낼 수 있는데 실수형으로 나타내진 경우
                self.digit_result_num = int(self.digit_result_num)
                
            self.digit_result = str(self.digit_result_num)  # digit_result 는 문자열로 변환시킴 
            #self.digit_result = str(round(eval(self.calc_str), 8))  # 소수점 8번째 자리 까지만 반올림
            
            self.result_screen.setText(str(self.digit_result))
            self.btn_color_Reset()  # 연산자 버튼 색 초기화
            self.reset_calculator()  # 모든 변수 초기화

        else:  # 마지막 입력이 연산자인 경우 즉, 연산자를 누르고 나서 = 버튼을 누른 경우
            self.btn_color_Reset()  # 우선 버튼 입력 초기화
            first_result = self.calc_list[0]  # 첫 번째 인자를 first_result 에 저장
            self.equal_cnt += 1
            #self.is_last_input_operator = False  # 중간에 연산자 입력 가능
            if self.calc_list[-1] == '+':  # '+' 연산자 입력한 상태에서 '=' 버튼 누르면
                #first_result = self.calc_list[0]  # 첫 번째 인자를 first_result 에 저장
                self.digit_result = eval(f"{first_result} * ({self.equal_cnt} + 1)")
                self.result_screen.setText(str(self.digit_result))
            
            elif self.calc_list[-1] == '-':  # '-' 연산자 입력한 상태에서 '-; 버튼 누르면
                self.digit_result = eval(f"{first_result} - {first_result} * {self.equal_cnt}")
                self.result_screen.setText(str(self.digit_result))


    def reset_calculator(self):
        self.equal_cnt = 0  # 초기화
        self.operator_cnt = -1  # 초기화
        self.is_new_input = True  # 새로운 숫자 입력 여부
        self.calc_list = []  # 계산 리스트 초기화
        self.is_init = True
        self.is_last_input_operator = False
        self.digit_clear_flag = False
        self.operator_clear_flag = False 


    # 초기화 버튼 누르기
    def clear_btn_Clicked(self):
        if self.clear_btn.text() == 'AC':  # 초기 상태에 누르거나 두 번 연속 눌리면 계산기 초기화
            self.reset_calculator()  # 계산기를 초기화
            self.btn_color_Reset()  # 연산자 버튼 색깔도 초기화

        else:  # self.clear_btn.text() != 'AC' 즉, 'C' 일 때
            self.digit_result = '0'
            #self.result_screen.setText(str(self.digit_result))  # 우선 화면에 0 을 띄워주고
            self.clear_btn.setText('AC')  # 'AC' 로 글자 초기화
            btn_status_dict = {'+' : 'self.plus_color_changed', '-' : 'self.minus_color_changed',
                                '*' : 'self.multiply_color_changed', '/' : 'self.divide_color_changed'}
            if eval(btn_status_dict[self.calc_list[-1]]) != True:  # 숫자 누른 상태에서 클리어 누르면
                self.is_new_input = True  # 새롭게 문자열 입력
                # 마지막에 눌렀던 연산자 버튼 켜주고
                key_value = self.calc_list[-1]  # 예를 들어 '+' 라면 + 버튼을 다시 켜야 함.
                self.btn_color_Changed(key_value)  # 생성된 딕셔너리에서 키값을 이용해 값 가져옴.
        self.result_screen.setText(str(self.digit_result))


    # 부호 변환 함수
    def convert_op_Clicked(self):
        self.is_init = False
        if not '-' in self.digit_result[0]:  # (+) 부호라면
            self.digit_result = '-' + self.digit_result
        else:  # (-) 부호라면
            self.digit_result = self.digit_result[1:]

        self.result_screen.setText(str(self.digit_result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
