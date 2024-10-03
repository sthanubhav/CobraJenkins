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
                    sh "${GIT_HOME}/bin/git clone -b main https://github.com/sthanubhav/CobraJenkins.git" // Replace with your repo URL
                }
            }
        }
        
        stage('Set Up Python Environment') {
            steps {
                script {
                    // Set up a virtual environment for Python
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt' // Install dependencies
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube analysis
                    withSonarQubeEnv(SONARQUBE_SERVER) {
                        sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=cobrasonarqube_lab1 -Dsonar.sources=. -Dsonar.host.url=http://10.0.0.246:9000 -Dsonar.login=sqp_3379bf214842a1a5c2aec0abf96d3f469452641b" // Adjust parameters as needed
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run tests
                    sh 'source venv/bin/activate'
                    sh 'python manage.py test' // Run Django tests
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
