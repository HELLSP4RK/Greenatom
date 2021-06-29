pip install -U pip
pip install pipenv
pipenv install
pipenv run py project/manage.py makemigrations
pipenv run py project/manage.py migrate
echo 'Deploy DONE'
