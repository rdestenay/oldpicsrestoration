# oldpicsrestoration
This first project using the fast.ai library aim to provide a general automated tool for old images restoration.

## Inception
The project started when I saw a black and white deteriorated picture of my grandmother when she was young.
I thought I could improve the quality a lot using deep learning.
The aim is to remove all artifacts (grain, vignette, hair on the lens, blurriness, high contrasts) and colorize it. In the end, it should look like it could have been taken nowadays with a high quality camera.

Here is the picture that I want to restore :
![grandma's pic](https://github.com/rdestenay/oldpicsrestoration/blob/master/grandma.jpg)



## Method
To achieve this goal, I use inspiration from the most recent papers on the subject such as Pix2Pix, Pix2PixHD, Progressive Growing of GANs and Image Inpainting for Irregular Holes Using Partial Convolutions.
(references to come)

![Pix2Pix](https://phillipi.github.io/pix2pix/images/teaser_v3.jpg)
