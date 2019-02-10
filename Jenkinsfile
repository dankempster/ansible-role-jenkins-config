#!/usr/bin/env groovy

pipeline {

  agent none

  environment {
    ANT_ARGS = '-logger org.apache.tools.ant.listener.AnsiColorLogger'
  }

  stages {

    stage ('Test Distros') {
      parallel {

        stage('Debian 9') {
          agent {
            label 'x86_64'
          }
          steps {
            checkout scm

            withAnt(installation: 'System') {
              sh "ant virtenv"
            }

            sh '''
              source virtenv/bin/activate

              molecule -e ./molecule/debian9_env.yml test
            '''
          }
          post {
            always {
              junit 'build/reports/**/*.xml'
            }
          }
        }

        stage('Raspbian Stretch') {
          agent {
            label 'raspberrypi_3'
          }
          steps {
            withAnt(installation: 'System') {
              sh "ant virtenv"
            }

            sh '''
              source virtenv/bin/activate

              molecule -e ./molecule/raspbian_stretch_env.yml test
            '''
          }
          post {
            always {
              junit 'build/reports/**/*.xml'
            }
          }
        }
      }
    }
  }
}
