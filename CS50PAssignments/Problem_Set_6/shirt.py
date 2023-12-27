from posixpath import splitext
import sys
from PIL import Image
import PIL


def check_if_ext_of_inp_are_same(file1, file2):
    ext1 = splitext(file1)
    ext2 = splitext(file2)
    if ext1[1] == ext2[1]:
        return True
    else:
        return False


def check_if_ext_is_valid(file1):
    ext1 = splitext(file1)
    if ext1[1] == '.jpj' or ext1[1] == '.jpej' or ext1[1] == '.png':
        return True
    else:
        return False


def open_given_file_and_save_final_img(file1, file2, file):

    photo = Image.open(file1)
    shirt = Image.open(file)
    size = shirt.size
    photo = PIL.ImageOps.fit(
        photo, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    photo.paste(shirt, shirt)
    photo.save(file2)


def check_if_file_exists_or_not(file1):
    try:
        Image.open(file1)
    except FileNotFoundError:
        return False
    else:
        return True


def main():
    if len(sys.argv) == 3:
        if check_if_file_exists_or_not(sys.argv[1]):
            if check_if_ext_of_inp_are_same(sys.argv[1], sys.argv[2]) and check_if_ext_is_valid(sys.argv[1]):
                open_given_file_and_save_final_img(
                    sys.argv[1], sys.argv[2], 'shirt.png')
            else:
                print('Extension of given files not same or valid ')
                sys.exit()
        else:
            print('File not found')
            sys.exit()
    else:
        print('Too many or too few arguments')
        sys.exit()


main()
