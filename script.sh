#!/bin/sh
#=========================================================

#=========================================================
echo "Install the packages..."
#=========================================================
sudo apt-get update
sudo apt-get -y install fluxbox xorg unzip vim default-jre rungetty firefox python-pip python-dev build-essential libffi-dev libssl-dev python3-pip
sudo -s -H pip install selenium requests pyopenssl ndg-httpsclient pyasn1 
sudo -s -H pip install --upgrade pyopenssl ndg-httpsclient pyasn1 pip
sudo apt-get -y install python-dev && apt-get install build-essential
sudo -s -H pip install --upgrade setuptools
sudo -s -H pip install ez_setup
sudo -s -H easy_install -U setuptools
sudo -s -H pip3 install python3-xlib
sudo apt-get -y install scrot
sudo apt-get -y install python3-tk
sudo apt-get -y install python3-dev
sudo -s -H pip install Image
sudo -s -H pip install python-xlib
sudo apt-get -y install libjpeg-dev
sudo apt-get -y install zlib1g-dev
sudo apt-get -y install libpng-dev
sudo -s -H pip install pillow
sudo -s -H pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/
sudo -s -H pip install apscheduler
sudo ln -s /vagrant/chromedriver /usr/bin/chromedriver
# sudo -s -H pip install pyautogui

#=========================================================
echo "Set autologin for the Vagrant user..."
#=========================================================
sudo sed -i '$ d' /etc/init/tty1.conf
sudo echo "exec /sbin/rungetty --autologin vagrant tty1" >> /etc/init/tty1.conf

#=========================================================
echo -n "Start X on login..."
#=========================================================
PROFILE_STRING=$(cat <<EOF
if [ ! -e "/tmp/.X0-lock" ] ; then
    startx
fi
EOF
)
echo "${PROFILE_STRING}" >> .profile
echo "ok"

#=========================================================
echo "Download the latest chrome..."
#=========================================================
wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo rm google-chrome-stable_current_amd64.deb
sudo apt-get install -y -f

#=========================================================
echo "Download latest selenium server..."
#=========================================================
SELENIUM_VERSION=$(curl "https://selenium-release.storage.googleapis.com/" | perl -n -e'/.*<Key>([^>]+selenium-server-standalone-2[^<]+)/ && print $1')
wget "https://selenium-release.storage.googleapis.com/${SELENIUM_VERSION}" -O selenium-server-standalone.jar
chown vagrant:vagrant selenium-server-standalone.jar

#=========================================================
echo "Download latest chrome driver..."
#=========================================================
CHROMEDRIVER_VERSION=$(curl "http://chromedriver.storage.googleapis.com/LATEST_RELEASE")
wget "http://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
sudo rm chromedriver_linux64.zip
chown vagrant:vagrant chromedriver

#=========================================================
echo -n "Install tmux scripts..."
#=========================================================
TMUX_SCRIPT=$(cat <<EOF
#!/bin/sh
tmux start-server

tmux new-session -d -s selenium
tmux send-keys -t selenium:0 './chromedriver' C-m

tmux new-session -d -s chrome-driver
tmux send-keys -t chrome-driver:0 'java -jar selenium-server-standalone.jar' C-m
EOF
)
echo "${TMUX_SCRIPT}"
echo "${TMUX_SCRIPT}" > tmux.sh
chmod +x tmux.sh
chown vagrant:vagrant tmux.sh
echo "ok"

#=========================================================
echo -n "Install startup scripts..."
#=========================================================
STARTUP_SCRIPT=$(cat <<EOF
#!/bin/sh
~/tmux.sh &
xterm &
EOF
)
echo "${STARTUP_SCRIPT}" > /etc/X11/Xsession.d/9999-common_start
chmod +x /etc/X11/Xsession.d/9999-common_start
echo "ok"

#=========================================================
echo -n "Add host alias..."
#=========================================================
echo "192.168.33.1 host" >> /etc/hosts
echo "ok"

#=========================================================
echo "Reboot the VM"
#=========================================================
sudo reboot
