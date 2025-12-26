pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aya8-01/restaurant-recommendation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t restaurant-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f restaurant-container || true
                docker run -d -p 5000:5000 --name restaurant-container restaurant-app
                '''
            }
        }
    }
}

