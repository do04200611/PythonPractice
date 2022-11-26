score = int(input("첫번째 숫자입력: "))
score2 = int(input("두번째 숫자입력: "))
if score < score2 :
 print("두수 중에 큰 수는 {} 작은 수는 {} 입니다. ".format(score, score2))
elif score2 < score:
 print("두수 중에 큰 수는 {} 작은 수는 {} 입니다.".format(score, score2))
else :
    print("두 수 모두 같습니다.".format(score,score2))