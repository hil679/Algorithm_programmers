def solution(emergency: list) -> list: #함수에 작성된 annotation은 주석, 따라서 annotation과 무관한 인자를 넣어도 정상 동작
    dict = {num: index for index, num in enumerate(sorted(emergency, reverse=True), start=1)}
    #enumerate -> start지정(0이 아닌 1순위부터 시작)
    #reverse = True => 역정렬
    
    return [dict[x] for x in emergency]



    # Fuctnion annotation
# def func(arg1: str, arg2: 1+2, arg3: 'this is annotation') -> bool
    
#    위와 같이 파라미터에 : expression 형태로 매개변수 마다 annotation 을 쓸 수 있다. 

#    annotation 에는 arg1 처럼 매개변수의 type 을 써놓을 수도 있고,

#    arg2 의 annotation 처럼 덧셈과 같은 간단한 연산 표현도 작성 가능하며, 

#    arg3 처럼 string 형태로도 작성 가능하다. 


#    또한, function 의 return 값에 대해서는 -> expression 형태로 사용한다. 

#    return 또한 매개변수와 사용 방법은 동일하다.