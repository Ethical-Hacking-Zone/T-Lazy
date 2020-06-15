msf_6 () {
	pkg install -y autoconf bison clang coreutils curl findutils apr apr-util postgresql openssl readline libffi libgmp libpcap libsqlite libgrpc libtool libxml2 libxslt ncurses make ruby ncurses-utils ncurses git wget unzip zip tar termux-tools termux-elf-cleaner pkg-config

}

if [ "$1" == 'msf' ];
then
	msf_6
else
	pkg install -y neofetch python
	pip3 install requests
fi
