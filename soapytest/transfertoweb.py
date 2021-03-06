#! /usr/bin/env python

import os

SOAPYTEST_DIR = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "../")

PLOTS_DIR = os.path.join(SOAPYTEST_DIR, "plots/")

def transfer(plotsdir=None):
    if plotsdir==None:
        plotsdir = PLOTS_DIR

    plotfiles = os.listdir(plotsdir)


    for f in plotfiles:
        os.system('scp {}/{} d70j6c@mira.dur.ac.uk:~/public_html/soapytest/'.format(plotsdir, f))

if __name__=="__main__":
    transfer()
