wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py --user
printf "\nPATH=\$PATH:~/.local/bin" >> ~/.bashrc
source ~/.bashrc
pip install pytest --user  