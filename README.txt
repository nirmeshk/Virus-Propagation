Dependencies needed to be installed:

networkx==1.9.1
matplotlib==1.3.1
numpy version compatible with python3
scipy version compatible with python3

Installation steps:
1) install networkx using python 3: 
$sudo pip3 install networkx

2) install matplotlib
$sudo pip3 install matplotlib 

3)install scipy in ubuntu
$sudo apt-get install python3-scipy

4)install numpy in ubuntu
$sudo apt-get install python3-numpy 
for installation in other platforms, refer http://www.scipy.org/install.html

-------------------------------------------------------------------------
Structure of project code:
==========================
there are 5 python files located inside option-1 folder. Since calculating the eigen values was slow in scipy package of python, I have divided the projects into different modules so that we can run each question separately.

SIS.py : this is main module that contains classes and function that are used by all simulations and other tasks.

part_1.py and part_2.py are solution of question 1 and 2 respectively.

part_3_a.py and part_3_b.py are files of question 3.


-------------------------------------------------------------------------
Data set used to test the program: data/static.network


-------------------------------------------------------------------------
Steps to run program
====================

Each file can be run as independent python file as far as relative structure of folder is maintained i.e data/static.network is accessible. Out put will be printed on terminal. 

$ python3 part_1.py
$ python3 part_2.py
$ python3 part_3_a.py
$ python3 part_3_b.py

---------------------------------------------------------------------------

Reference Citations:

* I have used networkx library in python in order to calculate the store the graoh and performing its common operations.
* Scipy package is used for eigen value and eigen vector calculations.
* Matplotlib library in Python for ploting.
* For testing, I have used the datasets provided by course website only.





