pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Repository cloned'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python test.py'
            }
        }

        stage('Run') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
