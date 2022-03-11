# Add base image
FROM python:latest
#set the directory
WORKDIR /Project
#copy directory contents including requirements.txt
COPY . .

RUN pip3 install -r requirements. 

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]