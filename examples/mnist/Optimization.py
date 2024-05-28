# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:42:21 2023

@author: Tom_voitz
"""

# =============================================================================
# Imports
# =============================================================================


import subprocess as sb
import os

# =============================================================================
# Optimization n_train
# =============================================================================

#Is there a maximum value of n_train => is overtraining possible ?

print("Start Simulation n_train")

fic_name = "no_change"  #So we have sth to compare with
simulation = f"python3 salah_example.py --save {fic_name} --n_train 60000"
evaluation = f"python3 evaluate_plot.py --saved {fic_name}"

if os.path.exists(f"Results/net_{fic_name}.pt"):
    try:
        print("Base test already done")
    except sb.CalledProcessError as e:
        print(f"Command execution error: : {e}")
else:
    try:
        print("Start simulation for 60k")
        sb.run(simulation, shell=True)
    except sb.CalledProcessError as e:
        print(f"Command execution error: : {e}")

n_train_best_value = 30000  #Make the next simulation faster 

# I want to understand the impact of each param => i'm trying to make the simulation faster

print("End Simulation n_train")

# =============================================================================
# Optimization time
# =============================================================================

print("Start Simulation time")

for n_time_value in range(100, 400, 50): #vary from 100 to 400 or even more?
    fic_name = f"time_var_{n_time_value}"
    simulation = f"python3 salah_example.py --n_train {n_train_best_value} --time {n_time_value} --save {fic_name}"
    evaluation = f"python3 evaluate_plot.py --n_train {n_train_best_value} --time {n_time_value} --saved {fic_name}"
    if os.path.exists(f"Results/net_{fic_name}.pt"): 
        try:
            print(f"Simulation n_time_value = {n_time_value} already done")
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Start simulation for {n_time_value}")
            #sb.run(simulation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {n_time_value}")

    
time_best_value = 200 #makes the next simulation faster

#Should we take more to be sure ? => 250 or 300 ?

print("End Simulation n_train")


# =============================================================================
# Optimization exc
# =============================================================================

# 22.5 de base
for exc_value in range(15,30,5): #faire varier de 15 à 30
    fic_name = f"exc_value_{exc_value}"
    simulation = f"python3 salah_example.py --n_train {n_train_best_value} --time {time_best_value} --exc {exc_value}  --save {fic_name}"
    evaluation = f"python3 evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"Results/net_{fic_name}.pt"): 
        try:
            print(f"Simulation exc_value = {exc_value} already done")
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation exc_value = {exc_value}")
            #sb.run(simulation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {exc_value}")

exc_best_value = 22.5 #Not that much variation


# =============================================================================
# Optimization theta_plus
# =============================================================================

#0.05 de base
for theta_plus in (0.3,0.25):
    print(f"Start simulation {theta_plus}")
    fic_name = f"theta_plus_value_{theta_plus}"
    simulation = f"python3 salah_example.py --n_train {n_train_best_value} --time {time_best_value} --theta_plus {theta_plus}  --save {fic_name}"
    evaluation = f"python3 evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"Results/net_{fic_name}.pt"): 
        try:
            print(f"Simulation theta_plus = {theta_plus} already done")
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation theta_plus = {theta_plus}")
            #sb.run(simulation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {theta_plus}")

# =============================================================================
# Optimization inh
# =============================================================================

#120 de base
for inh_value in range(100,140,10): #faire varier de 15 à 30
    print(f"Start simulation {inh_value}")
    fic_name = f"inh_value_{inh_value}"
    simulation = f"python3 salah_example.py --n_train {n_train_best_value} --time {time_best_value} --inh {inh_value}  --save {fic_name}"
    evaluation = f"python3 evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"Results/net_{fic_name}.pt"): 
        try:
            print(f"Simulation inh_value = {inh_value} already done")
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation inh_value = {inh_value}")
            #sb.run(simulation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {inh_value}")


# =============================================================================
# Optimization intensity
# =============================================================================

#0.05 de base
for intensity in range(60,90,5):
    print(f"Start simulation {intensity}")
    fic_name = f"intensity_value_{intensity}"
    simulation = f"python3 salah_example.py --n_train {n_train_best_value} --time {time_best_value} --intensity {intensity}  --save {fic_name}"
    evaluation = f"python3 evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"Results/net_{fic_name}.pt"): 
        try:
            print(f"Simulation intensity = {intensity} already done")
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation intensity = {intensity}")
            #sb.run(simulation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {intensity}")

# =============================================================================
# Optimization thresh_exc
# =============================================================================

#0.05 de base
for thresh_exc in range(-60,-20,5):
    print(f"Start simulation {thresh_exc}")
    fic_name = f"thresh_exc_{thresh_exc}"
    simulation = f"python3 salah_example.py --n_train {n_train_best_value} --time {time_best_value} --thresh_exc {thresh_exc}  --save {fic_name}"
    evaluation = f"python3 evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"Results/net_{fic_name}.pt"): 
        try:
            print(f"Simulation thresh_exc = {thresh_exc} already done")
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation thresh_exc = {thresh_exc}")
            sb.run(simulation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {thresh_exc}")

    # =============================================================================
# Optimization thresh_inh
# =============================================================================

#0.05 de base
for thresh_inh in range(-60,-20,10):
    print(f"Start simulation {thresh_inh}")
    fic_name = f"thresh_inh_{thresh_inh}"
    simulation = f"python3 salah_example.py --n_train {n_train_best_value} --time {time_best_value} --thresh_inh {thresh_inh}  --save {fic_name}"
    evaluation = f"python3 evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"Results/net_{fic_name}.pt"): 
        try:
            print(f"Simulation thresh_inh = {thresh_inh} already done")
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation thresh_inh = {thresh_inh}")
            sb.run(simulation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {thresh_inh}")
