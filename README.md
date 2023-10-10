# speech-recognition-app

Deploying on EC2:


Clone the repository on your EC2 instance:


git clone https://github.com/priya141/speech-recognition-app.git
Navigate to the app directory:


cd speech-recognition-app
Build the Docker image:


docker build -t my-flask-app .
Run the Docker container:

docker run -p 80:80 my-flask-app
Access your Flask application:
Open a web browser and go to http://your-ec2-ip. You should see the Speech Recognition and Text-to-Speech application.

