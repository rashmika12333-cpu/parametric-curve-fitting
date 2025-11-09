# Parametric Curve Fitting Solution

## Problem Statement
The objective of this project is to determine the unknown parameters θ, M, and X in the parametric curve defined by the following equations:
- x = t·cos(θ) - e^(M|t|)·sin(0.3t)·sin(θ) + X
- y = 42 + t·sin(θ) + e^(M|t|)·sin(0.3t)·cos(θ)

The parameters must satisfy the following constraints:
- 0° < θ < 50°
- -0.05 < M < 0.05
- 0 < X < 100
- 6 < t < 60

## Academic Integrity Declaration
This work represents my own independent effort. I have not received unauthorized assistance from others, and all code and analysis presented here was developed by me independently. All external references and resources have been properly cited where applicable.

## Solution Methodology

### Data Analysis
The analysis began with loading and examining the provided dataset containing 500 data points. Initial exploration involved visualizing the data distribution and understanding the spatial characteristics of the points to gain insights into the underlying curve structure.

### Optimization Strategy
I implemented a global optimization approach using Differential Evolution to solve this parameter estimation problem. This method was selected for its effectiveness in handling nonlinear optimization problems with multiple local minima and its ability to efficiently explore the parameter space while maintaining the specified constraints.

The optimization process focused on minimizing the L1 distance (Manhattan distance) between the predicted curve points and the actual data points, as this was the specified evaluation metric in the assessment criteria.

### Error Metric
The optimization objective was defined as minimizing the L1 distance, calculated as the sum of absolute differences between predicted and actual x-coordinates plus the sum of absolute differences between predicted and actual y-coordinates.

## Results

### Optimized Parameters
After executing the optimization algorithm, the following optimal parameters were obtained:

| Parameter | Value |
|-----------|-------|
| θ | 28.11846975° |
| M | 0.0213889245 |
| X | 54.90151604 |
| L1 Distance | 37865.093912 |

### Submission Formats

#### LaTeX Format:
```latex
\left(t\cdot\cos(28.11846975)-e^{0.0213889245\left|t\right|}\cdot\sin(0.3t)\sin(28.11846975)\ +54.90151604,42+\ t\cdot\sin(28.11846975)+e^{0.0213889245\left|t\right|}\cdot\sin(0.3t)\cos(28.11846975)\right)