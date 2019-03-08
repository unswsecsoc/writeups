#!/usr/bin/env python

import argparse
from PIL import Image

ALPHA = -1
PERIOD = 2019 - 1883
ASCII_LOWER = 32
ASCII_UPPER = 126

# Parse Args
parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Simple steganography encoder/decoder using Least \
                     Significant Digit encoding on each [RGB] byte."
        )
parser.add_argument("mode",
        help="Specify encode/decode mode.", 
        choices=['encode', 'decode'],
        type=str)
parser.add_argument("image",
        help="Image to encode/decode.", 
        type=str)
parser.add_argument("-m", "--message",
        help="Message to encode with image", 
        type=str, default="Steganography!")
parser.add_argument("-o", "--output",
        help="Output file.", 
        type=str, default="out.png")
args = parser.parse_args()

if args.mode == "decode":
    im1 = Image.open(args.image)
    pixels = im1.load()

    message = ''
    try:
        for y in range(im1.size[1]):
            for x in range(im1.size[0]):
                if (x + y*im1.size[0]) % PERIOD == 0:
                    pix = pixels[x,y]
                    #print(f'{x}, {y} : {pix}')
                    decode_int = (pix[2]%10)*100 + (pix[1]%10)*10 + pix[0]%10
                    if ASCII_LOWER <= decode_int < ASCII_UPPER:
                        char = bytearray.fromhex(f'{decode_int:02x}').decode()
                        message += char
                    if decode_int == 26:
                        raise StopIteration
    except StopIteration:
        pass
    finally:
        print(message)
        im1.close()

else:
    message_iterator = iter(args.message)

    im1 = Image.open(args.image)
    pixels_in = im1.load()

    im2 = Image.new(im1.mode, im1.size)
    pixels_out = im2.load()

    once = None
    # Image.size is a tuple of (width, height)
    for y in range(im1.size[1]):
        for x in range(im1.size[0]):
            pix = list(pixels_in[x,y])
            if (x + y*im1.size[0]) % PERIOD == 0 and pix[ALPHA] != 0:
                try:
                    # Encode 3-digit int onto the least significant digit
                    # of each pixel
                    next_hex = next(message_iterator).encode('utf-8').hex()
                    next_int = int(next_hex, base=16)
                    pix[0] = (pix[0]//10)*10 + (next_int % 10)
                    next_int //= 10
                    pix[1] = (pix[1]//10)*10 + (next_int % 10)
                    next_int //= 10
                    pix[2] = (pix[2]//10)*10 + (next_int % 10)
                    print(f'Pixel[{x}, {y}] = ' + str(pix))
                except StopIteration:
                    if once is None:
                        # Terminate with ASCII SUB 26
                        pix[0] = (pix[0]//10)*10 + 6
                        pix[1] = (pix[1]//10)*10 + 2
                        pix[2] = (pix[2]//10)*10 + 0
                        once = True

            pix = tuple(pix)
            pixels_out[x,y] = pix

    im1.close()
    im2.save(args.output)
    im2.close()
