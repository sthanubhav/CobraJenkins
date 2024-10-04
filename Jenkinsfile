pipeline {
    agent any

    environment {
        SONARQUBE_SERVER = 'CobraSonarqube' 
        SCANNER_HOME = tool 'SonarQubeScanner'
        GIT_HOME = tool 'Git'
        ZAP_API_KEY = 'cmhcdvblqj5iekdgc6ek6vjtcc' // Your ZAP API key
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from GitHub
                    git branch: 'main', url: 'https://github.com/sthanubhav/CobraJenkins.git'
                }
            }
        }
        
        stage('Set Up Python Environment') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv(SONARQUBE_SERVER) {
                        sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=cobrasonarqube_lab1 -Dsonar.sources=. -Dsonar.host.url=http://10.0.0.246:9000 -Dsonar.login=sqp_3379bf214842a1a5c2aec0abf96d3f469452641b -Dsonar.exclusions=venv/**"
                    }
                }
            }
        }

        stage('Run Tests for Landing App') {
            steps {
                script {
                    // Run tests for Django's landing app
                    sh 'python manage.py test landing'
                }
            }
        }

        stage('OWASP ZAP DAST Scan') {
            steps {
                script {
                    // Run OWASP ZAP scan for the Django app hosted at http://10.0.0.166:8000
                    sh """
                    curl "http://localhost:8081/JSON/ascan/action/scan/?apikey=$ZAP_API_KEY&url=http://10.0.0.166:8000/&recurse=true&inScopeOnly=true"
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying the application...'
                    // Add your deployment steps here if needed
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
