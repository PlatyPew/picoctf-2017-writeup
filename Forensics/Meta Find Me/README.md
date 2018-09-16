# Meta Find Me
Points: 70

## Category
Forensics

## Question
>Find the location of the flag in the image: [image.jpg](files/image.jpg). Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

### Hint
>How can images store location data? Perhaps search for GPS info on photos.

## Solution
From the name of the challenge, we can safely assume that the flag is hidden somewhere in the metadata of the image.

Using a program _exiftool_, we can view all metadata in an image.

Using the command `exiftool image.jpg`, we get this.

```
$ exiftool image.jpg

...

Comment                         : "Your flag is flag_2_meta_4_me_<lat>_<lon>_1c84. Now find the GPS coordinates of this image! (Degrees only please)"
Image Width                     : 500
Image Height                    : 500
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 500x500
Megapixels                      : 0.250
Thumbnail Image                 : (Binary data 6989 bytes, use -b option to extract)
GPS Position                    : 7 deg 0' 0.00", 100 deg 0' 0.00"
```

We can see that there is a comment, which gives us an incomplete flag. We fill in the respective latitude and longtitude data values into its respective places, and we get the flag!

### Flag
`flag_2_meta_4_me_7_100_1c84`
