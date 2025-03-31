FROM ubuntu
RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install flask
COPY  app.py /opt/app.py
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]