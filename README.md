# Example Django REST and React Restaurant App

Client/server application to show the menu of a restaurant from a browser

### Prerequisites

- python 3 (as `python`, else replace all example `python` commands with `python3`)
- npm


### Getting Started

- Clone this repo
`git clone https://github.com/mdaizovi/restaurant_repo.git`


#### Back End
- Change to backend directory: 
  `cd restaurant_repo/back_end`

- Make a Virtual Environment: 
  `python -m venv venv`

- Activate virtual environment:
  `source venv/bin/activate`

- Install backend requirements:
  `pip install -r requirements.txt`

- Copy the example .env file: 
  `cp restaurant/.env.example restaurant/.env`

- Run initial migrations, to prepare database:
  `python manage.py migrate`

- Make yourself a super user:
  `python manage.py createsuperuser`

  - You will be prompted by Django to create a super user, and you can use these credentials to log into the admin interface (more in next step)

- Make Menu Items (optional)

  - First, run the Django server: `python manage.py runserver`

  - Next, navigate to the [Admin](http://localhost:8000/admin)
  - Log in with the credentials you just created, and create [Menu Items](http://localhost:8000/admin/menu/menuitem/)

#### Front End
- In another terminal,
  - navigate to `restaurant_repo/front_end/` (EX: run `cd ../front_end`, if you are currently in `restaurant_repo/back_end`)
  - run `npm install`

### Running The App
- from the Activate virtual environment:
`source venv/bin/activate`

- Run the Django backend server.
  - From `restaurant_repo/back_end/`, run :`python manage.py runserver`

- Run React
  - In another terminal, navigate to 'restaurant_repo/front_end/' (EX: `cd front_end`)
  - run `npm start`


- In your browser, navigate to [http://localhost:3000/](http://localhost:3000/)


## Running the tests

- From your virtual environment, run `python manage.py test`
