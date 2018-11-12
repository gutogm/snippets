# rsync + termux
## instalar rsync no termux
rsync -r -a -v -e 'ssh -p 8022' ./roms u0_a11@192.168.0.87:~/roms

## ERROR with ssh + termux
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~