

#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>


std::string MOUNTPOINT = "/mnt",
    TIMEZONE = "/usr/share/zoneinfo/America/New_York";

void cmd(std::string s){
    std::cout << "COMMENTED EXECUTION: " + s << std::endl;
    //system(s.c_str());
    
}

void cmds(std::vector<std::string> v){
    for (unsigned int i=0; i<v.size(); i++){
        cmd(v[i]);
    }
}

void part1(){
    std::string num, swapnum;
    std::cout << "make swap to NUM: /dev/sda<NUM>? [0 to pass]: ";
    std::cin >> swapnum;
    std::cout << "mount to what /dev/sda<NUM>?: ";
    std::cin >> num;

    if (swapnum != "0"){
        std::string s[] = {"sudo mkswap /dev/sda"+swapnum, "sudo mkswap /dev/sda"+swapnum};
        cmd(s[0]);
        cmd(s[1]);
    }
    
    std::vector<std::string> v = {
        "sudo mount /dev/sda" + num + " " + MOUNTPOINT,
        "pacstrap "+MOUNTPOINT+" base base-devel vim sudo links", //move part two executable to /mnt
        "pacstrap "+MOUNTPOINT+" grub-bios os-prober",
        "genfstab -p "+MOUNTPOINT+" >> "+MOUNTPOINT+"/etc/fstab",
        "arch-chroot "+MOUNTPOINT,
        
        
        //"sudo umount /mnt"; //test unmount
        //"reboot"; //login into root when upon boot up
    };
    cmds(v);
}

void part2(){
    std::string hostname_path = "/etc/hostname",
        hosts_path = "/etc/hosts",
        pacmanconf_path = "/etc/pacman.conf",
        region = "/etc/locale.gen";
        
    std::vector<std::string> v = {
        //add hostname to hostname_path
        "systemctl enable dhcpcd.service",
        //add hostname to end of line after localhost
        "sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup",
        //in pacman_conf_path, uncomment TotalDownload && uncomment multilib and the inlcude line below it
        "ln -s "+TIMEZONE+" /etc/localtime",
        //uncomment en_US.UTF-8 UTF-8 (or other region )
        "locale-gen",
        "mkinitcpio -p linux",
        "grub-mkconfig -o /boot/grub/grub.cfg",
        "grub-install /dev/sda",
        "passwd",
        //"exit" commented out for testing
        
    };
    cmds(v);
}

void part3(){
    std::string username;
    std::cout << "New user's username: " << std::endl;
    std::cin >> username;

    std::vector<std::string> v = {
        "useradd -m -g users -G lp,audio,video,storage,optical,scanner,games,power,network,wheel -s /bin/bash "+username,
        "passwd "+username,
        //visudo uncomment %wheel under root
        "pacman -Syy",
        "pacman -Syu",
        "rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist",
        //"exit" //login to username //commented out for testing
    };
    cmds(v);
}

void part4(){
    std::vector<std::string> v = {
        "sudo pacman -Syy",
        "sudo pacman -Syu",
        //set up pacaur
        "sudo pacman -S alsa-utils alsa-oss alsa-plugins pulseaudio",
        "alsamixer", //notify m for unmute and up arrow on first one, Esc to exit
        "sudo alsactl store",
        "sudo pacman -S ttf-dejavu ttf-droid ttf-cheapskate",
        "sudo pacman -S xorg-server xorg-server-utils xorg-utils xorg-xclock xorg-twm xterm xf86-video-vesa xorg-xinit mesa mesa-demos libgl xf86-video-ati",
        "startx", //notify left window and exit
        "sudo pacman -S gnome gnome-extra xfce4",
        "xinit /usr/bin/gnome-session" //notify to logout only testing
        "sudo systemctl enable gdm.service",
        //"reboot" //commented out for testing
        
    };
}

int main(){
    part1();
    part2();
    part3();
    part4();
}

/*
pacaur setup
* 
* #set up pacaur
links www.google.com
google -> AUR -> search -> PACKAUR -> first pacaur -> download cower and pacaur
#https://github.com/Spyhawk/pacaur/archive/4.1.21.tar.gz
tar -xzvf pacaur.tar.gz
tar -xzvf cower.tar.gz
sudo pacman -S curl yajl expac
cd cower
makepkg -s
sudo pacman -U *.xz
cd ../packaur
makepkg -s
sudo pacman -U *.xz
*/
