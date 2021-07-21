#
# def decorator(fn):
#     def decorated(input_text):
#         print('함수 시작')
#         fn(input_text)
#         print('함수 끝')
#     return decorated
#
# @decorator
# def hello_world(input_text):
#     print(input_text)
#
# hello_world('안녕')

def decorator_2(fn):
    def decorated(h, w):
        if h > 0 and w > 0 :
            return fn(h,w)
        else:
            raise ValueError('입력값이 양수가 아닙니다')
    return decorated

@decorator_2
def triangle(h,w):
    print(1/2 * h * w)

@decorator_2
def rectangle(h,w):
    print(h * w)

triangle(-1,2)

rectangle(2,3)