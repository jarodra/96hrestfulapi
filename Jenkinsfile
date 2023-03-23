pipeline {
    agent any
	environment {
        def img = ("${env.JOB_NAME}:${env.BUILD_ID}").toLowerCase()
    }

    stages {
		stage('Checkout') {
			steps {
				git branch: 'main', url: 'https://github.com/Durgrim/96hrestfulapi.git'
			}
		}
        stage('Build') {
            steps {
				echo "## Building our image ##"
				script {
					sh 'docker-compose build'
                }
            }
		}
      

        stage('Deploy Run') {
            steps {
				echo "## Deploy and Run ##"
				script {
                sh 'docker-compose up -d'
                }
            }
        }
	}
}
