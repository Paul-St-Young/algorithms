import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import plot_tools as pt
import sys
import seaborn as sns
from copy import deepcopy as copy
pt.matplotlib_header()

##################################
# Standard defintions of functions.
def wavy_energy(loc):
  return 0.5*np.sin(10*np.pi*loc)**2 + abs(loc-0.5)**1.7

def noisy_wave(loc,sig=0.1):
  return (
      0.05*np.sin(10*np.pi*loc)**2 +\
      0.05*np.sin(50*np.pi*loc)**2 +\
      abs(2*(loc-0.5))**4 +\
      -0.8*abs(2*(loc-0.5))**2 +\
      0.1*2*(loc-0.5) +\
      0.4*gaussian(loc,0.5,0.01)
    )*3

def gaussian(loc,mu=0.0,sig=1.0):
  return np.exp(-(loc-mu)**2/(2*sig**2))

def linear_cool(temp,nstep=100):
  newtemp=temp-1./nstep
  return newtemp,newtemp>1/nstep

#################################
# Class definitions. 
class AnnealingSimulation:
  """ Most basic version of a simulated annealing algorithm. """
  def __init__(self,init_state,transition_function,cooling_function,
      max_iterations=int(1e6)):
    """ 
    Input defintions:
    init_state          : first state the system is in.
    energy_function     : Measure of merit of a solution.
    transition_function : newstate=transition_function(oldstate,temperature)
    cooling_function    : newtemperature,continue = cooling_function(current_temperature)
    max_iterations      : system should be cooled by here.

    Temperature is assumed to start at 1.

    See child classes for examples.
    """

    self.init_state=init_state
    self.state=init_state
    self.energy=energy_function
    self.trans=transition_function
    self.cool=cooling_function
    self.maxit=max_iterations
    self.history=[copy(init_state)]

    self.mean=0.0
    self.std=0.0
    self.best_state=self.init_state
    self.best_energy=self.energy(self.init_state)

  def simulate(self,save_states=False,restart=False):
    temp=1.0
    iswarm=True
    iterations=0

    if restart:
      self.best_state=self.init_state
      self.best_energy=self.energy(self.init_state)
      self.state=self.init_state

    while iswarm and iterations < self.maxit:
      iterations+=1
      self.state=self.trans(self.state,temp)
      if save_states:
        self.history.append(copy(self.state))
      new_energy=self.energy(self.state)
      if new_energy<self.best_energy:
        self.best_energy=new_energy
        self.best_state=copy(self.state)

      temp,iswarm=self.cool(temp)

class OneDExample(AnnealingSimulation):
  ''' Example of simulated annhealing in 1-d. Since it's 1-d additional plotting
  functionality is available.'''
  def __init__(self,energy=wavy_energy,cool=linear_cool,step_std=1.0,max_iterations=int(1e6),init=None):
    if init is None: 
      self.init_state=np.random.random()
    else:
      self.init_state=init
    self.state=copy(self.init_state)
    self.trans=self.random_step
    self.energy=energy
    self.cool=cool
    self.maxit=max_iterations
    self.sigma=step_std

    self.history=[copy(self.init_state)]
    self.best_state=self.init_state
    self.best_energy=self.energy(self.init_state)

  def energy(self,loc):
    return 0.5*np.sin(10*np.pi*loc)**2 + abs(loc-0.5)**1.7

  def random_step(self,loc,temp):
    new=loc+np.random.normal(0,self.sigma)
    de=self.energy(new)-self.energy(loc)
    if np.random.rand() < min(1,np.exp(-de/temp)):
      return new
    else:
      return loc

  # This is not really useful, since it's bounded by 0 below.
  def stats(self,nstats=100):
    m1,m1s,m2,m2s=np.zeros(4)
    for sim in range(nstats):
      self.simulate(save_states=False,restart=True)
      en=self.energy(self.state)
      m1+=en
      m2+=en**2
      m1s+=self.state
      m2s+=self.state**2
    m1/=nstats
    m2/=nstats
    m1s/=nstats
    m2s/=nstats
    self.mean=m1
    self.std=(m2-m1**2)**0.5
    self.smean=m1s
    self.sstd=(m2s-m1s**2)**0.5

  def hist(self,nstats=500):
    self.ens=np.zeros(nstats)
    self.states=np.zeros(nstats)
    for sidx in range(nstats):
      self.simulate(save_states=False,restart=True)
      self.states[sidx]=self.best_state
      self.ens[sidx]=self.best_energy

  def animate(self,mp4out='movie.mp4',fps=10,div=1):
    self.simulate(save_states=True)
    history=[h for hi,h in enumerate(self.history) if hi%div==0]
    fig,axes=plt.subplots(1,1)

    dom=np.linspace(0,1,1000)
    lines=[]
    lines+=axes.plot(dom,self.energy(dom),pt.pc['db'],lw=2)
    lines+=axes.plot(history[0],self.energy(history[0]),'o',color=pt.pc['dr'],animated=True)
    axes.set_xlabel('Domain',size='large')
    axes.set_ylabel('Energy',size='large')
    fig.set_size_inches(5,3)
    fig.tight_layout()


    def updater(fidx,lines):
      sys.stdout.write('\rProgress: %.2f'%(fidx/len(history)))
      sys.stdout.flush()
      lines[1].set_xdata(history[fidx])
      lines[1].set_ydata(self.energy(history[fidx]))
      return lines

    animator = anim.FuncAnimation(
        fig, updater, fargs=(lines,),
        frames=len(history), blit=True,repeat=False)
   
    animator.save(mp4out,fps=fps,dpi=200)

  def show(self,outfn='1dexample'):
    # Compute stats about the solution.
    self.hist()

    fig,axes=plt.subplots(2,2,
        gridspec_kw={'width_ratios':[1,3],
                     'height_ratios':[1,3]})
    plt.delaxes(axes[0,0])

    # Objective function.
    dom=np.linspace(0,1,1000)
    axes[1,1].plot(dom,self.energy(dom),pt.pc['db'],lw=0.5)

    # Statistics of solution.
    axes[0,1].hist(self.states,bins=np.linspace(0,1,30))
    axes[0,1].set_xlim(axes[1,1].get_xlim())
    axes[0,1].set_yticks(pt.thin_ticks(axes[0,1].get_yticks()))

    axes[1,0].hist(self.ens,orientation='horizontal')
    print(axes[1,0].get_xlim(),axes[1,0].get_ylim())
    #axes[1,0].set_yticks(np.linspace(0,1,5))
    #axes[1,1].set_yticks(np.linspace(0,1,5))
    #axes[1,0].set_xticks(np.linspace(0,100,3,dtype=int))
    axes[1,0].set_xticks(pt.thin_ticks(axes[1,0].get_xticks()))

    pt.fix_lims(axes[1,1])
    axes[0,1].set_xlim(axes[1,1].get_xlim())
    axes[1,0].set_ylim(axes[1,1].get_ylim())
    fig.set_size_inches(4,3)

    # Labeling.
    axes[1,1].set_xlabel('Domain')
    axes[0,1].set_ylabel('Histogram')
    axes[1,0].set_xlabel('Histogram')
    axes[1,0].set_ylabel('Objective')
  
    fig.tight_layout()
    sns.despine()
    fig.savefig(outfn+'.pdf')
    fig.savefig(outfn+'.eps')

class NDExample(AnnealingSimulation):
  ''' Example of an optimization in N dimensions using simulated annhealing.'''
  def __init__(self,dimensions=2,step_std=1.0,max_iterations=int(1e6)):
    self.dim=dimensions
    self.init_state=np.random.random(size=self.dim)
    self.trans=self.random_step
    self.cool=self.linear_cool
    self.maxit=max_iterations
    self.sigma=step_std

    self.best_state=self.init_state
    self.best_energy=self.energy(self.init_state)

  def energy(self,coords):
    return sum(0.5*np.sin(10*np.pi*coords)**2) + np.prod(abs(coords-0.5)**1.7)

  def random_step(self,loc,temp):
    new=loc+np.random.normal(0,self.sigma,size=self.dim)
    de=self.energy(new)-self.energy(loc)
    if np.random.rand() < min(1,np.exp(-de/temp)):
      return new
    else:
      return loc

  def linear_cool(self,temp,nstep=20):
    newtemp=temp-1./nstep
    return newtemp,newtemp>1/nstep

  def hist(self,nstats=100):
    self.ens=np.zeros(nstats)
    for sidx in range(nstats):
      self.simulate(save_states=False,restart=True)
      self.ens[sidx]=self.best_energy

  def show(self):
    fig,axes=plt.subplots(1,1)
    axes.hist(self.ens)
    #pt.fix_lims(axes)
    fig.set_size_inches(3,3)
    fig.tight_layout()
    sns.despine()
    fig.savefig('ndexample.pdf')

#################################
# Exploring how this works.
def display_wavy(outfn='wavy_example'):
  ex=OneDExample(
      energy=lambda x:noisy_wave(x),
      cool=lambda x:linear_cool(x,nstep=1000),step_std=0.05,
      init=0.8
    )
  ex.show(outfn)

def make_movie(outfn='movie.mp4'):
  nstep=10000
  nframes=400
  div=nstep//nframes
  ex=OneDExample(
      energy=lambda x:noisy_wave(x),
      cool=lambda x:linear_cool(x,nstep=nstep),step_std=0.05
    )
  ex.animate(outfn,fps=4,div=div)

def plot_steps():
  ''' Trying different dimensions with different step sizes to see the effect.'''
  steps=np.linspace(0.1,1.0,5)
  dims=np.linspace(1,10,5,dtype=int)
  fig,axes=plt.subplots(steps.shape[0],dims.shape[0],sharex=True,sharey=True)
  for didx,dim in enumerate(dims):
    for sidx,step in enumerate(steps):
      sim=NDExample(dimensions=dim,step_std=step)
      sim.hist(nstats=1000)
      axes[sidx,didx].hist(sim.ens,bins=np.linspace(0.0,0.2,6),align='mid')
      axes[sidx,didx].annotate("d=%d,step=%.1f"%(dim,step),(0.7,0.9),xycoords='axes fraction')
  axes[0,0].set_xticks(pt.thin_ticks(axes[0,0].get_xticks()))
  fig.set_size_inches(2*len(dims),2*len(steps))
  fig.tight_layout()
  sns.despine()
  fig.savefig('ndsteps.pdf')

if __name__=='__main__':

  import pickle as pkl
  import os
  #plot_steps()
  #make_movie()
  display_wavy()
