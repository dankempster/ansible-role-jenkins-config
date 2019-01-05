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

            ansiColor('xterm') {
              sh '''
                virtualenv virtenv
                source virtenv/bin/activate

                tput colors

                export ANSIBLE_FORCE_COLOR=true

                pip install --upgrade ansible molecule docker jmespath

                molecule -e molecule/debian9_env.yml test
              '''
            }
          }          
        }

        stage('Raspbian Stretch') {
          agent {
            label 'raspberrypi_3'
          }
          steps {
            sh '''
              virtualenv virtenv
              source virtenv/bin/activate
              pip install --upgrade ansible molecule docker jmespath
          
              molecule -e molecule/raspbian_stretch_env.yml test
            '''
          }
        }
      }
    }
  }
}
