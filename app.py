
import os
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
genai.configure(api_key=os.getenv("API_KEY"))
from sympy import sin, cos, tan, exp, log, sqrt

def getContent(inputText, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    res = model.generate_content(prompt + inputText)
    return res.text

def parse_equation(equation_str):
    try:
        equation = sp.sympify(equation_str)
        return equation
    except sp.SympifyError:
        return None

def generate_graph_data(equation, x_min, x_max, num_points=500):
    x_vals = np.linspace(x_min, x_max, num_points)
    try:
        y_vals = np.array([float(equation.subs('x', val)) for val in x_vals])
    except ZeroDivisionError:
        raise ValueError("Math error occurred while evaluating the equation.")
    return x_vals, y_vals

prompt = """Prompt for Generating SymPy Mathematical Expressions:
You are tasked with converting a mathematical equation involving one variable, x, into a valid SymPy mathematical expression. The equation can include standard mathematical functions such as sin(x), cos(x), tan(x), exp(x), log(x), sqrt(x), and other mathematical operations.
Please ensure that your output follows the SymPy syntax correctly and supports standard functions like sin, cos, exp, log, sqrt, etc. Make sure that the expression uses x as the only variable. Return the expression as a valid SymPy code, and do not include any extra text.
If the sympy syntax isn't possible just return a -1 with no extra text.
"""

st.title("Equation Visualizer")
inputText = st.text_input("Enter the expression: ")
x_min = st.number_input("Enter the minimum value for x:", -200, 0, -100)
x_max = st.number_input("Enter the maximum value for x:", 0, 200, 100)

if st.button("Graph the equation"):
    # Show loading spinner while the equation is being processed
    with st.spinner('Processing the equation...'):
        # Preprocessing: Correcting syntax issues like '^' to '**'
        inputText = inputText.replace("^", "**").replace(" ", "")
    
        input2 = getContent(inputText, prompt)
    
        if input2 == "-1":
            st.error("Invalid mathematical expression! Please check your syntax or use only supported functions.")
        else:
            eqn = parse_equation(input2)
            if eqn is None:
                st.error("There was an error processing the equation. Please ensure it is a valid mathematical expression.")
            else:
                try:
                    # Generate graph data
                    x_vals, y_vals = generate_graph_data(eqn, x_min, x_max)
                    
                    # Plot the graph
                    fig, ax = plt.subplots()
                    ax.plot(x_vals, y_vals)
                    ax.grid(True)
                    st.pyplot(fig)
                except ValueError as e:
                    st.error(str(e))