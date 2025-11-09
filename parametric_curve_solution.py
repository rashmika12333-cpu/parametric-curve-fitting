"""
Parametric Curve Fitting Solution
Student: [Your Name]
Student ID: [Your ID]
Date: [Current Date]

Academic Integrity Declaration:
This work represents my own independent effort. I have not received
unauthorized assistance and all code was developed by me independently.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

# Load data
def load_data():
    data = pd.read_csv('xy_data.csv')
    return data['x'].values, data['y'].values

# Parametric curve equations
def parametric_curve(t, theta_deg, M, X):
    theta_rad = np.radians(theta_deg)
    x = t * np.cos(theta_rad) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta_rad) + X
    y = 42 + t * np.sin(theta_rad) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta_rad)
    return x, y

# L1 distance objective function
def objective_function(params, t_values, x_data, y_data):
    theta, M, X = params
    x_pred, y_pred = parametric_curve(t_values, theta, M, X)
    l1_distance = np.sum(np.abs(x_pred - x_data) + np.abs(y_pred - y_data))
    return l1_distance

def main():
    print("PARAMETRIC CURVE FITTING SOLUTION")
    
    # Load data
    x_data, y_data = load_data()
    t_values = np.linspace(6, 60, len(x_data))
    
    # Parameter bounds
    bounds = [(0, 50), (-0.05, 0.05), (0, 100)]
    
    # Global optimization
    result = differential_evolution(
        objective_function, bounds,
        args=(t_values, x_data, y_data),
        strategy='best1bin',
        maxiter=100,
        popsize=15,
        seed=42
    )
    
    # Extract results
    theta_opt, M_opt, X_opt = result.x
    l1_distance = result.fun
    
    print(f"\nOPTIMIZED PARAMETERS:")
    print(f"θ = {theta_opt:.8f}°")
    print(f"M = {M_opt:.10f}")
    print(f"X = {X_opt:.8f}")
    print(f"L1 Distance = {l1_distance:.6f}")
    
    # Generate visualization
    t_fine = np.linspace(6, 60, 1000)
    x_fit, y_fit = parametric_curve(t_fine, theta_opt, M_opt, X_opt)
    
    plt.figure(figsize=(12, 8))
    plt.scatter(x_data, y_data, alpha=0.6, s=10, label='Original Data (500 points)')
    plt.plot(x_fit, y_fit, 'r-', linewidth=2, label='Fitted Curve')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Parametric Curve Fitting\nθ={theta_opt:.4f}°, M={M_opt:.6f}, X={X_opt:.4f}, L1={l1_distance:.2f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.savefig('results.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return theta_opt, M_opt, X_opt, l1_distance

if __name__ == "__main__":
    theta, M, X, l1 = main()
    
    # Generate submission formats
    print("\nSUBMISSION FORMATS:")
    print("=" * 50)
    
    # LaTeX format
    latex = f"\\left(t\\cdot\\cos({theta:.8f})-e^{{{M:.10f}\\left|t\\right|}}\\cdot\\sin(0.3t)\\sin({theta:.8f})\\ +{X:.8f},42+\\ t\\cdot\\sin({theta:.8f})+e^{{{M:.10f}\\left|t\\right|}}\\cdot\\sin(0.3t)\\cos({theta:.8f})\\right)"
    print("LaTeX:\n" + latex)
    
    print("\n" + "-" * 40)
    
    # Desmos format  
    desmos = f"(t*cos({theta:.8f})-e^({M:.10f}|t|)*sin(0.3t)sin({theta:.8f})+{X:.8f},42+t*sin({theta:.8f})+e^({M:.10f}|t|)*sin(0.3t)cos({theta:.8f}))"
    print("Desmos:\n" + desmos)