# DOM & Event

# History of JavaScript

## ECMAScript
: Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- 스크립트 언어가 준수해야 하는 규칙, 세부사항 등

### ECMAScript와 JavaScript
- ECMAScript는 JavaScript의 표준, Java는 ECMA 표준을 따르는 구체적인 프로그래밍 언어
- ECMA는 언어의 핵심을 정의하고, Java는 ECMA 표준을 따라 구현된 언어로 사용

### ECMAScript의 역사
- ECMAScript 2015(ES6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, 역사상 가장 중요한 버전으로 평가(2015)

# 변수데이터 타입

## 변수 선언 키워드

### 식별자(변수명) 작성 규칙
- 반드시 문자, 달러('$') 또는 밑줄('_')로 시작
- 대소문자 구분
- 예약어 사용 불가
    - for, if, function 등

### 식별자(변수명) Naming case
----- 수업에서는 언급 안 한 듯

### 변수 선언 키워드 3가지
1. let
2. const
3. ~~var~~

#### let
----- 일단 쉬는 시간에...
- 블록 스코프(block scope)를 갖는 지역 변수를 선언
- 재할당 가능
- 재선언 불가능
- ES6에서 추가

#### const
- **블록 스코프**를 갖는 지역 변수를 선언
- 재할당 불가능
- 재선언 불가능
- ES6에서 추가

#### 블록 스코프 (block scope)
- if, for, 함수 등의 '중괄호({}) 내부'를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

#### 어떤 변수 선언 키워드를 사용해야 할까?
- 기본적으로 const 사용 권장

## 데이터 타입

### 원시 자료형(Primitive type)
: 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
- Number, String, Boolean, null, undefined

#### Number
- 정수 또는 실수형 숫자를 표현하는 자료형
- NaN: 연산할 수 없는 연산을 진행했을 때

#### Template literals (템플릿 리터럴)
- 내장된 표현식을 허용하는 문자열 작성 방식
----- 추가하기

#### null과 undefined
- null: 변수의 값이 없음을 의도적으로 표현할 때 사용
- undefined: 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

#### '값이 없음'에 대한 표현이 null과 undefined 2가지인 이유
------ 추가하시길...
```javascript
typeof null         // "object"
typeof undefined    // "undefined"
```

#### 자동 형변환




### 참조 자료형(Reference type)
: 객체의 주소가 저장되는 자료형(가변, 주소가 복사)
- Objects(Object, Array, Function)


# 연산자

### 할당 연산자

### 증가 & 감소 연산자
----- 있다 정도

### 비교 연산자
----- python이랑 똑같다

### 동등 연산자(==)
- 암묵적 타입 변환까지 진행된다
```javascript
console.log('1' == 1)       // true
```

### 일치 연산자(===)

### 논리 연산자
- and 연산 `&&`
- or 연산 `||`
- not 연산 `!`
- 단축 평가 지원

# 제어문
## 조건문

### if
```javascript
if
else if
else
```

### 삼항 연산자 (시험에 안 나옴 기억해두면 좋음)
```javascript
ㅇㅇ
```


## 반복문
- while
- for
- for...in
- for...of

### while
----- 파이썬이랑 똑같

### for
- 

### for...in
- 객체의 열거 가능한 속성(property)에 대한 반복
- object 순회할 때만 쓸 거

### for...of
- 반복 가능한 ...

### 반복문 종합
----- 써보셈...



# DOM

### DOM tree

### 브라우저가 웹 페이지를 불러오는 과정

### DOM 핵심
: 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API

## document 객체
: 웹 페이지 객체
: DOM Tree의 진입점
- 페이지를 구성하는 모든 객체 요소를 포함



# DOM 선택

### DOM 조작 시 기억해야 할 것
**웹 페이지를 동적으로 ...

## 선택 메서드
- `document.querySelector()`
    - 요소 한 개 선택
- `document.querySelectorAll()`
    - 요소 여러 개 선택

### `document.querySelector(selector)`
-----

### `document.querySelectorAll(selector)`
: 제공한 선택자와 일치하는 여러 element를 선택
- 제공한 CSS selector를 만족하는 NodeList를 반환

### DOM 선택 실습


# DOM 조작
1. 속성(attribute) 조작
    - 클래스 속성 조작
    - 일반 속성 조작
2. HTML 콘텐츠 조작
3. DOM 요소 조작
4. 스타일 조작

## 속성 조작

### 클래스 속성 조작
`classList` property
: 
### 1. classList method

### 클래스 속성 조작 실습

### 2. 일반 속성 조작 메서드

### 일반 속성 조작 실습


## HTML 콘텐츠 조작
`textContent1` property
:
### HTML 조작 실습????

## DOM 요소 조작

### DOM 요소 조작 메서드

## style 조작
`style` property
: 

### style 조작 실습
----- 왜 안 쓸까? 스타일 조작 어케 해야할까? 고민해보삼

# 참고
----- 한 번쯤 읽어보시면 좋을 거 가태요



# 함수
Function: 참조 자료형에 속하며 모든 함수는 `Function` object

## 함수 정의

### 함수 구조
```javascript
```
- `function` 키워드
- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statments
- **return 값이 없으면 undefined 반환**

### 함수 정의 2가지 방법

선언식 vs 표현식

#### 선언식
```javascript
```

#### 표현식
```javascript
```

### 함수 표현식 특징


## 매개변수

### 매개변수 정의 방법

### 1. 기본 함수 매개변수 ()

### 매개변수와 인자 개수가 불일치 할 때
- 누락된 인자는 undefined로 할당
- 초과 입력한 인자는 사용하지 않음

### 2. 



## Spread syntax

`...` (Spread syntax): 전개 구문

### 전개 구문 활용처
1. 함수와의 사용
2. 객체와의 사용
-----

### 전개 구문 활용



## 화살표 함수
화살표 함수 표현식(Arrow function y)

### 화살표 함수 작성 결과
```javascript
```
```javascript
```

### 화살표 함수 작성 과정
1. **function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성**
2. ----- 나머지는 걍 잘 확인해보시길

### 화살표 함수 심화

## 참고

### 세미콜론
- 자바스크립트는 문장 마지막 세미콜론(';')을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
- JavaScript를 만든 Brendan Eich 또한 세미콜론 작성을 반대



# 이벤트

### 일상 속의 이벤트

### 웹에서의 이벤트


## event 객체

### event
: 무언가 일어났다는 신호, 사건
- -----

### `event` object
: DOM에서 이벤트가 발생했을 때 생성되는 객체
- 이벤트 종류
    - mouse, input, keyboard, touch ...

**DOM 요소는 event를 받고 받은 event를 '처리'할 수 있음**



## event handler
: 이벤트가 발생했을 때 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

### `.addEventlistener()`
대표적인 ----- 이거 무시하는 멘트
- 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
```javascript
EventTarget.addEventListener(type, handler)
// EventTarget - DOM 요소
// type - 수신할 이벤트
```
"대상에 특정 Event가 발생하면, -----"

### addEventListener 활용
-=---


## 버블링

### 버블링 개요



# event handler 활용





# 이벤트 기본 동작 취소
----- 이건 꼭 알고 가면 좋겠다
- HTML의 각 요소가 기본적으로 가지고 있는 이벤트가 때로는 방해가 되는 경우가 있어 이벤트의 기본 동작을 취소할 필요가 있음
- 예시
    - form 요소의 제출 이벤트를 취소하여 -----

### `.preventDefault()`
: 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정