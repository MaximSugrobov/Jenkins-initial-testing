pipeline {
    agent any
    stages {
    stage('test') {
      steps {
        echo 'testing the app...'
        bat 'python test_hw1.py'
      }
    }

    stage('run') {
      steps {
        echo 'running the app...'
        bat 'python hw2_1.py'
      }
    }

  }

}
