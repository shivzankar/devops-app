pipeline {
  agent any
  environment {
    IMAGE = "shivzankar/devops-app"
    TAG   = "${env.BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build Image') { steps { sh 'docker build -t $IMAGE:$TAG .' } }
    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                         usernameVariable: 'U', passwordVariable: 'P')]) {
          sh 'echo $P | docker login -u $U --password-stdin && docker push $IMAGE:$TAG'
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        sh '''
          sed "s|IMAGE_PLACEHOLDER|$IMAGE:$TAG|" k8s/app.yaml | kubectl apply -f -
          kubectl rollout status deployment/devops-app --timeout=180s
          kubectl get pods -o wide
        '''
      }
    }
  }
  post { always { sh 'docker logout || true' } }
}
