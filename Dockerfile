# init a base image (Alpine is small Linux distro)
FROM python:3.11-alpine
# define the present working directory
WORKDIR /potato
# copy the contents into the working dir
ADD . /potato
# upgrade pip
RUN pip install --upgrade pip
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD [ "python", "app.py" ]
