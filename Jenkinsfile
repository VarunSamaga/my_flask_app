pipeline {
    agent any  

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VarunSamaga/my_flask_app.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'  
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m unittest discover -s tests'
            }
        }
    }

    post {
        success {
            echo 'Tests successful'
        }
        failure {
            echo 'Tests failed'
        }
        always {
            echo 'Cleaning up...'
        }
    }
}
