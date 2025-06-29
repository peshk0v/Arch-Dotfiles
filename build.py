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
inpt3 = input("Enable nvidia settings? [y/N] > ")
inpt4 = input("Install astraNeovim? [Y/n] > ")
inpt5 = input("Install WalMan(Wallpaper Manager)? [Y/n] > ")
inpt6 = input("Install WPS Office? [y/N] > ")

os.system("clear")
art.tprint("ArchLinux", font="blubhead")
aprint("Installig archlinux dotfiles...")
aprint("Installing yay...")
os.system("sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
aprint("Yay installed!", 2)
aprint("Move to repo folder")
os.system(f"cd {pathlib.Path(__file__).parent.resolve()}")
aprint("Installig base packages...")
os.system("sudo pacman -S hyprpaper hyprshot git curl rofi nano brightnessctl pulseaudio waybar fastfetch kitty htop xorg swww nautilus nwg-look obsidian telegram-desktop discord nerd-fonts ttf-ubuntu-font-family ttf-font-awesome --needed")
aprint("Base packages installed!", 2)
aprint("Installig AUR packages...")
os.system("yay -S ttf-meslo-nerd-font-powerlevel10k zen-browser")
aprint("Aur packages installed!", 2)
aprint("Installig user selected packages...")
if checkinpt(inpt1, 1):
    aprint("Installig oh my zsh...")
    os.system("sudo pacman -S zsh --needed")
    os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
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
    aprint("Hypridle installed!\nThe hypridle configuration will be applied after the main config loaded")
