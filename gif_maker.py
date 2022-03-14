import imageio
import glob
import os

images = []
for filename in glob.glob(os.path.join(r"C:\Users\emrea\Desktop\'22 Courses\Num-Methods\secant_gif",'*.png')):
    images.append(imageio.imread(filename))
imageio.mimsave('secant.gif', images, duration=0.5)


