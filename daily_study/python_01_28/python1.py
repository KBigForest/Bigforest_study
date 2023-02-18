import random
import pandas as pd

total_list = ['이소정', '석은수', '장마가', '우광원', '하주리', '김현아', '신지은', '이혜원', '이장국', '김동우', '서홍열', '정도', '임도영', '김도형', '손지현', '김한림', '서동영', '한수아', '강서연', '김준수', '이아름', '김성훈', '신호림', '김수진', '김상민']

# 이전 조에 있었던 사람들을 저장할 set
prev_teams = set()

# 총 15번 반복
for i in range(15):
    # 이번 조를 저장할 리스트
    this_team = []
    # 전체 팀원 명단에서 5명을 랜덤으로 뽑는다.
    while len(this_team) < 5:
        person = random.choice(total_list)
        # 이번 조에 이미 있거나 이전 조에 있었던 사람이면 다시 뽑는다.
        if person not in this_team and person not in prev_teams:
            this_team.append(person)
    # 이번 조를 이전 조에 추가
    prev_teams.update(this_team)
    # 이번 조를 출력
    print("Team {}: {}".format(i+1, this_team))