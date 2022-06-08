pipeline{
    agent any
    stages {
       stage ('checkout'){
          steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/test']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/naren-21/multipydemo.git']]])
                }
        }
       stage ('programe3'){
          steps { 
                git branch: 'test', credentialsId: 'test123', url: 'https://github.com/naren-21/multipydemo.git'
                sh 'python3 cmp.py'
                
                }
            }
        stage ('email'){
            steps {
                 mail bcc: '', body: 'descriptive pipeline program executed...', cc: 'dravi@stratapps.com,mmahesh@stratapps.com,vabhinav@stratapps.com', from: '', replyTo: '', subject: 'build success', to: 'duvvarapu.naren@gmail.com,dnkumar@stratapps.com'
                 }
            }
        }
   }
