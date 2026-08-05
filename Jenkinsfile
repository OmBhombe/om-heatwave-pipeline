pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/OmBhombe/om-heatwave-pipeline.git'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }

    }

    post {
        success {
            echo 'Build Successful!'
        }

        failure {
            echo 'Build Failed!'
        }
    }
}
