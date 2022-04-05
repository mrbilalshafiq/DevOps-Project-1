# Online Business Directory
> **_An online business directory with user-generated businesses_**

## Step-by-Step Guide
1. Update and install the necessary packages

         sudo apt update && sudo apt install pip mysql-client mysql-server gunicorn -y
         
2. Clone the repo

         git clone https://github.com/mrbilalshafiq/DevOps-Project-1     
         
3. Install the requirements

         pip3 install -r applications/requirements.txt
         
4. Log into MySQL

         sudo mysql -u root
         
5. Create the user which matches what is written in __init__.py

         CREATE USER 'bilalhalal'@'localhost' IDENTIFIED BY 'password';
         
6. Grant the necessary privileges to the newly created user

         GRANT ALL PRIVILEGES ON *.* TO 'bilalhalal'@'localhost';
         
7. Flush the privileges to update the privileges table

         FLUSH PRIVILEGES;
         
8. Create the database which matches the database name written in __init__.py

         CREATE DATABASE halalworlddb;
         
9. Exit out of MySQL

         EXIT

10. Create the tables

         python3 create.py
         
11. Start the app using Gunicorn (an alternative to the command below would be running "python3 app.py")

         gunicorn --workers=4 --bind=0.0.0.0:5000 app:app         

## Scope 
This project will be based upon:
* Project Management
* Python Fundamentals
* Python Testing
* Git
* Basic Linux
* Python Web Development
* Continuous Integration
* Cloud Fundamentals
* Databases

## CI Pipeline

![CIpipeline](https://github.com/mrbilalshafiq/halalworld/blob/main/images/Lucid.jpeg)
> Trello, Lucidchart, AWS, Flask, Git, Jenkins, Pytest, Gunicorn

## Evolution of Software Application Designs

### Design 1

When I was told to work on a project that I would be passionate about, I decided to make an online version of my family business, which is mainly a fruit & veg shop.

Therefore when constructing my entity relational database diagram, it was based on this business model.

![firsterd](https://github.com/mrbilalshafiq/halalworld/blob/main/images/Online%20Green%20Grocers%20(2).jpeg)
>My first ERD

### Design 2

However, when it came to coding the tables using SQLAlchemy I realised that 4 tables was too complex to begin with for my first flask project. I then decided to change the business model to another idea that I had whilst abroad for my honeymoon which was an online business directory specifically for hospitality & catering businesses that sold halal food, so that muslims can find halal take-aways and restaurants when in another country. 

This idea was perfect to be a CRUD application as I always envisioned it being a user-generated directory meaning that the user adds the business to a database to be displayed on the website.

![seconderd](https://github.com/mrbilalshafiq/halalworld/blob/main/images/halalworlderd.jpeg)
> My second ERD

### Design 3

Although with only 2 tables, the amount of columns were proving to be a hinderance when testing if my application was performing correctly as it was being built. I then decided to have the least amount of columns possible, which is following the concept of MVP (Minimum Viable Product).

![finalerd](https://github.com/mrbilalshafiq/halalworld/blob/main/images/Final%20ERD.jpeg)
> My final ERD


## Kanban/Trello Board

My kanban board displayed below shows, chornologically, the steps that I took to complete the application: creating the structure, seperating code into different files, creating models, then forms, then routes, then the html file and then repeating for each CRUD function until it became a fully functional CRUD application. I then performed unit tests in linux and in Jenkins. 

It also displayes the main hurdles and issues I came across that took the most time when trying to create the app.

![kanbanboard](https://github.com/mrbilalshafiq/halalworld/blob/main/images/Kanban.jpg)
>My completed trello board


## Testing & Deploying within Jenkins

After finishing writing the tests which gave me over 90% coverage, I configured Jenkins to run those tests within jenkins, which then produced a successful build.

I then configured the build to deploy the application using gunicorn as shown in the picture below.

![jenkins](https://github.com/mrbilalshafiq/halalworld/blob/main/images/testedanddeployed.png)
> As you can see just above; the application passed the unit tests and then was successfully deployed on jenkins.


## Risk Assessment

![RiskAssessment](https://github.com/mrbilalshafiq/halalworld/blob/main/images/Risk.jpg)
>This risk assessment shows a non-exhaustive list of potential risks.

## Future Improvements
1. Implementation of CSS & Javascript
2. Adding images and branding
3. Adding login functionality
4. Making the more secure in line with the principles of confidentiality, integrity and availability.
5. Make it more user friendly
6. Adding extra fields for user details and business details.
7. More thorough testing, aiming for 100% (currently at 91%).

## Conclusion
As my first flask application, I am pleased that it is fully functional with 91% test coverage. I actually wrote the code from scratch twice which has cemented the concepts required to develop the application. Excluding the python programming language, all the tools used were new to me. These include:
* Git
* Trello
* MySQL
* GCP/AWS
* Flask Framework
 * Pytest
 * Gunicorn
 * UnitTest
 * SQLAlchemy
 * WTForms
 * Jinja2
* Jenkins

I am also pleased with the process that I went through to create the app which is presented chronologically in my Trello board. The concepts clicked for me really quickly which has helped increase my confidence in my skills. The application itself is a MVP, minimum viable product, which is evident in the simplicity of design and use. It looks more like a skeleton of a website with CRUD functionality ready-to-go. Therefore this application could be built upon in the future, creating extra features and making it more user friendly and pleasing to the eye. I am concerned that there is no login functionality which means that anybody can edit and delete from the database but as this wasn't apart of the mark scheme, I decided to omit this from the app.

## Author
Mr. Bilal Shafiq


