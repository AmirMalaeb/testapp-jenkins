pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/AmirMalaeb/testapp-jenkins', branch: 'main'
                sh "ls -ltr"
            }
        }

        stage('Setup') {
            steps {
                sh "pip3 install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                sh "pytest"
            }
        }
    }
}