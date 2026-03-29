								Big-M Method Solver

Project Overview

This project is an interactive Linear Programming Solver built using Python and Streamlit, implementing the Big M Method to solve optimization problems involving:

Maximization problems
Constraints with <=, >=, and =
Artificial variables handling
Step-by-step tableau visualization (like manual notebook solving)

It also includes a graphical visualization of constraints and optimal solution (for 2-variable and 3-variable problems).

Objectives

To implement the Big M Method algorithm programmatically
To replicate manual simplex table steps digitally
To provide interactive visualization for better understanding
To create a user-friendly UI for solving LPP problems with up to 3 decision variables

Features

Core Features

Supports: <=, >=, = constraints
Supports up to 3 decision variables (x1, x2, x3)
Automatic:
	Slack variable addition
	Artificial variable handling using Big M
Step-by-step:
	Iteration tables
	Pivot column & pivot row
	Ratio column

Tableau Representation

Each iteration displays:

Basis variables
Cb (cost of basic variables)
Zj row
Cj − Zj row
Ratio column

Graph Visualization

2-variable problems: Plots constraint lines and shades the feasible region, shows optimal solution point
3-variable problems: Renders a 3D plot of constraint planes using Matplotlib's 3D toolkit, highlights the optimal solution point in 3D space
Animated drawing effect for better understanding

Working of the Project

1. Input Processing
User enters:
	Objective function (e.g., 5x1 + 4x2 + 3x3)
	Constraints (line by line, supporting up to 3 variables)
Input is parsed using regular expressions

2. Conversion to Standard Form
<= → Slack variable added
>= → Surplus + Artificial variable
= → Artificial variable

3. Big M Method Logic
Artificial variables are assigned a large penalty (−M)
Objective function is modified accordingly
Initial tableau is constructed (now accommodates x1, x2, and x3 columns)

4. Iterative Optimization
Compute:
	Zj
	Cj − Zj
Select:
	Entering variable (max Cj − Zj)
	Leaving variable (minimum ratio)
Perform pivot operations
Repeat until optimal solution is reached

5. Final Output
Displays:
	Optimal values of all decision variables (x1, x2, x3)
	Maximum value of objective function
	2D graph for 2-variable problems; 3D graph for 3-variable problems

Installation Guide

Prerequisites

Make sure you have:

Python 3.8+
pip installed

Step-by-Step Setup

1. Clone Repository

git clone https://github.com/your-username/big-m-solver.git
cd big-m-solver

2. Install Dependencies

pip install streamlit numpy pandas matplotlib

3. Run the App

streamlit run app.py

4. Open in Browser

http://localhost:8501

Example Input — 2 Variables

Objective Function: 5x1 + 4x2
Constraints:
6x1 + 4x2 >= 24
x1 + 2x2 = 6
-x1 + x2 <= 1

Output
Iteration tables (step-by-step)
Optimal solution:
x1 = value
x2 = value
Z = max value
2D graph with feasible region and optimal point

Example Input — 3 Variables

Objective Function: 3x1 + 5x2 + 4x3
Constraints:
2x1 + x2 + x3 <= 14
x1 + 2x2 + x3 <= 14
x1 + x2 + 2x3 <= 14

Output
Iteration tables (step-by-step)
Optimal solution:
x1 = value
x2 = value
x3 = value
Z = max value
3D graph with constraint planes and optimal point highlighted

Research & Concepts Used

Topics Covered

Linear Programming Problems (LPP)
Simplex Method
Big M Method
Artificial Variables
Optimization Techniques
3D Visualization of Feasible Regions

Algorithm Used

Big M Method (Penalty Method)
Pivot operations (Gauss-Jordan elimination)

Resources / References

Books
Operations Research by Kanti Swarup
Introduction to Operations Research by Hillier & Lieberman

Online Resources
https://www.geeksforgeeks.org/linear-programming/
https://www.tutorialspoint.com/operation_research
https://www.youtube.com
 (for conceptual understanding)

Libraries Used
Streamlit (UI)
NumPy (matrix operations)
Pandas (table display)
Matplotlib (2D/3D graph plotting)
mpl_toolkits.mplot3d (3D visualization for 3-variable problems)
