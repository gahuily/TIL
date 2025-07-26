# 학생들의 이름과 점수를 딕셔너리에 저장하시오.
#    "Alice" = 85,
#    "Bob" = 78,
#    "Charlie" = 92,
#    "David" = 88,
#    "Eve" = 95
# 모든 학생의 평균 점수를 계산하여 출력하시오.
# 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
# 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
# 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.

'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.

students = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 88, "Eve": 95}
scores = students.values()
average = sum(scores)/5

print(average)

over80 = [i for i, j in students.items() if j >= 80]
print(over80)

sorted_by_score = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
for name, score in sorted_by_score.items():
    print(f"{name}: {score}")

score_max = max(students.values())
score_min = min(students.values())
print(score_max-score_min)

for i in students.keys():
    if students.get(i) < average:
        print(f"{i}의 점수는 {students.get(i)}입니다.")