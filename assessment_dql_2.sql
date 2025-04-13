---Write a query to retrieve the names of employees who are assigned to more than one project, including the total number of projects for each employee.
select e.num_e, count(project_num_p) as total_project,e.name,e.position
from employee as  e
left join employee_project as ep
on e.num_e = ep.num_e
group by e.num_e

--Write a query to retrieve the list of projects managed by each department, including the department label and manager’s name

select d.label, d.manager_name, count(ep.project_num_p) as total_project
from employee_project as ep
left join employee as e
on ep.num_e = e.num_e
join department as d
on e.department_num_s = d.num_s
group by d.label, ep.project_num_p, d.manager_name;

--Write a query to retrieve the names of employees working on the project "Website Redesign," including their roles in the project.
select e.name, p.title, e.position, e.salary
from project as p
left join employee as e
on p.department_num_s = e.department_num_s
where title = 'Website Redesign'


---Write a query to retrieve the department with the highest number of employees, including the department label, manager name, and the total number of employees.
select d.label, d.manager_name, count(e.num_e) as number_employee
from employee_project as ep
left join employee as e
on ep.num_e = e.num_e
join department as d
on e.department_num_s = d.num_s
group by e.department_num_s, d.label, d.manager_name

--Write a query to retrieve the names and positions of employees earning a salary greater than 60,000, including their department names.
select *
from employee
where salary >= '60000'

--Write a query to retrieve the number of employees assigned to each project, including the project title.
select title, count(num_p) as number_project, e.name, e.position, count(num_e) as num_employee
from employee as e
left join project as p
on p.department_num_s = e.department_num_s
group by num_e, title, num_p

--write a query to retrieve a summary of roles employees have across different projects, including the employee name, project title, and role.
select *
from employee as e
left join project as p
on p.department_num_s = e.department_num_s

--Write a query to retrieve the total salary expenditure for each department, including the department label and manager name.
select  sum(e.salary) as total_salary, p.manager_name, p.label, p.num_s
from employee as e
left join department as p
on p.num_s = e.department_num_s
group by p.manager_name, p.label, p.num_s
order by p.label;
