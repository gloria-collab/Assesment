INSERT INTO DEPARTMENT(Label, Manager_Name) VALUES 
(1,"IT","Alice Johnson"),
(2,"HR","Bob smith"),
(3,"Marketing", "Clara Bennett");

INSERT INTO Employee(Name,Position, Salary, Department_Num) VALUES
("John Doe","Developer",60000.00,1),
("Jane Smith","Analyst",55000.00,2),
("Mike Brown","Designer",55000.00,3),
("Sarah Johnson", "Data Scientist",70000,1),
("Emmma Watson","HR Specialist",52000,2);

INSERT INTO Project(Title, Start_Date, End_Date,Department_Num_S ) VALUES
("Website Redesign", "2024-01-15","2024-06-30",1),
("Employee Onboarding", "2024-03-01","2024-09-01",2),
("Market Research", "2024-02-01","2024-07-31",3),
("IT Infastructure Setup", "2024-04-01","2024-12-31",1);

INSERT INTO Employee_Project  (Employee_Num_E , Project_Num_P, Roles) VALUES
(101,201,"Frontend Developer"),
(104,201,"Backend Developer"),
(102,202,"Trainer"),
(105,202,"Cordinator"),
(103,203,"Research Lead"),
(101,204,"Network Specialist");

UPDATE Employee_Project
Set Role = "Full Stack Developer"
where Employee_Num_E = 101;


delete from Employee_Project
    where Employee_Num_E = 103;





