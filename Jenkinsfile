pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Himanshugarg2/PythonTest.git', branch: 'main'
            }
        }
        stage('Setup Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest --maxfail=1 --disable-warnings --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}
