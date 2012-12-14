# installing dependencies on Debian for MotionClouds
# --------------------------------------------------
# A script for the impatient:
# uncomment to fit your installation preference
# others should read the README.txt doc.

#
# 1) minimal install 
#
# sudo aptitude install python-numpy python-scipy 

#
# 2) minimal install with visualization and generation of documentation
#
# sudo aptitude install python-numpy python-scipy mayavi2 python-matplotlib ffmpeg
# sudo aptitude install texlive-latex-recommended  latexmk latexdiff

#
# 3) full install with python editor and libraries for various export types
#
sudo aptitude install python-numpy python-scipy mayavi2 python-matplotlib ffmpeg spyder liblzo2-2 python-tables imagemagick texlive-latex-recommended latexmk latexdiff
