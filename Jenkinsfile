pipeline {
    agent any // This allows Jenkins to run on any available agent

    environment {
        // Define environment variables for SonarQube
        SONARQUBE_SERVER = 'CobraSonarqube' // The name of your SonarQube server configured in Jenkins
        SCANNER_HOME = tool 'SonarQubeScanner' // This should match the installation name in Jenkins
        GIT_HOME = tool 'Git' // Use the Git tool name
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from your GitHub repository using the Git tool
                    git branch: 'main', url: 'https://github.com/sthanubhav/CobraJenkins.git'
                }
            }
        }
        
        stage('Set Up Python Environment') {
            steps {
                script {
                    // Install dependencies directly without a virtual environment
                    sh 'pip install -r requirements.txt'
                    }
            }
        }


        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube analysis
                    withSonarQubeEnv(SONARQUBE_SERVER) {
                        sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=cobrasonarqube_lab1 -Dsonar.sources=. -Dsonar.host.url=http://10.0.0.246:9000 -Dsonar.login=sqp_3379bf214842a1a5c2aec0abf96d3f469452641b -Dsonar.exclusions=venv/**" // Adjust parameters as needed
                    }
                }
            }
        }

        stage('Run Tests for Landing App') {
            steps {
                script {
                    // Activate the virtual environment and run tests for the landing app
                    sh 'source venv/bin/activate && python manage.py test landing' // Run tests for landing app only
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add deployment steps if applicable (e.g., deploying to a server)
                    echo 'Deploying the application...'
                    // Example command for deployment
                    // sh 'your-deployment-command'
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
