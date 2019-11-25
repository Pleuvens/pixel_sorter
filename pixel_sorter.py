#!/usr/bin/env python3

from PIL import Image

def getMaxInRow(r, start, h, arr):
    index = 0;
    #print(arr[0, c])
    value = arr[r, 0][0] + arr[r, 0][1] + arr[r, 0][2]
    for j in range(start, h):
        if arr[r, j][0] + arr[r, j][1] + arr[r, j][2] > value:
            index = j
            value = arr[r, j][0] + arr[r, j][1] + arr[r, j][2]
    return index

def getMaxInColumn(c, start, w, arr):
    index = 0;
    #print(arr[0, c])
    value = arr[0, c][0] + arr[0, c][1] + arr[0, c][2]
    for i in range(start, w):
        if arr[i, c][0] + arr[i, c][1] + arr[i, c][2] > value:
            index = i
            value = arr[i, c][0] + arr[i, c][1] + arr[i, c][2]
    return index

def sortRow(w, h, pixels):
    for i in range(w):
        for j in range(h):
            index = getMaxInRow(i, j, h, pixels)
            tmp = pixels[i, j]
            pixels[i, j] = pixels[i, index]
            pixels[i, index] = tmp
        print(str(int(i * 100 / w)) + '%', end='\r')
    return pixels

def sortColumn(w, h, pixels):
    for j in range(h):
        for i in range(w):
            index = getMaxInColumn(j, i, w, pixels)
            tmp = pixels[i, j]
            pixels[i, j] = pixels[index, j]
            pixels[index, j] = tmp
        print(str(int(j * 100 / h)) + '%', end='\r')
    return pixels

def main():
    img = Image.open("samples/smol2.jpg")
    pixels = img.load()
    pixels = sortRow(img.size[0], img.size[1], pixels)
    #for i in range(img.size[0]):
    #    for j in range(img.size[1]):
    #        pixels[i,j] = (i, j, 100)
    img.show()

main()
