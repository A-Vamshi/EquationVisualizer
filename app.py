import os
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
genai.configure(api_key=os.getenv("API_KEY"))
def getContent(inputText, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    res = model.generate_content(prompt + inputText)
    return res.text

def parse_equation(equation_str):
    equation = sp.sympify(equation_str)
    return equation

def generate_graph_data(equation):
    x_vals = np.linspace(-100, 100, 500)
    y_vals = np.array([float(equation.subs('x', val)) for val in x_vals])
    return x_vals, y_vals

prompt = """Prompt for Generating SymPy Mathematical Expressions:

You are tasked with converting a mathematical equation involving one variable, x, into a valid SymPy mathematical expression. The output must be a SymPy-compatible Python expression that can be evaluated for any value of x using SymPy's symbolic capabilities.

Instructions:
Input Format:
The input will be a mathematical equation or expression that involves x as the only variable. The equation may include standard mathematical operations such as addition, subtraction, multiplication, division, exponentiation, and parentheses.
The input may also contain common mathematical notation errors that need to be corrected to match SymPy's syntax (e.g., ^ for exponentiation should be replaced with **, and multiplication must be explicitly shown with *).
Output Requirements:
Valid SymPy Expression: Your output must be a single-line string representing a valid SymPy expression involving only the variable x.
The expression should be syntactically correct for SymPy and usable in SymPy functions (e.g., sympy.Symbol('x')).
Correct Formatting: Ensure that:
Multiplication is explicitly shown with *. For example, use 5*x**2 instead of 5x^2.
Exponentiation is written as **. For example, use x**2 instead of x^2 or x^2 for exponentiation.
Invalid Expression: If the input cannot be converted into a valid SymPy expression with x as the only variable, return -1 and nothing else. No additional characters, explanations, or symbols should be included.
Specific Constraints:
The expression must be valid for SymPy’s symbolic evaluation. Ensure it only contains x as the variable. Any other variables or functions that are not part of SymPy’s standard library should result in -1.
The expression should strictly follow SymPy’s syntax rules, including the proper use of arithmetic operations, exponentiation, and parentheses.
The expression must be in a form compatible with SymPy’s standard library and capable of symbolic evaluation (e.g., sympy.Symbol('x')).
Edge Cases:
If the expression involves any undefined functions or variables (e.g., sin(x), cos(x), or any other functions not built-in to SymPy without explicit import), return -1.
If the input is malformed (such as incorrect parentheses or operators), return -1.
Example of Valid Input and Expected Output:
Input:
2*x + 5

Output:
2*x + 5

Input:
x^2 + 3*x + 2

Output:
x**2 + 3*x + 2

Input:
sin(x) + cos(x)

Output:
-1 (since sin and cos are not defined by default in SymPy without importing them)

Input:
x / (x + 1)

Output:
x / (x + 1)

Input:
5x^2 + 2x + 3

Output:
5*x**2 + 2*x + 3

Input:
x + y

Output:
-1 (since y is not defined, and only x should appear in the expression)

Here is the string you need to convert, if it's valid just return a single line of valid sympy expression else return -1.
You must not return any other output, also make sure you don't add any symbols either.
The input: 
"""

st.title("Equation Visualizer")
inputText = st.text_input("Enter the expression: ")
if st.button("Graph the equation"):
    input2 = getContent(inputText, prompt)
    print(input2)
    eqn = parse_equation(input2)
    x, y = generate_graph_data(eqn)
    a, b = plt.subplots()
    b.plot(x, y)
    b.grid(True)
    st.pyplot(a)

