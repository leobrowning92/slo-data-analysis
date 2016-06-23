import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def plotupdown(ax,xdata,ydata):
    half=int(len(xdata)/2)
    ax.plot(xdata[:half],ydata[:half],'b-.',label="start - to + sweep",linewidth=2.0)
    ax.plot(xdata[half:],ydata[half:],'b--',label="+ to - sweep",linewidth=2.0)
    ax.legend()

def log_plotupdown(ax,xdata,ydata):
    half=int(len(xdata)/2)
    ax.semilogy(xdata[:half],ydata[:half],'b-.',label="start - to + sweep",linewidth=2.0)
    ax.semilogy(xdata[half:],ydata[half:],'b--',label="+ to - sweep",linewidth=2.0)
    ax.legend()


def plotgradient(ax,xdata,ydata):
    ax2=ax.twinx()
    half=int(len(xdata)/2)
    ax.plot(xdata[:half],ydata[:half],'b-.',label="Up sweep")
    ax2.plot(xdata[:half],np.gradient(ydata[:half]),'r-',label="gradient")
    ax2.legend()

def format_axis(ax, title,xlabel,ylabel):
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    ax.set_title(title)

def make_linlog_figure(data,name):
    fig=plt.figure(figsize=(12,5))
    ax1 = plt.subplot(1,2, 1)
    ax2 = plt.subplot(1,2, 2)
    log_plotupdown(ax1,data[:,0],data[:,2])
    plotupdown(ax2,data[:,0],data[:,2])
    format_axis(ax1,name+" log","$V_{GS}$","$I_{DS}$")
    format_axis(ax2,name+ " linear","$V_{GS}$","$I_{DS}$")

def calculate_metrics(data):
    maximum=np.max(data[:,2])
    minimum=np.min(data[:,2])
    onoffratio=maximum/minimum
    return onoffratio

path1="data/COL208_device1_postdielelectric_FET_2016_05_28_1312.csv"
path2="data/COL211_device2_postdielelectric_FET_2016_05_28_1322.csv"
data1=np.loadtxt(fname=path1,skiprows=1,delimiter=',')
data2=np.loadtxt(fname=path2,skiprows=1,delimiter=',')

make_linlog_figure(data1,os.path.basename(path1)[:6])
plt.show()
