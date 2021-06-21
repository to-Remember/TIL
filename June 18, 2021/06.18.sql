use encore;

/*
#제약조건 검색
select * from information_schema.table_constraints;

#제약조건 삭제
alter table 테이블명
drop constraint 제약조건 이름;

alter table
drop foreign key 제약조건이름;

#제약조건 추가
#primary key 추가
alter table 테이블명
add constraint [제약조건 이름-생략가능] primary key(컬럼명);

#foreign key 추가
alter table 테이블명
add constraint [제약조건 이름-생략가능] foreign key(컬럼명)
references 부모테이블(컬럼명) [on delete cascade / on delete set null];

#not null 추가
alter table 테이블명
modify 컬럼명[타입] constrain[사용할제약조건이름] not null;
*/

/*
뷰: 가상 테이블 -> 쓰기 작업은 하지 말 것
(테이블에 다이렉트로 접근하는 게 아님.)
(껐다 키면 뷰는 없어지지만 뷰를 작성한 식은 남아있음.)
1. 복잡한 쿼리를 가상 테이블인 뷰로 만들면 사용이 간단해진다.
2. 보안(사용자의 레벨에 따라 접근 레벨을 분류할 수 있다.)
3. 데터의 독립성을 유지

생성
create [or replace] view 뷰이름
as 
서브쿼리
*/

create view view_80
as
select employee_id
as emp_id, last_name as name, salary
from employees
where department_id = 80;

select * from view_80;

update view_80 set name = 'aaa' where emp_id = 145;
select last_name from employees where employee_id = 145;

create or replace view emp_view
as
select last_name, department_name, city, salary
from employees join departments
using(department_id)
join locations
using(location_id);

select * from emp_view;

/*
#인덱스: 빠른 검색을 제공하기 위해 지정된 컬럼값을 완전 B트리로 구성
제약조건 primary key, unique를 만들면 자동 생성됨
인덱스 설정할 컬럼: 수정, 삭제가 잘 일어나지 않고 테이블에 만흔 수의 행이 있지만 
검색 where 절에서 사용하는 컬럼으로 이 컬럼으로 검색된 행이 몇줄 안되는 컬럼.

create index 인덱스명 on 테이블명(컬럼명);
*/

/*저장 프로시저
create procedure 이름(파라미터 리스트)
begin
	실행문
end

============
함수 호출
call 함수명()
*/
#tlsql에서의 변수는 골뱅이
set @a = 10;

select @a;

set @enum = (select employee_id
             from employees
             where last_name = 'Abel');
select @enum;

select employee_id, salary into @enum, @sal from employees where last_name = 'Abel';
select @enum, @sal;

call p1(100);

call p2(100, @ename);
select @ename; #비립종

call p3(100);

call p4(145);
call p4(175);

/*
if 조건 then
elseif 조건 then
else 실행문
end if;
*/

call p5(202);

call p6(200);

call p7(10);

call p8(10);

call p9(10);

call p10(10);

call cursor_test();

SET GLOBAL log_bin_trust_function_creators = 1;

select employee_id, f1(last_name, first_name) as name, salary
from employees;

select f2(employee_id) as name from employees;

/*
트리거: insert, update, delete 동작이 실행될때마다 이 동작 전이나 후에 실행할 코드를 등록하는 방법
생성:
create tigger 트리거이름
전호(after/before) 동작(insert/update/delete)
on 테이블명
for each row
*/

select * from emp1;

delimiter $$
create trigger insert_emp_trig
after insert
on emp1
for each row
begin
	set @msg = concat(new.name, '님 새로 추가됨');
end$$
delimiter ;
# emp1에 insert할 때마다 실행된다.

insert into emp1 values(300, 'aaa', 10000, 80);
select @msg;

create table emp1_backup(
num int auto_increment primary key,
id int,
cmd varchar(20),
old_sal int,
new_sal int
);

delimiter $$
create trigger emp1_trig1
after insert
on emp1
for each row
begin
	insert into emp1_backup(id, cmd, new_sal) 
    values(new.emp_id, 'insert', new.sal);
end$$
delimiter ;

insert into emp1 values(301, 'bbb', 15000, 80);
select @msg;

select * from emp1_backup;

delimiter $$
create trigger emp1_trig2
after update
on emp1
for each row
begin
	insert into emp1_backup(id, cmd, old_sal, new_sal) 
    values(old.emp_id, 'update', old.sal, new.sal);
end$$
delimiter ;

update emp1 set sal = 24000 where emp_id = 145;

select * from emp1

delimiter $$
create trigger emp1_trig3
after update
on emp1
for each row
begin
	insert into emp1_backup(id, cmd, old_sal) 
    values(old.emp_id, 'delete', old.sal);
end$$
delimiter ;

delete from emp1 where emp_id >= 145 and emp_id < 150;

select * from member;
call get_member('C');

call mem_join('aaa', '111', 'namea', 'aaa@email.com');

call get_members();

call edit_member('aaa', '5678');

call del_member('C');