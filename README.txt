#acl All:read


= MotionClouds: installing and running the python scripts =
[[TagMotionClouds|MotionClouds]] are parameterized stimuli with controlled motion content and no spatial coherence.  They are precisely tuned in the frequency space.

 * A full description can be found in Paula S. Leon, Ivo Vanzetta, Guillaume S. Masson, Laurent U. Perrinet. Motion Clouds: Model-based stimulus synthesis of natural-like random textures for the study of motion perception, URL . Journal of Neurophysiology, 107(11):3217--3226, 2012, see  http://www.ncbi.nlm.nih.gov/pubmed/22423003 or http://jn.physiology.org/content/107/11/3217 .

== installing and running the python scripts ==
This package consists of:
 * {{{MotionClouds.py}}} : the API with all the math and display routines,
 * {{{test_*.py}}} : different types of stimuli are tested,
 * {{{experiment_*py}}} : different experiments.
 * {{{fig_*py}}} : different scripts used to generate wiki pages.
 * {{{figures}}} : resulting figures of tests and experiments (as set in the variable {{{MotionClouds.figpath}}}.
 * {{{Makefile}}} : a GNUmake file to edit files {{{make edit}}}, generate figures {{{make figures}}} or compile the documentation {{{make doc}}}.

== Installation ==

 * Installation of MotionClouds consists simply in downloading the {{{MotionClouds.py}}} file which contains all routines to compute and use the MotionClouds textures. This script uses [[http://python.org|python]]] which comes (pre-installed /  easy to download and install) on many operating systems.

 * Installation has some dependencies: 
  1. mandatory: {{{numpy}}} is the core library used to compute textures,
  1. optional: {{{mayavi}}} is used to visualize envelopes,
  1. optional: {{{ffmpeg}}} is used to generate movies.
  1. optional: {{{matplotlib}}}, {{{scipy}}} (with PIL support) and {{{imagemagick}}} are used to generate figures in the documentation.
  1. optional: {{{progressbar}}} for displaying progress of encoding.
  1. optional: {{{texlive-latex-recommended  latexmk latexdiff}}} to compile the documentation 

== download ===

 * to get the latest version, download the current state from the repository:
{{{
git clone https://github.com/meduz/MotionClouds.git 
}}}

 * other sources exist to get a stable release, such as [[http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146953|ModelDb]].

=== installation using custom scripts ===

 * depending on your system you should use in a terminal window {{{
sh install_dependencies_debian.sh
}}} or {{{
sh install_dependencies_macosx.sh
}}}
 * an alternative is to use a virtual machine such as for instance the one provided by the [[http://neuro.debian.net/vm.html|NeuroDebian team]].

=== Installation in Debian-based distributions (such as Ubuntu) ===

 * Use the {{{aptitude}}} front end to install packages: (or alternatively {{{apt -get}}} if you feel confident with that tool instead)

 * {{{python}}} is supported by most distribution and should already be installed. You can check which version is installed : {{{
python -V
}}}

 * The same libraries as for MacOsX need to be installed : {{{
sudo aptitude install python-scipy python-numpy python-matplotlib
}}}

 * Idem for the progress bar module {{{
sudo easy_install progressbar 
}}}

 * Install the {{{ffmpeg}}} encoder to work with mpeg, avi, etc, videos: {{{
sudo aptitude install ffmpeg
}}}

 * Install !LaTeX to compile the documentation: {{{
sudo aptitude install texlive-latex-recommended latexmk latexdiff
}}}

 * when creating MoiMoin pages, it is useful to package images in a zip file: {{{
aptitude install zip
}}}

=== Installation on MacOsX: EPD ===

 * Enthought distributes a battery-included installation of python. It is recommended to use the i386 version as the 64-bits version lacks a proper compilation of MayaVi. You will still need {{{ffmpeg}}} to make movies (see HomeBrew or MacPorts section below).

 * Similarly, to compile the documentation, I recommend to install !TexLive from the !MacTex distribution available @ https://www.tug.org/mactex/

=== Installation on MacOsX: HomeBrew (for more experienced users) ===

 * install it following their [[https://github.com/mxcl/homebrew/wiki/Installation|instructions]] : {{{
ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"
}}}
 * then install the following packages {{{

# install python through HomeBrew as a framework
brew install python --framework

# bootstrap pip
/usr/local/share/python/easy_install pip
/usr/local/share/python/pip install --upgrade distribute

# libraries
brew install gfortran
pip install -U ipython

# useful packages
pip install -U nose
pip install -U progressbar
easy_install pyreport
easy_install -f http://dist.plone.org/thirdparty/ -U PIL==1.1.7

# numpy et al
pip install -U numpy
pip install -U scipy
pip install -U -e git+git@github.com:matplotlib/matplotlib.git#egg=matplotlib
# pip install -f http://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.0/matplotlib-1.0.0.tar.gz matplotlib

# IDE
pip install -U sphinx pyflakes rope
brew install sip
brew install pyqt
pip install -U spyder

# mayavi
brew install vtk --python
pip install -U traitsbackendqt
pip install -U configobj
pip install  -U "Mayavi[app]"
}}}
  * be sure to install ffmpeg : {{{
brew install ffmpeg
brew install zip
}}}

=== Installation on MacOsX: MacPorts (outdated documentation) ===
On MacOsX, this may be achieved using !MacPorts:
 * [[http://www.macports.org|MacPorts]] is a generic package manager, somewhat related to Debian's {{{apt}}} scheme. You will need the XCode package which sits in your MacOSX installation DVD or may downloaded on Apple's site or even borrowed to me.
 * Once installed, do the following on the command-line 

  * on Leopard (python 26 works fine too): {{{
sudo port install python25 python_select 
sudo python_select python25
sudo port install  py25-pil py25-numpy py25-scipy py25-ipython py25-matplotlib
+cairo+latex+tkinter
sudo port install py25-enthoughtbase py25-mayavi py25-traitsbackendqt
}}}
  * on Snow Leopard: {{{
sudo port install python26 python_select 
sudo python_select python26
sudo port install  py26-pil py26-numpy py26-scipy py26-ipython py26-matplotlib
+cairo+latex+tkinter
sudo port install py26-enthoughtbase py26-mayavi py26-traitsbackendqt
 * then optionally, {{{
sudo easy_install progressbar pygarrayimage pyglet
}}}
  * be sure to install ffmpeg : {{{
sudo port install ffmpeg
}}}

----
TagMotion TagMotionClouds
