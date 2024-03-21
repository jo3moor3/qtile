#!/bin/sh
feh --bg-scale ~/Pictures/coolcat.png
#picom & disown

# --experimental-backends --vsync should prevent screen tearing on most setups if needed

#SpaceNav Xorg fix
#sudo cp ~/.Xauthority /root/
#sudo spnavd_ctl x11 start
#sudo systemctl restart spacenavd

#Launch the emacs daemon (:
#/usr/bin/emacs --daemon & disown

# Low battery notifier (Taken out for desktop config)
#~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
#eos-welcome & disown

#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME


#Launch volume icon
#volumeicon & disown
#dfiujfdi
#Launch Night Light
#redshift-gtk & disown

#Disable middle click paste
#xmousepasteblock & disown
#Launch Albert
#albert & disown
