import art, os, pathlib
from colorama import Fore, Back, Style

print(pathlib.Path(__file__).parent.resolve())

art.tprint("Peshk0v", font="blubhead")

def checkinpt(inpt, type):
    if type == 1:
        if not inpt == "N" or not inpt == "n": return True
        else: return False
    else:
        if not inpt == "Y" or not inpt == "y": return False
        else: return True

def aprint(text, type=False):
    if type == False or type == 1:
        print(Back.BLUE)
        print(Fore.BLACK, text)
        
    if type == 2:
        print(Back.GREEN)
        print(Fore.BLACK, text)

    if type == 3:
        print(Back.RED)
        print(Fore.BLACK, text)

    print(Style.RESET_ALL)

inpt1 = input("Install and config zsh? [Y/n] > ")
inpt2 = input("Install and config hypridle? [Y/n] > ")
inpt3 = input("Install astroNeovim? [Y/n] > ")
inpt4 = input("Install WPS Office? [y/N] > ")

os.system("clear")
art.tprint("ArchLinux", font="blubhead")
aprint("Installig archlinux dotfiles...")
aprint("Installing yay...")
os.system("sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
aprint("Yay installed!", 2)
aprint("Move to repo folder")
os.system(f"cd {pathlib.Path(__file__).parent.resolve()}")
aprint("Installig base packages...")
os.system("sudo pacman -S cargo npm hyprpaper hyprshot hyprlock git curl rofi nano brightnessctl pulseaudio waybar fastfetch kitty htop xorg swww nautilus nwg-look obsidian telegram-desktop discord nerd-fonts ttf-ubuntu-font-family ttf-font-awesome")
aprint("Base packages installed!", 2)
aprint("Installig AUR packages...")
os.system("yay -S ttf-meslo-nerd-font-powerlevel10k wlogout grub-customizer")
aprint("Aur packages installed!", 2)
aprint("Applyng configs...")
os.system(f"rm -rf ~/.config/hypr")
os.system(f"cp -r {pathlib.Path(__file__).parent.resolve()}/.config/* {pathlib.Path.home()}/.config/")
aprint("Configs applied!", 2)
aprint("Setting rofi...")
os.system("~/.config/rofi/Themes/colors catppuccinmavue")
aprint("Rofi", 2)
aprint("Copy wallpapers folder")
if pathlib.Path(f"{pathlib.Path.home()}/Pictures").is_dir():
    os.system(f"cp -r {pathlib.Path(__file__).parent.resolve()}/data/Wallpapers {pathlib.Path.home()}/Pictures/")
else:
    os.mkdir(f"{pathlib.Path.home()}/Pictures/")
    os.system(f"cp -r {pathlib.Path(__file__).parent.resolve()}/data/Wallpapers {pathlib.Path.home()}/Pictures/")
aprint("Installig user selected packages...")
if checkinpt(inpt1, 1):
    aprint("Installig oh my zsh...")
    os.system("sudo pacman -S zsh --needed")
    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && exit')
    aprint("Installig p10k-theme, plugins and config")
    os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"')
    os.system('git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')
    os.system('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
    os.system(f"cp {pathlib.Path(__file__).parent.resolve()}/data/.zshrc ~/")
    os.system(f"cp {pathlib.Path(__file__).parent.resolve()}/data/.p10k.zsh ~/")
    aprint("Zsh Installed and Configured!",2)

if checkinpt(inpt2, 1):
    aprint("Installig hypridle...")
    os.system("sudo pacman -S hypridle")
    aprint("Configuring hypridle...")
    os.system(f"cp {pathlib.Path(__file__).parent.resolve()}/data/hypridle.conf ~/.config/hypr/")
    aprint("Hypridle", 2)

if checkinpt(inpt3, 1):
    aprint("Installig AstroNeovim...")
    os.system("cargo install ripgrep")
    os.system("sudo pacman -S lazygit gdu bottom nodejs-lts-iron")
    os.system("git clone --depth 1 https://github.com/AstroNvim/template ~/.config/nvim")
    os.system("rm -rf ~/.config/nvim/.git")
    aprint("AstroNeovim installed!",2)

if checkinpt(inpt4, 2):
    aprint("Installig WPS Office...")
    os.system("yay -S wps-office ttf-wps-fonts")
    aprint("WPS Office installed!",2)

os.system("clear")
art.tprint("peshk0v", font="blubhead")
aprint("Installig sddm theme...")
os.system("git clone -b main --depth=1 https://github.com/uiriansan/SilentSDDM && cd SilentSDDM && ./install.sh")
os.system(f"cd {pathlib.Path(__file__).parent.resolve()}")
aprint("Sddm theme installed!",2)

aprint("Installig grub theme...")
os.system("sudo mkdir -p /boot/grub/themes")
os.system(f"sudo mv {pathlib.Path(__file__).parent.resolve()}/data/Arcade/ /boot/grub/themes/")
os.system("sudo pacman -S grub-customizer")
aprint("Grub theme installed!",2)

os.system("clear")
art.tprint("Finish!", font="blubhead")
aprint("Rebooting system...",2)
os.system("reboot")
