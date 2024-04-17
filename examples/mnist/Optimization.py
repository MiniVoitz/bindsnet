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

#Do we need to train with 60k pics ?

print("Start Simulation n_train")

fic_name = "no_change"  #So we have sth to compare with
simulation = f"python salah_example.py --save {fic_name} --n_train 60000"
evaluation = f"python evaluate_plot.py --saved {fic_name}"

if os.path.exists(f"C:\\Users\\Tomvo\\Labwork\\my_branch\\bindsnet\\examples\\mnist\\Results\\net_{fic_name}.pt"):
    try:
        print("Evaluation for 60k")
        #sb.run(evaluation, shell=True)
    except sb.CalledProcessError as e:
        print(f"Command execution error: : {e}")
else:
    print("Evaluation not ok")
    try:
        print("Simulation for 60k")
        sb.run(simulation, shell=True)
        print("Evaluation for 60k")
        sb.run(evaluation, shell=True)
    except sb.CalledProcessError as e:
        print(f"Command execution error: : {e}")

n_train_best_value = 30000  #Make the next simulation faster 

print("End Simulation n_train")

# =============================================================================
# Optimization time
# =============================================================================

print("Start Simulation time")

for n_time_value in range(100, 400, 50): #vary from 100 to 400 or even more?
    fic_name = f"time_var_{n_time_value}"
    simulation = f"python salah_example.py --n_train {n_train_best_value} --time {n_time_value} --save {fic_name}"
    evaluation = f"python evaluate_plot.py --n_train {n_train_best_value} --time {n_time_value} --saved {fic_name}"
    if os.path.exists(f"C:\\Users\\Tomvo\\Labwork\\my_branch\\bindsnet\\examples\\mnist\\Results\\net_{fic_name}.pt"): 
        try:
            print(f"Start evaluation for {n_time_value}")
            #sb.run(evaluation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Start simulation for {n_time_value}")
            #sb.run(simulation, shell=True)
            print(f"Start evaluation for {n_time_value}")
            #sb.run(evaluation, shell=True)
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
    simulation = f"python salah_example.py --n_train {n_train_best_value} --time {time_best_value} --exc {exc_value}  --save {fic_name}"
    evaluation = f"python evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"C:\\Users\\Tomvo\\Labwork\\my_branch\\bindsnet\\examples\\mnist\\Results\\net_{fic_name}.pt"): 
        try:
            print(f"Evaluation exc_value = {exc_value}")
            #sb.run(evaluation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation exc_value = {exc_value}")
            #sb.run(simulation, shell=True)
            print(f"Evaluation exc_value = {exc_value}")
            #sb.run(evaluation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {exc_value}")

exc_best_value = 22.5 #Not that much variation

# =============================================================================
# Optimization inh
# =============================================================================

#120 de base
for inh_value in range(100,140,10): #faire varier de 15 à 30
    print(f"Start simulation {inh_value}")
    fic_name = f"inh_value_{inh_value}"
    simulation = f"python salah_example.py --n_train {n_train_best_value} --time {time_best_value} --inh {inh_value}  --save {fic_name}"
    evaluation = f"python evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"C:\\Users\\Tomvo\\Labwork\\my_branch\\bindsnet\\examples\\mnist\\Results\\net_{fic_name}.pt"): 
        try:
            print(f"Evaluation inh_value = {inh_value}")
            #sb.run(evaluation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation inh_value = {inh_value}")
            sb.run(simulation, shell=True)
            print(f"Evaluation inh_value = {inh_value}")
            sb.run(evaluation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {inh_value}")


# =============================================================================
# Optimization theta_plus
# =============================================================================

#0.05 de base
for theta_plus in (0.3,0.25):
    print(f"Start simulation {theta_plus}")
    fic_name = f"theta_plus_value_{theta_plus}"
    simulation = f"python salah_example.py --n_train {n_train_best_value} --time {time_best_value} --theta_plus {theta_plus}  --save {fic_name}"
    evaluation = f"python evaluate_plot.py --n_train {n_train_best_value} --time {time_best_value} --saved {fic_name}"
    if os.path.exists(f"C:\\Users\\Tomvo\\Labwork\\my_branch\\bindsnet\\examples\\mnist\\Results\\net_{fic_name}.pt"): 
        try:
            print(f"Evaluation theta_plus = {theta_plus}")
            #sb.run(evaluation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")
    else:
        try:
            print(f"Simulation theta_plus = {theta_plus}")
            sb.run(simulation, shell=True)
            #print(f"Evaluation theta_plus = {theta_plus}")
            #sb.run(evaluation, shell=True)
        except sb.CalledProcessError as e:
            print(f"Command execution error: : {e}")  
    print(f"Fin simulation {theta_plus}")


