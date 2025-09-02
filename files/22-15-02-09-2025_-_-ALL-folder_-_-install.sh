sudo apt update
sudo apt install openssh-server
udo systemctl enable ssh 
sudo systemctl start ssh
sudo ufw allow ssh
hostname -I
