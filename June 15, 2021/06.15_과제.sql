use encore;

## 2장

#2-1
#급여가 $12,000를 넘는 사원의 이름과 급여를 표시하는 질의를 작성하시오.

select last_name, salary
from employees
where salary > 12000;

#2-2
#사원번호가 176인 사원의 이름과 부서 번호를 표시하는 질의를 작성하시오.

select last_name, department_id
from employees
where employee_id = 176;

#2-3
#급여가 $5,000에서 $12,000 사이에 포함되지 않는 모든 사원의 이름과 급여를 표시하는 질의를 작성하시오.

select last_name, salary
from employees
where salary not between 5000 and 12000;

#2-4
#1998년 2월 20일과 1998년 5월 1일 사이에 입사한 사원의 이름, 업무 ID 및 시작일을 표시하되, 시작일을 기준으로 오름차순으로 정렬하시오.

select last_name, job_id, hire_date
from employees
where hire_date between date('2003-02-20') and date('2006-05-01')
order by hire_date asc;

#2-4 (2)
select last_name, job_id, hire_Date
from employees
where hire_date between date('2003-10-10') and date('2008-10-10')

#2-5
#부서 20 및 50에 속하는 모든 사원의 이름과 부서 번호를 이름을 기준으로 영문자순으로 표시하십시오.

select last_name, department_id
from employees
where department_id in(20, 50)
order by last_name;

#2-6
#급여가 $5,000와 $12,000 사이이고 부서 번호가 20 또는 50인 사원의 이름과 급여를 나열하도록 [3번 문제]을 수정 하고, 
#열 레이블을 Employee와 Monthly Salary로 각각 지정하여 실행하시오.

select last_name "Employee", salary "Monthly salary"
from employees
where salary between 5000 and 12000 and department_id in (20, 50);

#2-6 (2)
select last_name as Employee, salary as 'Monthly Salary', department_id
from employees
where salary between 5000 and 12000
and department _id in (20,50);

#2-7
#1994년에 입사한 모든 사원의 이름과 입사일을 표시하시오.

select last_name, hire_date
from employees
where date(hire_date) like '%06';

#2-8
#관리자가 없는 모든 사원의 이름과 업무를 표시하시오.

select last_name, job_id
from employees
where manager_id is null;

#2-9
#커미션을 받는 모든사원의 이름, 급여 및 커미션을 급여 및 커미션을 기준으로 내림차순으로 정렬하여 표시하시오.

select last_name, salary, commission_pct
from employees
where commission_pct is not null
order by salary desc, commission_pct desc;

#2-10
#이름의 세번째 문자가 a인 모든 사원의 이름을 표시하십시오.

select last_name
from employees
where last_name like '__a%';

#2-11
#이름에 a와 e가 있는 모든사원의 이름을 표시하십시오.

select last_name
from employees
where last_name like '%a%' and last_name like '%e%';

#2-12
#업무가 영업 사원 또는 사무원이면서 급여가 $2,500, $3,500 또는 $7,000가 아닌 모든 사원의 이름, 업무 및 급여를 표시하십시오.

select last_name, job_id, salary
from employees
where job_id in ('st_clerk', 'sa_rep')
and salary not in (2500, 3500, 7000);

#2-13
#커미션 비율이 20%인 모든 사원의 이름, 급여 및 커미션을 표시하도록 [6번 문제]을 수정하십시오

select last_name "Employee", salary "Monthly Salary", commission_pct "COMMISSION_PCT"
from employees
where commission_pct = 0.2;  # .2 입력 가능

## 4장
#4-1
#모든 사원의 이름, 부서 번호, 부서 이름을 표시하는 질의를 작성하십시오.
select e.last_name, e.department_id, d.department_name
from employees e 
join departments d
using (department_id);

#4-2
#부서 80에 속하는 모든 업무의 고유 목록을 작성하고 출력 결과에 부서의 위치를 포함시키십시오.

select distinct e.job_id, d.location_id
from employees e 
join departments d
using (department_id)
where e.department_id = 80; 

#4-2 (2)
select job_id, location_id
from employees join departments
using(department_id)
where department_id = 80;

#4-3
#커미션을 받는 사원의 이름, 부서 이름, 위치 ID 및 도시를 표시하는 질의를 작성하십시오.

select e.last_name, d.department_name, d.location_id, l.city
from employees e
join departments d
on d.department_id = e.department_id
join locations l
on d.location_id = l.location_id
where e.commission_pct is not null;

#4-4
#이름에 a(소문자)가 포함된 모든 사원의 이름과 부서 이름을 표시하시오.

select e.last_name, d.department_name
from employees e
join departments d
using (department_id)
where last_name like '%a%';

#4-5
#Toronto에서 근무하는 모든 사원의 이름, 업무, 부서 번호 및 부서 이름을 표시하는 질의를 작성하십시오.

select e.last_name, e.job_id, e.department_id, d.department_name
from employees e
join departments d
on d.department_id = e.department_id
join locations l
on d.location_id = l.location_id
where l.city = 'Toronto';

#4-5 (2)
select last_name, job_id, department_id, department_name
from employees join departments
using(department_id)
join locations
using(location_id)
where city = 'Toronto';

#4-6
#사원의 이름 및 사원 번호를 관리자의 이름 및 관리자 번호화 함께 표시하고 각각의 열 레이블을 Employee, Emp#, Manager, Mgr#로 지정하십시오.

select e1.last_name 'Employee', e1.employee_id 'Emp#', 
e2.last_name 'Manager', e2.employee_id 'Mgr#'
from employees e1
join employees e2
on e1.manager_id = e2.employee_id			
order by e2.employee_id;					
​
#4-6 (2)
select e.employee_id as 'EMP#', e.last_name as Employee,
m.employee_id as 'Mgr#', m.last_name as MAnager
from employees e join employees m
on e.manager_id = m.employee_id;


#4-7
#6번을 수정하되 King을 포함하여 관리자가 없는 모든 사원을 표시하도록 하고 결과를 사원 번호를 기준으로 정렬하십시오.

select e.employee_id as 'EMP#', e.last_name as Employee,
m.employee_id as 'Mgr#', m.last_name as Manager
from employees e left outer join employees m
on e.manager_id = m.employee_id;

#4-8
#지정한 사원의 이름, 부서 번호 및 지정한 사원과 동일한 부서에서 근무하는 모든 사원을 표시하도록 질의를 작성하고 각 열에 적합한 레이블을 지정하십시오.

select e.last_name, e.department_id, c.last_name as colleague
from employees e join employees c
on e.department_id = c.department_id
where e.last_name <> c.last_name;

#4-9
#JOB_GRADES 테이블의 구조를 표시하고 모든 사원의 이름, 업무, 부서 이름, 급여 및 등급을 표시하는 질의를 작성하십시오.

desc job_grades;
select last_name, job_id, department_name, salary, gra
from employees join deaprtments
using(department_id)
join job_grads
on salary between lowest_sal and highest_sal;

#4-10
#Davies라는 사원보다 늦게 입사한 사원의 이름과 입사일을 표시하는 질의를 작성하십시오.

select e2.last_name, e2.hire_date
from employees e1 join employees e2
on e1.hire_date < e2.hire_date
where e1.last_name = 'Davies';

#4-11
#관리자보다 먼저 입사한 모든 사원의 이름 및 입사일을 관리자의 이름 및 입사일과 함께 표시하고 
#열 레이블을 각각 Employee, Emp Hired, <anager, Mgr Hired로 지정하십시오.

select e.last_name as Employee, e.hire_date as 'Emp Hired', 
m.last_name as Manager, m.hire_date as 'Mgr Hired'
from employees e join employees m
on e.hire_date < m.hire_date;