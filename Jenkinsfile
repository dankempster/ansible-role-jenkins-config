#!/usr/bin/env groovy

pipeline {

  agent none

  stages {

    stage('Static Code Analysis') {
      agent {
        label 'raspberrypi_3'
      }
      steps {
        checkout scm

        sh '[ -d build/reports ] || mkdir -p build/reports'
        sh 'ansible-lint -p tasks/ > build/reports/ansiblelint.txt'
        sh 'yamllint -c yaml-lint.yml -f parsable . > build/reports/yamllint.txt'

        step([
          $class: 'ViolationsToGitHubRecorder',
          config: [
            gitHubUrl: 'https://api.github.com/',
            repositoryOwner: 'dankempster',
            repositoryName: 'ansible-role-jenkins-config',
            pullRequestId: '2',

            // Only specify one of these!
            credentialsId: 'com.github.dankempster.token',

            createCommentWithAllSingleFileComments: true,
            createSingleFileComments: true,
            commentOnlyChangedContent: true,
            minSeverity: 'INFO',
            keepOldComments: false,

            commentTemplate: """
            **Reporter**: {{violation.reporter}}{{#violation.rule}}

            **Rule**: {{violation.rule}}{{/violation.rule}}
            **Severity**: {{violation.severity}}
            **File**: {{violation.file}} L{{violation.startLine}}{{#violation.source}}

            **Source**: {{violation.source}}{{/violation.source}}

            {{violation.message}}
            """,

            violationConfigs: [
              [ pattern: 'build/reports/ansiblelint\\.txt$', parser: 'FLAKE8', reporter: 'AnsibleLint' ], 
              [ pattern: 'build/reports/yamllint\\.txt$', parser: 'YAMLLINT', reporter: 'YAMLLint' ], 
            ]
          ]
        ])
      }
    }

    stage ('Test Distros') {
      parallel {

        stage('Debian 9') {
          agent {
            label 'x86_64'
          }
          steps {
            checkout scm

            sh '[ -d build/reports ] || mkdir -p build/reports'

            sh '''
              virtualenv virtenv
              source virtenv/bin/activate
              pip install --upgrade ansible molecule docker jmespath xmlunittest

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
            checkout scm
            sh '[ -d build/reports ] || mkdir -p build/reports'

            sh '''
              virtualenv virtenv
              source virtenv/bin/activate
              pip install --upgrade ansible molecule docker jmespath xmlunittest
          
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
