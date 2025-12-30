pipeline {
    agent any

    environment {
        IMAGE_NAME = "ai-task-platform"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage("Checkout") {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Manoji0702/ai-task-platform.git'
            }
        }

        stage("Build Docker Image") {
            steps {
                bat """
                docker build -t %IMAGE_NAME%:%IMAGE_TAG% .
                """
            }
        }

        stage("Run Container (Test)") {
            environment {
                OPENAI_API_KEY = credentials('openai-api-key')
            }
            steps {
                bat """
                docker run -d --rm ^
                  -e OPENAI_API_KEY=%OPENAI_API_KEY% ^
                  -p 9000:8000 ^
                  --name ai-task-test ^
                  %IMAGE_NAME%:%IMAGE_TAG%
                """
            }
        }
    }

    post {
        always {
            bat "docker stop ai-task-test || exit 0"
        }
    }
}
