pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/transcend-all/jenkins-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-pyspark-demo .'
            }
        }

        stage('Run PySpark Job') {
            steps {
                sh 'docker run --rm jenkins-pyspark-demo'
            }
        }
    }
}
