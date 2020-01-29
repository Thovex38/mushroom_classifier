# mushroom_classifier

# requirements  
docker installed or pipenv

# Run on docker on local
1) from base directory build the image: docker build . -t {some tag name a}  -f ./Dockerfile

1') Alternatively you can pull the image from my docker hub account: docker pull germai83/test-mushroom-api

2)docker run --rm --name {name of the instance} -p 5000:5000 -d {tag name of the docker image}

Results on : http://0.0.0.0:5000/

# Run on local with pipenv
can load environment from pipenv:

go to base directory and type: 1)pipenv install 2) pipenv run python wsgi.py

# call from an api 
example in request.py

go to base directory and type: pipenv run python application/request.py 
