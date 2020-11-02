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

## Docker commands
> `sudo docker run -it aman/ccs /bin/bash`
- `-it` is used to make the container run in interactive mode
- `aman/ccs` is the image name for easier access.

> `sudo docker build .`
- To create image usind Dockerfile

> To get the IP address of the docker
`sudo docker inspect container_id(fba765bc9744) | grep IPAddress | cut -d '"' -f 4 | head -n 2 | tail -n 1`



## Update on project
1. Built a Ubuntu container which even after installing old openssl is still secure.
2. Built a debian container with old openssl and libssl but cannot build `debian:wheezy` so the oldest one I can do is stretch without updates breaking
3. Built a pre-packaged debian container specially designed for vulnerability testing.
    - Used a Kali docker container to make sure the docker created in `3` is vulnerable to openssl.