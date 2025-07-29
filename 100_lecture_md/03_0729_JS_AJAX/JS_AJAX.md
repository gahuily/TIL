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



```javascript
```
```javascript
```
```javascript
```



# 배열

## 배열 메서드

## Array helper method

## 추가 배열 문법

# 비동기

# AJAX

## XHR

# Callback과 Promise

# Axios