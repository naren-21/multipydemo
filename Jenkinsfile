pipeline{
    agent any
    stages {
       stage ('checkout'){
          steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/naren-21/multipydemo.git']]])
                }
        }
       stage ('programe3'){
          steps { 
                git branch: 'main', credentialsId: 'test123', url: 'https://github.com/naren-21/multipydemo.git'
                sh 'python3 avg.py'
                
                }
            }
        stage ('email'){
            steps {
                 mail bcc: '', body: 'descriptive pipeline program executed...', cc: 'mrohini@stratapps.com,vabhinav@stratapps.com,klakshmansai@stratapps.com', from: '', replyTo: '', subject: 'build success', to: 'duvvarapu.naren@gmail.com,dnkumar@stratapps.com'
                 }
            }
        }
   }
