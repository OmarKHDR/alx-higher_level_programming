sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get -y --force-yes install gdb
gdb -v
sudo add-apt-repository --remove ppa:ubuntu-toolchain-r/test
sudo apt-get update