# mushroom_classifier

# requirements  
docker installed

# Run on docker on local
docker build . -t {some tag name a}  -f ./Dockerfile 

docker run --rm --name test-api -p 5000:5000 -d {tag name a}

Results on : http://0.0.0.0:5000/

# Run on local with pipenv
can load environment from pipenv:

go to base directory and type: 1)pipenv install 2) pipenv run python wsgi.py

# call from an api 
example in request.py

go to base directory and type: pipenv run python application/request.py 
