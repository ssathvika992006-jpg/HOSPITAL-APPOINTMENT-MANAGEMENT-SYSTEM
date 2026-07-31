pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'echo Building Hospital Appointment Management System'
            }
        }

        stage('Test') {
            steps {
                bat 'echo Testing Hospital Appointment Management System'
            }
        }

        stage('Deploy') {
            steps {
                bat 'echo Deploying Hospital Appointment Management System'
            }
        }
    }

    post {
        success {
            echo 'Build, Test and Deploy completed successfully'
        }

        failure {
            echo 'Pipeline Failed'
        }
    }
}