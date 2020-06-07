# INSTAGRAM CLONE

## AUTHOR
- [Derrick Kiprop](https://github.com/derrokip34)

## PROJECT DESCRIPTION
This django app is a clone of the popular social media site Instagram with a few of its features

## SETUP AND USAGE INSTRUCTIONS
### Prerequisites
- A web browser
- Github account
- Terminal
- Python3.6
- Text editor software

#### Clone or download the zip file of this repository
- Clone by typing in the following command `git clone https://github.com/derrokip34/Instagram-clone.git`
- If you've downloaded the zip extract it in your preferred destination

#### Navigate into the project directory

#### Install python3.6 if not yet installed

##### Install virtual environment by typing the following command
`python3.6 -m venv --without-pip virtual`

#### Activate virtual environment
`source virtual/bin/activate`

#### Install pip
`curl https://bootstrap.pypa.io/get-pip.py | python`

#### Install dependencies by typing the following command
`pip install -r requirements.txt`

#### Create an `.env` file and edit it where appropriate
```bash
export SECRET_KEY=<your secret key>
export DB_NAME=<your database name>
export DB_USER=<your database username>
export DB_PASSWORD=<your database password>
export DEBUG=<True or False>
```
#### Run the following commands in your terminal
```bash
source .env
python3.6 manage.py runserver
```

#### Open 'http://127.0.0.1:8000/' in your browser and enjoy your app

## [IG-Clone Live site](https://ig-clone34.herokuapp.com/)

## BDD
### Input required
- Registration details or login details
- Image and image details for posting
- New user details when updating user profile

### Behaviour
- The user's details will be saved in a database upon registration
- Images will be saved in a databases after posting it
- User's details will be updated

### Output
- Images posted will be displayed on the homepage and profile page
- User's details will be shown on the profile page

## TECHNOLOGIES USED
- HTML
- CSS
- Bootstrap 4
- Material Design Bootstrap
- Python3.6
- Django
- Markdown
- Heroku
- PostgreSQL

## BUGS
There are no known bugs at the moment
In case of any bugs contact me at derrickip34@gmail.com

## LICENSE & COPYRIGHT INFORMATION
[MIT License](https://github.com/derrokip34/Instagram-Clone/blob/master/license.md)
