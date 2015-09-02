wget -P ~/.local/lib https://bootstrap.pypa.io/get-pip.py; python ~/.local/lib/get-pip.py --user
printf "\nPATH=\$PATH:~/.local/bin/" >> ~/.bashrc
source ~/.bashrc
pip install pytest --user  
