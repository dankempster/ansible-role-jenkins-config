#!/usr/bin/env groovy

pipeline {

  agent none

  stages {

    stage ('Test Distros') {
      parallel {

        stage('Debian 9') {
          agent {
            label 'x86_64'
          }
          steps {
            checkout scm

            sh '''
              virtualenv virtenv
              source virtenv/bin/activate
              pip install --upgrade ansible molecule docker jmespath

              molecule -e molecule/debian9_env.yml test
            '''
          }          
        }
      }
    }
  }
}
