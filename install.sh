msf_6 () {
        apt update
        apt update --fix-missing
	apt install perl libllvm protobuf c-ares libltdl glib libandroid-shmem libicu libyaml autoconf bison clang coreutils curl findutils apr apr-util postgresql openssl readline libffi libgmp libpcap libsqlite libgrpc libtool libxml2 libxslt ncurses make ruby ncurses-utils ncurses git wget unzip zip tar termux-tools termux-elf-cleaner resolv-conf pkg-config -y
}

if [ "$1" == 'msf' ];
then
	msf_6
else
	apt install neofetch python -y
	python3 -m pip install requests
fi
