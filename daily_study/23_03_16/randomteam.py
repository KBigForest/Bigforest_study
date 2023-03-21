import random as rd
Team1 = ['김성훈', '임도영', '김도형', '서홍렬', '정도']
names = ['이아름', '신지은', '이장국', '장마가', '김동우', '손지현', '우광원', '석은수', '김한림','이혜원', '이소정', '김상민', '김수진', '신호림', '한수아', '김현아','하주리', '강서연', '김준수']
rd.shuffle(names)

Team2 = names[0:5]
Team3 = names[5:10]
Team4 = names[10:15]
Team5 = names[15:]
print('Team1 is {} \nTeam2 is {} \nTeam3 is {} \nTeam4 is {} \nTeam5 is {}'.format(' '.join(Team1), ' '.join(Team2), ' '.join(Team3), ' '.join(Team4), ' '.join(Team5)))