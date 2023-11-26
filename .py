import argparse
import tkinter as tk
import pyqrcode as qr

parse = argparse.ArgumentParser()
parse.add_argument("--info", type=str,
                   help="ingresa info puedes poner 'el nombre con espacios'")
parse.add_argument("--nombre", type=str,
                   help="ingresa el nombre de la imagen png sin el .png puedes poner 'info con espacios'")
args = parse.parse_args()

if args.info == None:
    print("utiliza python .py -h para mas informacion")
    exit()
elif args.nombre == None:
    print("utiliza python .py -h para mas informacion")
    exit()

img = qr.create(args.info)
img.png(f"{args.nombre}.png", scale=8, background=(
    255, 255, 255, 255), module_color=(0, 0, 0, 255))
