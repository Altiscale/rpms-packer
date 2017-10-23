pipeline{
    agent any
    stages {
        stage('Git') {
            steps { 
              git branch: 'alti6', url: 'https://github.com/Altiscale/rpms-packer.git'
            }
        }
        stage('install alti build tools') {
            steps{
                sh '''
                  source $(rvm use --install --create 2.3.3@packer-rpm do rvm env --path)
                  gem install alti_build_tools'''
            }
        }
        stage('RVM') {
            steps {
                sh '''
                  source $(rvm use --install --create 2.3.3@packer-rpm do rvm env --path)

                  rm -f *rpm

                  # download
                  spectool -S packer.spec | awk '{print "wget",$NF}' | bash
                    
                  # name
                  name=`spectool -S packer.spec  | awk -F/ '{print $NF}'`
                    
                  alti_mock build -r centos6.7-x86_64 -s packer.spec -S ${name}                  
                '''
            }
        }
    }
}
