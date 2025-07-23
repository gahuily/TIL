# 문제
# 제공된 SNS 사용자 데이터를 기반으로 특정 조건을 만족하는 사용자 정보를 필터링하고, 이를 함수와 모듈을 사용하여 구현하시오.

# 요구사항
# 나이가 18세 이상인 사용자를 필터링하는 함수를 작성하시오.
# 활성화된(is_active가 True인) 사용자를 필터링하는 함수를 작성하시오.
# 나이가 18세 이상이고 활성화된 사용자를 필터링하는 함수를 작성하시오.
# 위의 함수를 별도의 모듈로 작성하고, 이를 메인 파일에서 불러와 사용하시오.

users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

# 아래에 코드를 작성하시오.

def adult():
    age = []
    for i in users:
        if i.get("age") >= 18:
            age.append(i)
    print(age)

# print(adult(users))

def active():
    act = []
    for i in users:
        if i.get("is_active") == True:
            act.append(i)
    print(act)

# print(active(users))

def adult_active():
    both = []
    for i in users:
        if (i.get("age") >= 18) & (i.get("is_active") == True):
            both.append(i)
    print(both)

# print(adult_active(users))


# print(users[2].get("age"))