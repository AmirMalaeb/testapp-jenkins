pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh """
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                sh """
                . venv/bin/activate
                pytest
                """
            }
        }
    }
}