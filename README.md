## Cloud Computing Security Project

### Setting up docker on Ubuntu
1. To update all repos
    > `sudo apt update`

2. To install prerequisites
    > `sudo apt install \`<br/>
    > `apt-transport-https \`<br/>
    > `ca-certificates \`<br/>
    > `curl \`<br/>
    > `gnupg-agent \`<br/>
    > `software-properties-common \`<br/>

3. Adding docker's official GPG key:
    > `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

4. Setup docker's repo
    >`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu \`<br/>
    `$(lsb_release -cs) \`<br/>
    `stable"`<br/>

5. Install docker
    > `sudo apt install docker-ce docker-ce-cli containerd.io`

6. Test docker
    > `sudo docker run hello-world`