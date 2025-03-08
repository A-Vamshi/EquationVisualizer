# Equation Visualizer

## Overview
Equation Visualizer is a Streamlit-based web application that allows users to input mathematical expressions, convert them into valid SymPy expressions using Gemini AI, and plot their graphs.

## Features
- Accepts mathematical expressions with `x` as the only variable.
- Uses Google Gemini AI to correct and convert input expressions into SymPy-compatible format.
- Plots the function using Matplotlib.
- Handles errors such as undefined variables, division by zero, and invalid syntax.

## Requirements
Ensure you have the following installed:

- Python 3.8+
- Required Python libraries:
  ```sh
  pip install streamlit sympy numpy matplotlib google-generativeai python-dotenv
  ```
- A valid OpenAI API key stored in a `.env` file:
  ```sh
  echo "API_KEY=your_google_api_key_here" > .env
  ```

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/A-Vamshi/EquationVisualizer.git
   cd EquationVisualizer
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   streamlit run app.py
   ```

4. Enter a mathematical expression in the input box and click "Graph the equation."

## Example Inputs & Outputs

| Input Expression   | Converted SymPy Expression |
|--------------------|--------------------------|
| `x^2 + 3*x + 2`   | `x**2 + 3*x + 2`         |
| `sin(x) + cos(x)` | `-1` (invalid input)     |
| `5x^2 + 2x + 3`   | `5*x**2 + 2*x + 3`       |

## Project Structure
```
├── app.py  # Main application script
├── requirements.txt  # Dependencies
├── .env  # API key storage
├── README.md  # Documentation
```

## Contribution
Feel free to contribute by submitting issues or pull requests.

## License
MIT License

