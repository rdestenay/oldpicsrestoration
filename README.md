# Old Pictures Restoration
This first project using the fast.ai library aim to provide a general automated tool for old images restoration.

## Inception
The project started when I saw a black and white deteriorated picture of my grandmother when she was young.
I thought I could improve the quality a lot using deep learning.
The aim is to remove all artifacts (grain, vignette, hair on the lens, blurriness, high contrasts) and colorize it. In the end, it should look like it could have been taken nowadays with a high quality camera.

It is important to understand that the goal is not to get the colors true to the original, but just to make it plausible that these colors were the ones that lead to this picture taken.
The tow important criteria are :
- The output image should look natural, nothing out of ordinary
- The output image once deteriorated should look like the original image
(This actually represent the two main loss we use in our algorithm)

Here is the picture that I want to restore :

<img src="https://github.com/rdestenay/oldpicsrestoration/blob/master/readmepics/grandma.jpg" alt="grandma's pic" height="500"/>



## Method
To achieve this goal, I use inspiration from the most recent papers on the subject such as Pix2Pix, Pix2PixHD, Progressive Growing of GANs and Image Inpainting for Irregular Holes Using Partial Convolutions.
(references to come)

![Pix2Pix](https://phillipi.github.io/pix2pix/images/teaser_v3.jpg)

## Image artificial deterioration
The first step of our work consists of artificially deteriorating a large dataset with as much randomness as possible by:
- making it black and white
- playing with the levels
- adding blur
- generating grain images to be added to the image
- generating masks to be added to the image (this is to simulate things that happens to old pictures, such as hair on the lens, stain, tearing, some vignette)

<img src="https://github.com/rdestenay/oldpicsrestoration/blob/master/readmepics/000003.jpg" alt="grain" height="200"/> <img src="https://github.com/rdestenay/oldpicsrestoration/blob/master/readmepics/000029.jpg" alt="mask" height="200"/>

The result is as follow:
![Example of artificial deterioration](https://github.com/rdestenay/oldpicsrestoration/blob/master/readmepics/deterioration.png)

The dataset use for our experiment is the LSUN person dataset.
