pipeline {
    agent any

    environment {
        VENV_DIR = '.jenkins_venv'
    }

    parameters {
        string(name: 'tags', defaultValue: '', description: 'Optional behave tag filter, e.g. "download_page" or "homepage"')
        string(name: 'test_dir', defaultValue: 'Features', description: 'Directory containing feature files')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup virtualenv') {
            steps {
                sh 'python3 -m pip install --user virtualenv'
                sh 'python3 -m virtualenv ${VENV_DIR}'
                sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                script {
                    def tagFilter = params.tags ? "--tags=${params.tags}" : ''
                    sh ". ${VENV_DIR}/bin/activate && python3 runner.py --behave_options='${tagFilter} --color --logcapture' --output_html=yes --test_dir=${params.test_dir}"
                }
            }
        }

        stage('Archive reports') {
            steps {
                archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}
