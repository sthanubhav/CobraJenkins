pipeline {
    agent any

    environment {
        SONARQUBE_SERVER = 'CobraSonarqube' 
        SCANNER_HOME = tool 'SonarQubeScanner'
        GIT_HOME = tool 'Git'
        ZAP_API_KEY = 'cmhcdvblqj5iekdgc6ek6vjtcc' // Your ZAP API key
        TARGET_URL = 'http://10.0.0.166:8000/' // Your target URL
        REPORT_DIR = 'zap-reports' // Directory for storing reports
        HTML_REPORT = "${REPORT_DIR}/zap_report.html" // Path for HTML report
        XML_REPORT = "${REPORT_DIR}/zap_report.xml" // Path for XML report
        ZAP_PATH = '/home/sthanubhav/Downloads/zap/zap.sh' // Path to the ZAP script
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
                    sh 'python3 manage.py test landing'
                }
            }
        }

        stage('Trigger ZAP Scan') {
            steps {
                script {
                    // Ensure ZAP is running
                    // (Assuming ZAP is already running)

                    // Wait a bit for ZAP to initialize
                    sleep 5
                    
                    // Check if the URL is accessible
                    def response = sh(script: 'curl -I http://10.0.0.166:8000/', returnStdout: true)
                    echo "Response: ${response}"

                    // Trigger the scan
                    def scanResponse = sh(script: 'curl -I "http://localhost:8081/JSON/ascan/action/scan/?apikey=cmhcdvblqj5iekdgc6ek6vjtcc&url=http://10.0.0.166:8000/&recurse=true&inScopeOnly=true"', returnStdout: true)
                    echo "Scan Response: ${scanResponse}"

                    // Handle scan response if needed
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
