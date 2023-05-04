#!/usr/bin/python3
# coding: utf-8
from PIL import Image
from time import sleep
import signal, sys, os, argparse

### By: Argon3x
### Supported: Debian Based Systems
### Version: 1.0

# Colors
green = "\033[01;32m"; blue = "\033[01;34m"; red = "\033[01;31m"
purple = "\033[01;35m"; yellow = "\033[01;33m"; end = "\033[00m"

# Context Box
box = f"{blue}[{green}+{blue}]{end}"
ast = f"{blue}[{purple}*{blue}]{end}"

# Function error and interrupt
def interrupt_handler():
    sys.stdout.write(f"\n{blue}>>> {red}Process Canceled {blue}<<<{end}\n\n")
    sys.exit(1)

def error_handler(type_error):
    sys.stdout.write(f"\n{blue}script error: {red}{type_error}{end}\n\n")
    sys.exit(1)

# Call the signals
signal.signal(signal.SIGINT, interrupt_handler)
signal.signal(signal.SIGTERM, error_handler)


# Compress image size
def compress_images(directory, images, new_directory):
    print(f"{ast} {yellow}Compressing images{end}...........")

    for list_images in images:
        path_image_old = directory + '/' + list_images
        path_image_new = new_directory + '/' + list_images

        print(f"{ast} {yellow}Compressing {green}{list_images}{end}...........", end='')
        try:
            with Image.open(path_image_old) as picture:
                picture.save(path_image_new, optimize=True, quality=70)
        except IOError:
            print(f"{box} {red}failed{end}")
            error_handler(type_error="[!] An Error Ocurred While Comprissing The Image [!]")
        else:
            print(f"{green}   done{end}")


# main function
def main(directory, new_directory):
    os.system('clear')
    print(f"{box} {yellow}Starting{end}...........")
    sleep(1)
    
    # Checking if the directory exist
    print(f"{ast} {yellow}Checking the {blue}{directory} {yellow}directory{end}...........", end='')
    sleep(1)

    if os.path.exists(directory):
        print(f"\t{blue}[{green}ok{blue}]{end}")
    else:
        error_handler(type_error="[!] {blue}{directory} {red}Directory Does Not Exist [!]")

    print(f"{ast} {yellow}Checking if {green}JPG/JPEG/PNG {yellow}files exist in directory{end}.......", end='')
    sleep(1)
    
    extensions = ('jpeg', 'jpg', 'png')
    files = os.listdir(directory)
    images = [file for file in files if file.endswith(extensions)]

    if len(images) != 0:
        print(f"\t{blue}[{green}ok{blue}]{end}")
    else:
        print(f"\t{blue}[{red}failed{blue}]{end}")
        error_handler(type_error="There is no Image in the Directory [!]")

    sleep(1)

    # Call Function
    compress_images(directory, images, new_directory)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compress images that are in a specific directory')
    parser.add_argument('--directory', '-d', required=True, type=str, metavar='', help='Select a specific directory.')
    parser.add_argument('--new_directory', '-n', required=True, type=str, metavar='', help='Select a different directory to save the news images.')
    args = parser.parse_args()
    new_directory = args.new_directory
     
    if new_directory is None:
        new_directory = new_directory if new_directory is not None else args.directory
    else:
        print(f"{ast} {yellow}Checking if the {green}{new_directory} directory exists{end}.......", end='')
        sleep(1)

        if os.path.isdir(new_directory):
            print(f"\t{blue}[{green}ok{blue}]{end}")
        else:
            print(f"\t{blue}[{red}failed{blue}]{end}")
            error_handler(type_error=f"{blue}{new_directory} {red}Directory Does No Exists [!]{end}")

    # call function compress images
    main(args.directory, new_directory)
