use encore;
'''
그룹으로 묶어서 검색
#그룹함수사용: avg(), max(), sum(), min(), count()
#group by절: 그룹핑 기준
#having 절: 그룹 선택
'''
'''
# 보충내용 #
select department_id, avg(salary)
from employees
group by department_id #부서별로
having avg(salary)>5000;

select last_name, commission_pct, 
12*salary+12*salary*ifnull(commission_pct,0)
from employees;

#nullif(exp1, exp2): exp1과 exp2가 같으면 null, 같지 않으면 exp1 반환
select last_name, length(last_name), first_name, length(first_name),
nullif(length(last_name), length(first_name))
from employees;

select last_name "LAST_NAME", hire_date "HIRE_DATE"
from employees
where last_name = 'King' and 'Ernst';


#case: 비교할 조건이 여러개 일때 사용
/*
case exp
	when 값1 then 실행문
    when 값2 then 실행문
    when 값3 then 실행문
    else 실행문
end as '컬럼별칭'
*/

select department_id,
case department_id
	when 10 then '10번 부서'
	when 20 then '20번 부서'
    when 30 then '30번 부서'
    else '이외 부서'
end as '부서명'
from employees;

select bit_length('가나다'), length('가나다')
from dual;

select concat(last_name, first_name) name
from employees;

select concat_ws(' / ', last_name, first_name) name
from employees;
 
##########################
/*
서브쿼리: 문장 안에 있는 문장.
조건, 일괄 inssert, create, update, delete에서 사용됨
select 컬럼명...
from 테이블
where 조건 (서브쿼리)
*/

#where 조건에서 서브쿼리 사용
select last_name, salary
from employees
where salary > (select salary 
				from employees 
                where last_name = 'Abel');
                
#서브쿼리를 사용하여 테이블 생성
create table emp1
as
select employee_id as emp_id, last_name as name,
salary as sal, department_id as dept_id
from employees
where 1=0;
'''

desc emp1;

#서브쿼리 사용하여 여러줄 insert
insert into emp1
select employee_id, last_name, salary, department_id
from employees
where department_id = 80;

select * from emp1;

'''
DML문: insert, update, delete
insert into 테이블명(컬럼명...) values(값들...);
'''
alter table emp1  #제약조건을 추가한 것
add foreign key(dept_id) references departments(department_id);

#emp_id에 primary key 제약조건 추가
alter table emp1
add primary key(emp_id); #줄의 대표값이기에 중복 불가능. -> not null이며 unique이다.

set sql_safe_updates=0;

delete from emp1 where dept_id<>80;

insert into emp1 values(200, 'Apple', 5000, 70);
#insert/update시 문제가 있는 값을 수정하고나 추가할 시 걸러준다. 즉 에러난다.
#같은 내용을 중복 insert할 시 

delete from emp1 where emp_id = '200';

####################

select * from emp1;
update emp1 set sal=15000 where name 'Turker';

delete from emp1 where departmnet_id = '30';


delete from emp1 where name = 'Turker';
delete from emp1 where dept_id = 70;

#그냥 롤백하면 전체 작업이 날아감.
#특정 한 부분만 롤백하고 싶다면 save point - > 점을 찍어서 표시

#트랜잭션
set autocommit = 0; #자동커밋 해제alter
insert into emp1 values(200, 'bbb', 15000, 70);
insert into emp1 values(201, 'ccc', 5000, 90);
insert into emp1 values(202, 'ddd', 4000, 100);

savepoint a;
update emp1 
set name = 'new bbb', sal='12345' 
where emp_id = 200;

savepoint b;

delete from emp1 where emp_id = 202;

##rollback to b;
#rollback to a;
#rollback;
commit;

select * from emp1;