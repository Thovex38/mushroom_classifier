# mushroom_classifier

# requirements  
docker installed

# Run on docker 
docker pull germai83/test-mushroom-api
docker run --rm --name {some tag name} -p 5000:5000 -d germai83/mushroom_classifier

# Run on local
can load environment from pipenv:
go to base directory and type: 1)pipenv install 2) pipenv run python wsgi.py

# call from an api 
example in request.py
