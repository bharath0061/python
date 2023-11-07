pipeline {
    agent any
    stages {
        stage ('checkout') {
            steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/bharath0061/python.git']]])
            }            
        }
        stage ('Archive') {
            steps {
                withEnv(['WORKSPACE=${WORKSPACE}']) {
                 sh '${WORKSPACE}/README.sh' 
                }
            }
        }
    }
}


this is test commit
