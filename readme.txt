please flollow the provided tips to review the project:
After maiking the migrations and run the server:
1* for "Does the web application use Django to serve static HTML content?"
to test go to the link:
http://localhost:8000/api/
2*Has the learner committed the project to a Git repository?
go to the link
https://github.com/Safia-gif/LittleLemon.git
3*Does the application connect the backend to a MySQL database?
you can be sure by doing the migrations sucssfully
4*Are the menu and table booking APIs implemented?
to test menu go to the link
http://localhost:8000/api/menu-items/
and 
http://localhost:8000/api/menu-items/1
for testing booking go to the 
http://localhost:8000/api/booking/tables/
and 
http://localhost:8000/api/booking/tables/2
5*Is the application set up with user registration and authentication?
you can register new user by the follwoing link
http://localhost:8000/api/users/
then test authanenticaation by the follwoing link
http://127.0.0.1:8000/auth/token/login/
6*Does the application contain unit tests?
by running the python manage.py test you will be sure by OK result
7*Can the API be tested with the Insomnia REST client?
you can follow this link and make sure it can be tested by Insomnia
https://www.coursera.org/learn/back-end-developer-capstone/supplement/OGeJJ/exercise-testing-the-api-using-insomnia