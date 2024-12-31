pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/AmirMalaeb/testapp-jenkins.git', branch: 'main'
                sh "ls -ltr"
            }
        }

        stage('Setup') {
            steps {
                sh """
                python3 -m venv venv
                . venv/bin/activate
                pip3 install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                sh "pytest"
            }
        }
    }
}