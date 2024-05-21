#!/usr/bin/env bash

# Global variable
nc="--noconfirm"

# Verify if needed packages are alread installed
get_and_install_pkgs() {
	if pacman -Qs git > /dev/null; then
		echo "pacote git já instalado"
	else
		sleep 1
		echo "Instalando git"
		sleep 1
		sudo pacman -S $nc git
		echo "git instalado!"
	fi

	if pacman -Qs base-devel > /dev/null; then
		echo "pacote base-devel já instalado"
	else
		sleep 1 
		echo "Instalando base-devel"
		sleep 1
		sudo pacman -S $nc base-devel
		echo "Pacote instalado!"
	fi
}

# Install Yay
install_yay() {
	echo "Instalando Yay"
	sleep 1
	cd ~/Downloads && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si $nc
	sleep 1

	yay -Y --gendb
	yay -Syu $nc --devel
	yay -Y --devel --save
	yay -Syu $nc

}

# Remove yay trash
remove_yay_trash() {
	echo "Removendo pasta git do yay"
	sleep 1
	rm -rf ~/Downloads/yay
	echo "Yay instalado e configurado!"
}

get_and_install_pkgs
install_yay
remove_yay_trash
 
