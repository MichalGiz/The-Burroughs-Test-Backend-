# The-Burroughs-Test-Backend

## Install

### Create an venv

`python3 -m venv venv`

### Activate venv and install packages

`source venv/bin/activate`

`pip install -r requirements.txt`

### Generate input data from random employee generator

`python3 ./generate_empl -o data.json -n 25` - where 25 can be replaced with desired amount of employees

### Create an docker container

`sudo docker build -t theburroughs .`

### Start docker container

`sudo docker run -dp 1980:1980 theburroughs`
Will start container and port 1980 will be used to access the API.

### API endpoints

`/salaries/{date}` where date format is yyyy-mm-dd
`/list` all employees input data

