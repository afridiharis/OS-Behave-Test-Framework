pipeline {
    agent any

    environment {
        VENV_DIR = '.jenkins_venv' // This is the name of the virtual environment needed to activate
    }

    stages {
        stage('Clone Test Framework Repository') {
            steps {
                // clone the git repository
                git branch: 'main', url: 'https://github.com/afridiharis/OS-Behave-Test-Framework'
            }
        }

        stage('Setup Virtual Environment and install tools/packages') {
            steps {
                // This will setup the virtual environment however with every new sh command a new subprocess is called so virtual activate is needed
                sh 'python3 -m pip install virtualenv'
                sh 'python3 -m virtualenv ${VENV_DIR}'
                sh 'source ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // This will take in the two parameters or default to no tags and running all tests with the behave options specified in runner.py file
                script {
                    def tags = params.tags ?: ''
                    def testDir = params.test_dir ?: 'Features'
                    sh "source ${VENV_DIR}/bin/activate && python3 runner.py --behave_options='--tags=${tags} --color --logcapture' --output_html=yes --test_dir=${testDir}"
                }
            }
        }

        stage('Archive Reports') {
            steps {
                // This will archive the html report of the test run
                archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            // Delete the workspace after finishing for next clean run
            deleteDir()
        }
    }
}
