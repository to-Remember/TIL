/*
<테이블 생성>
create table 이름(
컬럼명 타입(크기) [제약조건].
컬럼명 타입(크기) [제약조건].
컬럼명 타입(크기) default '기본값'
); 

<타입>
정수: int(integer)
실수: float
문자: char(크기) - 고정크기 / varchar(키기) - 가변크기
대용량 텍스트: longtext(4GB)
날짜: date(년-월-일) / datetime(년-월-일 시:분:초)
*/

create table test2(
num int auto_increment primary key, #컬럼 이름이 num 데이터 타입이 auto_increment자동으로 값 할당.
name varchar(29) not null,
addr varchar(50)default '서울',  #default 는 기본값
w_date datetime default now(),
msg varchar(200)
);

desc test2;

insert into test2(name, msg) values('aaa','hello');
insert into test2(name, addr, msg) values('aaa', '인천', 'hello');

select * from test2;

#테이블 수정: 테이블 구조 변경. -> 컬럼 추가, 삭제, 컬럼의 타입이나 크기
/*
컬럼추가
alter table 테이블명
add(컬럼명 타입(크기))
*/
alter table test2
add (pwd varchar(10));

desc test2;

/*
컬럼변경(타입이나 크기 변경)
alter table 테이블명
modify 컬럼명 새타입(새크기);
*/

alter table test2
modify pwd varchar(20);

 /*
 컬럼 삭제
 alter table 테이블명
 drop column 컬럼명;
 */
 
 alter table test2
 drop column pwd;
 
 /*
 컬럼명 변경
 alter table 테이블명
 change 원컬럼명 새컬럼명 타입;
 */
 
 alter table test2
 change msg hello_msg varchar(200);
 
 alter table test2
 add (col1 char(10));

 alter table test2
 add (col2 char(10));

/*
alter table test2
drop column col1, col2; -> 한번에 여러개 삭제 불가
 */
 
 #테이블 이름 변경
 alter table test2
rename new_test2;
 
select * from new_test2;
delete from new_test2; #delete는 rollback이 된다.
rollback;

truncate table new_test2; #전체행 삭제. rollback 안됨.

desc new_test2;

#게시판(num, writer, w_date, title, content). 회원가입(id, pwd, name, email)
create table member(
id varchar(20) primary key, #줄의 대표값
pwd varchar(20) not null, #null은 허용 안한다는 제약조건
name varchar(20) not null, 
email varchar(100) unique #중복 불가
);

insert into member value('A', '1111', 'Aa', 'Aa@');
insert into member value('B', '2222', 'Bb', 'Bb@');
insert into member value('C', '3333', 'Cc', 'Cc@');

#게시판(num, writer, w_date, title, content)
create table board(
num int auto_increment primary key,
writer varchar(20),
w_date datetime,
title varchar(50),
content varchar(500),
constraint foreign key(writer) references member(id)
);

insert into board(writer, w_date, title, content) 
values('A', sysdate(), 'title1', 'content1');

insert into board(writer, w_date, title, content) 
values('B', sysdate(), 'title2', 'content2');

#delete from member where id = 'B'; -> 이미 글을 작성한 후라 실행 안됨. 보드에서 참조하고 있기에. 그러므로 먼저 보드에서 글으 삭제한 후 삭제 가능

delete from board where writer = 'B';
delete from member where id = 'B';

select * from member;
select * from board;

#테이블 삭제
drop table board;
#on delete cascade: 부모 테이블의 행 삭제시 이 줄을 참조하는 모든 줄을 같이 삭제
create table board(
num int auto_increment primary key,
writer varchar(20),
w_date datetime,
title varchar(50),
content varchar(500),
constraint foreign key(writer) references member(id) on delete cascade
);

insert into board(writer, w_date, title, content) 
values('B', sysdate(), 'title2', 'content2');

drop table board;
#on delete set null: 부모 테이블의 행 삭제시 이 줄을 참조하는 모든 줄을 같이 삭제
create table board(
num int auto_increment primary key,
writer varchar(20),
w_date datetime,
title varchar(50),
content varchar(500),
constraint foreign key(writer) references member(id) on delete set null
);

insert into board(writer, w_date, title, content) 
values('B', sysdate(), 'title2', 'content2');

select * from board;

delete from member where id = 'ccc';
