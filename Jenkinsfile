pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build & Start Stack') {
      steps {
        sh 'docker-compose down --remove-orphans || true'
        sh 'docker-compose build --no-cache'
        sh 'docker-compose up -d'
      }
    }
    stage('Verify') {
      steps {
        sh 'docker ps --filter "name=delivery_metrics" --filter "name=prometheus" --filter "name=grafana"'
      }
    }
  }
}    
