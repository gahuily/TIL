# 웹
## Web site
- 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
## Web page
- HTML, CSS 등의 웹 기술을 이용하여 만들어진 "Web site"를 구성하는 하나의 요소

# 웹 구조화
## HTML
- ㅇ
### Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- 특징
    - -----참고하세요...

### Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

## Structure of HTML
----- 내용 강의 듣고 추가해주세요......

### HTML Attributes(속성) 작성 규칙
1. 속성은 요소 이름과 속성 사이에 공백이 있어야 함
2. 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
3. 속성 값은 열고 닫는 따옴표로 감싸야 함

### HTML 구조 예시
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>My page</title>
</head>

<body>
  <p>This is my page</p>
  <a href="https://www.google.co.kr/">Google로 이동</a>
  <img src="images/sample.png" alt="sample-img">
  <img src="https://random.imagecdn.app/500/150/" alt="sample-img">
</body>

</html>
```
- vscode에서는 `! + tab`, 여는 태그/닫는 태그 `태그 + tab`
- alt + b -> HTML 페이지 열기
- F12(개발자 도구) -> 주로 Elements, Console 사용

## HTML Text structure
### HTML
- HyperText Markup Language
- 웹 페이지의 의미와 구조를 정의하는 언어
#### `<h1>Heading<h1>`
- 예를 들어 h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것

#### 대표적인 HTML Text Structure
- Heading & Paragraphs
    - h1~6, p
- Lists
    - ol(ordered list), ul(unordered list), li
- Emphasis & Importance
    - em, strong

## 웹 스타일링
### CSS; Cascading Style Sheet
- 웹 페이지의 디자인과 레이아웃을 구성하는 언어

#### CSS 구문
```css
h1 {
    color: red;
    font-size: 30px;
}
```
`h1`: 선택자(Selector)
----- css 추가 내용 들으세요... 한 45분쯤?

#### CSS Selectors (선택자)
: HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

##### CSS Selectors 종류
- 기본 선택자
    - 전체(*) 선택자
    - 요소(tag) 선택자
    - 클래스(class) 선택자
        - `<p id=-->`
    - 아이디(id) 선택자
    - 속성(attr) 선택자 등
- 결합자 (Combinators)
    - 자손 결합자(" "(space))
    - 자식 결합자(">")

##### CSS Selectors 특징
- 전체 선택자(*)
    - HTML 모든 요소를 선택
- 요소 선택자
    - 지정한 모든 태그를 선택
- 클래스 선택자('.'(dot))
    - 주어진 클래스 속성을 가진 모든 요소를 선택
- 아이디 선택자('#')
    - 주어진 아이디 속성을 가진 요소 선택
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함

#### Specificity; 명시도
: 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘

#### CSS; Cascading Style Sheet
: 웹 페이지의 디자인과 레이아웃을 구성하는 언어

#### Cascade; 계단식
: 한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용됨

#### 명시도가 높은 순
1. Importance
    - !important
2. Inline 스타일
3. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 선언 순서
5. 상속 받은 속성들

##### !important
- 다른 우선순위 규칙보다 우선하여 적용하는 키워드
- **Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음 =**

----- 강의 다시 보세요...


#### 명시도 관련 문서
----- MM 참고하세요...

## 참고
### HTML 스타일 가이드
- 대소문자 구분
    - HTML은 대소문자를 구분하지 않지만, 소문자 사용을 강력히 권장
    - 태그명과 속성명 모두 소문자로 작성
- 속성 따옴표
    - 속성 값에는 큰 따옴표(")를 사용하는 것이 일반적
- 코드 구조와 포맷팅
    - 일관된 들여쓰기를 사용 (보통 2칸 공백)
    - 각 요소는 한 줄에 하나씩 작성
    - 중첩된 요소는 한 단계 더 들여쓰기
- 공백 처리
    - HTML은 연속된 공백을 하나로 처리
    - ----- 마저 쓰세요...

### CSS 스타일 가이드
- 코드 구조와 포맷팅
    - ----- 쓰세요...
    - **마지막 속성 뒤에는 세미콜론(;) 넣기**
- 선택자 사용
    - class 선택자를 우선적으로 사용
    - id, 요소 선택자 등은 가능한 피할 것
    -> 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 -----
- 명명 규칙
    -케밥 케이스

**CSS의 모든 속성은 외우는 것이 아님**

#### MDN Web Docs
- HTML, CSS, JavaScript, 웹 API, 개발 도구 등 웹 기술에 대한 정보를 제공