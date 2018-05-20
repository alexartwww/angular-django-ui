# Angular Django UI

## Goals and strategic fit

- Modern tech: Angular, Material Design, Django, DRF
- Easy to support


## Installation

```
# Install virtualenv and requirements
sudo apt install python3-pip
sudo pip3 install virtualenv virtualenvwrapper
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -p python3 angular-django-ui
workon angular-django-ui
pip3 install -r requirements.txt

# Install npm and requirements
cd ./ui
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm i -g npm
npm i
```

You awesome!
