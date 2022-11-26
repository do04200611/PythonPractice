score= int(input("점수를 입력하세요: "))
if score >= 90:
    print("좋은 성적 90점이상입니다.")
    print("A학점입니다.")
elif 80 <= score <= 90:
    print("좋은 성적 90점 미만 80점 이상입니다.")
    print("B학점입니다.")
elif 70 <= score <= 80:
    print("좋은 성적 80점이상 70점 미만입니다.")
    print("C학점입니다.")
elif 60 <= score <= 70:
    print("좋은 성적 70점이상 60점 미만입니다.")
    print("D학점입니다.")   
else:
    print("좋은 성적 60점 미만입니다.")
    print("F학점입니다.")   