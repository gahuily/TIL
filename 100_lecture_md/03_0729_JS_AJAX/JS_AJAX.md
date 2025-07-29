# 객체
### Object
: 키로 구분된 데이터 집합(data collection)을 저장하는 자료형

## 구조 및 속성

### 객체 구조
- 중괄호('{}')를 이용해 작성
- 중괄호 안에는 `key: value` 쌍으로 구성된 속성(property)를 여러 개 작성 가능
- key는 문자형만 허용 - 중복X, 불변형 자료 타입
- value는 모든 자료형 허용
```javascript
const user = {
    name: 'Alice',
    'key with space': true,
    greeting: function () {
    return 'hello'
    }
}
```
- 공백이 있는 경우만 따옴표(`'key with space'`), 아닌 경우 따옴표 없어도 무관(`name`)
- 함수도 객체다 (함수 표현식으로 greeting에 할당)

### 속성 참조
- 점('.', chaining operator) 또는 대괄호('[]')로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
```javascript

```

### 'in' 연산자
- 속성이 객체에 존재하는지 여부를 확인
```javascript
console.log('greeting' in user) // true
console.log('country' in user) // false
```

## 객체와 함수

### Method
: 객체 속성에 정의된 함수
- `object.method()` 방식으로 호출
- 메서드는

## this

### Method
: 객체 속성에 정의된 함수
- 'this' 키워드를 통해 -----

### 'this' keyword
: 함수나 메서드를 호출한 객체를 가리키는 키워드
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

### Method & this 사용 예시
```javascript
const person = {
    name: 'Alice',
    greeting: function () {
    return `Hello my name is ${this.name}`
    },
}

console.log(person.greeting()) // Hello my name is Alice
```
- person.greeting -> this - person

### JavaScript에서는 this는 함수를 **"호출하는 방법"**에 따라 가리키는 대상이 다름
| --- | --- |

### 1. 
```javascript
    const myFunc = function () {
      return this
    }
    console.log(myFunc()) // window
```
### 2. 
```javascript
    const myObj = {
      data: 1,
      myFunc: function () {
        return this
      }
    }
    console.log(myObj.myFunc()) // myObj
```
# *----- 이거 강의 한 번만 다시 봐봐*


### 중첩돤 함수에서의 this 문제점과 해결책

### JavaScript 'this' 정리
-----

## 추가 객체 문법

### 1. 단축 속성
- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음
```javascript
const name = 'Alice'
const age = 30

const user = {
    name: name,
    age: age
}
```

```javascript
const name = 'Alice'
const age = 30

const user = {
    name,
    age
}
```
### 2.

### 3. ...

### 4. 구조 분해 할당
- 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법

### 5. Oject with '전개 구문'
- "객체 복사"
    - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

### 6. 유용한 객체 메서드
----- 확인하고 넘어가죠

### 7. Optional chaining('?.')
- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환
1. Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 함 (남용 X)
    - ...


```javascript
```
```javascript
```
```javascript
```

# 참고 ----- 시험에 안 나온다

## JSON
- "JavaScript Object Notation"
- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 **"문자열"**




# 배열

### Object
: 키로 구분된 데이터 집합을 저장하는 자료형
- 이제는 **순서가 있는 collection**이 필요

- for...in은 순서 X, for...of는 순서 O 배열로 ㄱㄱ

### Array


### 배열 구조
- 대괄호('[]')로 작성


## 배열 메서드

### 주요 메서드



## Array Helper Method
: -----
- 배열의 각 요소를 **순회**하며 -----

### 주요 Array Helper Method
| 메서드 | 특징 |
| ----- | ---- |

### forEach 구조


### forEach 예시

### map()

### map 예시

### map 활용




### 기타 Arrya
----- some every는 있다 정도
----- forEach만큼 많이 쓰는 게 filter find


# 참고

## "배열은 객체다"
arr[-1] = 4 라고 하면 -1 자리에 4가 아니라


# 비동기

### Synchronous(동기)
: 프로그램의 실행 흐름이 순차적으로 진행
- 하나의 작업이 완료된 후에 다음 작업이 실행되는 

### Synchronous 예시
2. 메인 작업이 모두 수행되어야 마지막 작업이 수행됨
3. 함수의 작업이 완료될 때까지 기다렸다가 값을 반환해야 계속 진행 가능

### Asynchronous(비동기)
: 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식
- 작업의 완료 여부를 신경 쓰지 않고 **동시에 다른 작업들을 수행할 수 있음**

### Asynchronous 예시
1. 커피 주문
2. Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 별도로 처리됨
3. 브라우저는 웹페이지를 먼저 처리되는 요소부터 그려 나가며 처리가 오래 걸리는 것들은 별도로 처리가 완료되는 대로 병렬적으로 진행

### Asynchronous 특징

## JavaScript와 비동기

### Single Thread 언어, JavaScript

#### Thread란?
: 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미

### JavaScript Runtime
- "JavaScript가 동작할 수 있는 환경(Runtime)"
- -----

### 브라우저 환경에서의 JavaScript -----

### 런타임의 시각적 표현
- call stack - last in first out
- task queue - first in first out


# AJAX
: Asynchronous JavaScript and ~~XML~~ JSON
: XMLHttpRequest 기술을 사용해 복잡하고 동적인 웹 페이지를 구성하는 프로그래밍 방식

### AJAX 목적
- 전체 페이지가 다시 로드되지 않고 HTML 페이지 일부 DOM만 업데이터
- 웹 페이지 일부가 다시 로드되는 동안에도 코드가 계속 실행되어, 비동기식으로 작업할 수 있음

## XHR
: 서버와 상호작용할 때 사용하는 객체

### XMLHttpRequest 특징
- 브라우저와 서버 간의 네트워크 요청을 전송할 수 있음
- 사용자의 작업을 방해하지 않고 페이지의 일부를 업데이트할 수 있음
- 요청의 상태와 응답을 모니터링할 수 있음

### XHR 구조
-----

# Callback과 Promise

## 비동기 콜백

### 비동기 처리의 단점
- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 **작업이 완료되는 순서에 따라 처리**한다는 것
- 그런데 이는 개발자 입장에서 **코드의 실행 순서가 불명확**하다는 단점 존재
- 이와 같은 단점은 실행 결과를 예상하면서 코드를 작성할 수 없게 함

- 콜백 함수를 사용하자!

### 비동기 콜백
- 비동기적으로 처리되는 작업이 완료되었을 대 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 **순차적으로 동작**할 수 있게 함
- ------

### 비동기 콜백의 한계



### 콜백 지옥 (Callback Hell)


### 콜백 함수 정리
- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 ...

## 프로미스
: JavaScript에서 비동기 작업의 결과를 나타내는 객체
- 비동기 작업이 완료 -----

### "Promise" object
- 자바스크립트에서 비동기 작업을 처리하기 위한 객체
- 비동기 작업의 성공 또는 실패와 관련된 결과나 값을 나타냄

### 비동기 콜백 vs Promise

### then 메서드 chaining의 목적
- 비동기 작업의 **"순차적인"** 처리 가능
- 코드를 보다 직관적이고 가독성 좋게 작성할 수 있도록 도움

### then 메서드 chaining의 장점


성공에 대한 약속 then()
실패에 대한 약속 catch()


### Promise가 보장하는 것 (vs 비동기 콜백)


# Axios
: JavaScript에서 사용되는 HTTP 클라이언트 라이브러리

### Axios 정의
: 클라이언트 및 서버 사이에 HTTP 요청을 만들고 -----

### AJAX를 활용한 클라이언트 서버 간 동작

### Axios 활용

![then 추가 실습](image.png)
![then 추가 실습](image-1.png)


# 참고
### 비동기를 사용하는 이유 - "사용자 경험"