# Halal World
> **_A business directory specifically for halal restaurants/take-aways_**

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


## Testing within Jenkins

After finishing writing the tests which gave me over 90% coverage, I configured Jenkins to run those tests within jenkins, which then produced a successful build.

I then configured the build to deploy the application using gunicorn as shown in the picture below.

![jenkins](https://github.com/mrbilalshafiq/halalworld/blob/main/images/testedanddeployedonjenkinsusinggunicorn.png)
> As you can see just above; the application passed the unit tests and then was successfully deployed on jenkins.
