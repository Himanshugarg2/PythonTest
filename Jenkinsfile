pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-repo/python-selenium-tests.git', branch: 'main'
            }
        }
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
    post {
        always {
            junit '**/pytest*.xml'
        }
    }
}
