import art, os

art.tprint("Peshk0v", font="blubhead")

inpt1 = input("Install and config zsh? [Y/n] > ")
inpt2 = input("Install and config hypridle? [Y/n] > ")
inpt3 = input("Enable nvidia settings? [y/N] > ")
inpt4 = input("Install astraNeovim? [Y/n] > ")
inpt5 = input("Install WalMan(Wallpaper Manager)? [Y/n] > ")
inpt6 = input("Install WPS Office? [y/N] > ")

os.system("clear")
print("Installig archlinux dotfiles...")
print("Installing yay")
os.system("sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
print("Installig base packages")
os.system("sudo pacman -S hyprpaper git curl rofi nano brightnessctl pulseaudio waybar fastfetch kitty htop xorg swww nautilus nwg-look obsidian telegram-desktop discord nerd-fonts ttf-ubuntu-font-family ttf-font=awesome --needed")
print("Installig aur packages")
os.system("yay -S ttf-meslo-nerd-font-powerlevel10k zen-browser")
if not inpt1 == "N" or not inpt1 == "n":
    print("Installig oh my zsh")
    os.system("sudo pacman -S zsh --needed")
    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    print("Installig p10k-theme, plugins and config")
