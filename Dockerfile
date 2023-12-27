FROM python:3.10
EXPOSE 5000
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

#running the docker so it does not need to be restarted everytime
#docker run -dp 5005:5000 -w /app -v ${PWD}:/app restflask
#RUN THIS ON POWERSHELL ON WINDOWS IT WORKS!


