use sqlclass_db;
desc nobel;
select * from nobel;

-- 모든 column
-- year, category, prize_amount, fullname, gender, birth_continent,birth_country
-- 과제
-- 1) 1960년에 노벨상 물리학상 또는 노벨 평화상을 수상한 사람의 정보를 출력
-- 출력 컬럼: year, category, fullname
select n.year, n.category, n.fullname
	from nobel as n
	where category in ('Physics', 'Peace');
	

-- 2) Albert Einstein이 수상한 연도와 수상 분야(category), 출생대륙, 출생국가를 출력
-- 출력 컬럼: year, category, birth_continent, birth_country

select year, category, birth_continent, birth_country
	from nobel
	where fullname = 'Albert Einstein';
	
-- 3) 1910년 부터 2010년까지 노벨 평화상 수상자 명단 출력 (연도 오름차순)
-- 출력 컬럼: year, fullname, birth_country
select year, fullname, birth_country
	from nobel n 
	where year between 1910 and 2010
	order by year;
	
-- 4) 전체 테이블에서 수상자 이름이 ‘John’으로 시작하는 수상자 모두 출력
-- - 출력 컬럼: category, fullname
select category, fullname
from nobel n 
where fullname like 'John%';

-- 5) 1964년 수상자 중에서 노벨화학상과 의학상(‘Physiology or Medicine’)을 제외한 수상
-- 자의 모든 정보를 수상자 이름을 기준으로 오름차순으로 정렬 후 출력

select year, category, prize_amount, fullname, gender, birth_continent,birth_country
from nobel n 
where category in ('Physiology' or'Medicine')
order by fullname asc;

-- 6) 2000년부터 2019년까지 노벨 문학상 수상자 명단 출력
-- - 출력 컬럼: year, fullname, gender, birth_country
select year, fullname, gender, birth_country
from nobel n
where year between 2000 and 2019;

-- 7) 각 분야별 역대 수상자의 수를 내림차순으로 정렬 후 출력(group by, order by)

select category, count(*)
from nobel n 
group by category 
order by count(*) desc;

-- 8) 노벨 의학상이 없었던 연도를 모두 출력 (distinct) 사용
select distinct year
from nobel
group by year
having year not in (select year from nobel n where category = 'Physiology or Medicine');


-- 9) 노벨 의학상이 없었던 연도의 총 회수를 출력
select count(distinct T.year) as year
	from
	(select distinct year
	from nobel	
	group by year
	having year not in (select year from nobel n where category = 'Physiology or Medicine')) as T;



-- 10) 여성 노벨 수상자의 명단 출력
-- - 출력 컬럼: fullname, category, birth_country
select fullname, category, birth_country
from nobel n 
where gender = 'female';

-- 11) 수상자들의 출생 국가별 횟수 출력
-- - 출력 컬럼: birth_country, 횟수
select birth_country, count(*)
from nobel
group by birth_country;

-- 12) 수상자의 출생 국가가 ‘Korea’인 정보 모두 출력
select year, category, prize_amount, fullname, gender, birth_continent,birth_country
from nobel n 
where birth_country = 'Korea';

-- 13) 수상자의 출신 국가가 ‘Europe’, ‘North America’, 공백이 아닌 모든 정보 출력
select year, category, prize_amount, fullname, gender, birth_continent,birth_country
from nobel n 
where (birth_continent = 'Europe'  or birth_continent = 'North America')
and birth_continent  is not null;

-- 14) 수상자의 출신 국가별로 그룹화를 해서 수상 횟수가 10회 이상인 국가의 모든 정보
-- 출력하고 국가별 수상횟수의 역순으로 출력
select birth_country, count(*)
from nobel n 
group by birth_country
having count(*) >= 10
order by count(*) asc;


-- 15) 2회 이상 수상자 중에서 fullname이 공백이 아닌 경우를 출력하는데, fullname의 오
-- 름차순으로 출력
-- - 출력 컬럼: fullname, 횟수
select  fullname, count(*)
from nobel n 
where fullname !=''
group by fullname
having count(*) >= 2 
order by fullname asc;