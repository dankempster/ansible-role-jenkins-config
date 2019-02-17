#!/usr/bin/env groovy

def SAFE_JOB_NAME = env.JOB_NAME.replace("/", "-").replace("%2F", "-")
def BASE_NAME = "${SAFE_JOB_NAME}${env.BUILD_NUMBER}"

def DISTRO_RASPBIAN_STRETCH = "${BASE_NAME}_rpi_stretch"
def DISTRO_DEBIAN_9 = "${BASE_NAME}_debian_9"

def MOLECULE_NAME_RASPBIAN_STRETCH = DISTRO_RASPBIAN_STRETCH.reverse().take(30).reverse()
def MOLECULE_NAME_DEBIAN_9 = DISTRO_DEBIAN_9.reverse().take(30).reverse()

pipeline {

  agent none

  environment {
    ANT_ARGS = '-logger org.apache.tools.ant.listener.AnsiColorLogger'
  }

  stages {

    stage('Prepare') {
      agent any

      steps {
        script {
          echo "BRANCH_NAME: ${env.BRANCH_NAME}"
          echo "CHANGE_ID: ${env.CHANGE_ID}"
          echo "CHANGE_BRANCH: ${env.CHANGE_BRANCH}"
          echo "CHANGE_TAG: ${env.CHANGE_BRANCH}"

          sh 'printenv'
        }
      }
    }


    stage ('Test') {
      parallel {


        stage('Debian 9') {
          agent {
            label 'x86_64'
          }

          steps {
            withAnt(installation: 'System') {
              sh "ant -Dmolecule.name=${MOLECULE_NAME_DEBIAN_9} test"
            }
          }

          post {
            failure {
              script {
                try {
                  withAnt(installation: 'System') {
                    sh "ant -Dmolecule.name=${MOLECULE_NAME_DEBIAN_9} destroy"
                  }
                } catch (Exception e) { }
              }
            }
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
              sh "ant -Dmolecule.name=${MOLECULE_NAME_RASPBIAN_STRETCH} test"
            }
          }

          post {
            failure {
              script {
                try {
                  withAnt(installation: 'System') {
                    sh "ant -Dmolecule.name=${MOLECULE_NAME_RASPBIAN_STRETCH} destroy"
                  }
                } catch (Exception e) { }
              }
            }
            always {
              junit 'build/reports/**/*.xml'
            }
          }
        }
      }
    }
  }
}
