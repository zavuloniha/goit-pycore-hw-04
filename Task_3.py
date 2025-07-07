import sys
from pathlib import Path
from colorama import Fore, Style


def list_directories(path: Path, prefix=""):
    print(f'{prefix}{Fore.BLUE}{path.name} /{Style.RESET_ALL}')
    for item in sorted(path.iterdir()):
        if item.is_file():
            print(f'{prefix}   {Fore.GREEN}{item.name}{Style.RESET_ALL}')
    for item in sorted(path.iterdir()):
        if item.is_dir():
            list_directories(item, prefix + "   ")

dir_path = Path(sys.argv[1])

if not dir_path.exists():
    print(f'{Fore.RED} Директорія не знайдена.{Style.RESET_ALL}')
else:
    list_directories(dir_path)