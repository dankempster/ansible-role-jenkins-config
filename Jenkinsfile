#!/usr/bin/env groovy

def SAFE_JOB_NAME = env.JOB_NAME.replace("/", "-").replace("%2F", "-")
def BASE_NAME = "${SAFE_JOB_NAME}${env.BUILD_NUMBER}"

def DISTRO_RASPBIAN_STRETCH = "${BASE_NAME}_rsp9"
def DISTRO_DEBIAN_9 = "${BASE_NAME}_deb9"

def MOLECULE_NAME_DEFAULT_RASPBIAN_STRETCH = "${DISTRO_RASPBIAN_STRETCH}_def".reverse().take(30).reverse().replaceAll("^[^a-zA-Z0-9]+", "")
def MOLECULE_NAME_DEFAULT_DEBIAN_9 = "${DISTRO_DEBIAN_9}_def".reverse().take(30).reverse().replaceAll("^[^a-zA-Z0-9]+", "")
def MOLECULE_NAME_CONFIGED_RASPBIAN_STRETCH = "${DISTRO_RASPBIAN_STRETCH}_con".reverse().take(30).reverse().replaceAll("^[^a-zA-Z0-9]+", "")
def MOLECULE_NAME_CONFIGED_DEBIAN_9 = "${DISTRO_DEBIAN_9}_conf".reverse().take(30).reverse().replaceAll("^[^a-zA-Z0-9]+", "")

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


        stage('Debian 9: Default') {
          agent {
            label 'x86_64'
          }

          steps {
            withAnt(installation: 'System') {
              sh "ant -f build.default.xml -Dmolecule.name=${MOLECULE_NAME_DEFAULT_DEBIAN_9} ci"
            }
          }

          post {
            failure {
              script {
                withAnt(installation: 'System') {
                  sh "ant -f build.default.xml -Dmolecule.name=${MOLECULE_NAME_DEFAULT_DEBIAN_9} destroy-safe"
                }
              }
            }
            always {
              junit 'build/**/reports/**/*.xml'
            }
          }
        }


        stage('Raspbian Stretch: Default') {
          agent {
            label 'raspberrypi_3'
          }

          steps {
            withAnt(installation: 'System') {
              sh "ant -f build.default.xml -Dmolecule.name=${MOLECULE_NAME_DEFAULT_RASPBIAN_STRETCH} ci"
            }
          }

          post {
            failure {
              script {
                withAnt(installation: 'System') {
                  sh "ant -f build.default.xml -Dmolecule.name=${MOLECULE_NAME_DEFAULT_RASPBIAN_STRETCH} destroy-safe"
                }
              }
            }
            always {
              junit 'build/**/reports/**/*.xml'
            }
          }
        }


        stage('Debian 9: Configured') {
          agent {
            label 'x86_64'
          }

          steps {
            withAnt(installation: 'System') {
              sh "ant -f build.configured.xml -Dmolecule.name=${MOLECULE_NAME_CONFIGED_DEBIAN_9} ci"
            }
          }

          post {
            failure {
              script {
                withAnt(installation: 'System') {
                  sh "ant -f build.configured.xml -Dmolecule.name=${MOLECULE_NAME_CONFIGED_DEBIAN_9} destroy-safe"
                }
              }
            }
            always {
              junit 'build/**/reports/**/*.xml'
            }
          }
        }


        stage('Raspbian Stretch: Configured') {
          agent {
            label 'raspberrypi_3'
          }

          steps {
            withAnt(installation: 'System') {
              sh "ant -f build.configured.xml -Dmolecule.name=${MOLECULE_NAME_CONFIGED_RASPBIAN_STRETCH} ci"
            }
          }

          post {
            failure {
              script {
                withAnt(installation: 'System') {
                  sh "ant -f build.configured.xml -Dmolecule.name=${MOLECULE_NAME_CONFIGED_RASPBIAN_STRETCH} destroy-safe"
                }
              }
            }
            always {
              junit 'build/**/reports/**/*.xml'
            }
          }
        }
        

      }
    }
  }
}
