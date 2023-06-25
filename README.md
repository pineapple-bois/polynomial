# Creation of class `Polynomial`

----

The `Polynomial` class is a Python implementation that represents polynomials and provides various operations on polynomials. It allows you to create, evaluate, manipulate, approximate roots and plot polynomials easily.

Where a polynomial in a single indeterminate $x$ can be written in the form, 
$a_n x^n+a_{n-1} x^{n-1}+\cdots+a_2 x^2+a_1 x+a_0$

----

`poly_dict.py` contains a function `decompose_polynomial` which takes a polynomial equation as a string and extracts the coefficients of each term. It returns a dictionary where the keys are the powers and the values are the corresponding coefficients.

----

##### `Polynomial` features
- Creation using a dictionary format for coefficients.
- Evaluation for a given value of `x`.
- String representation.
- Approximating roots numerically by the [Newton-Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method)
- Addition, subtraction and multiplication
- Computation of the derivative.
- Plotting using `matplotlib`.

----

##### `Polynomial` usage

```python
# Create a Polynomial object with coefficients {3: 2, 2: -1, 0: 1}:
p = Polynomial({3: 2, 2: -1, 0: 1})

# Evaluate the polynomial for x = 2:
result = p(2)

# Print the string representation of the polynomial:
print(p)

# Add two polynomials:
p1 = Polynomial({2: 3, 1: 1})
p2 = Polynomial({3: 2, 2: -1, 0: 1})
p3 = p1 + p2

# Subtract two polynomials:
p4 = p1 + p2

# Multiply two polynomials:
p5 = p1 * p2

# Compute the derivative of the polynomial:
dp = p.derivative()

# Plot the polynomial:
p.plot()
```
----
##### Installation 

Uses; 
`Python 3.9`
`matplotlib 3.6.2`
`numpy 1.23.4`
`regex 2022.10.31`

Install the required dependencies from the `requirements.txt` file: 

```bash
pip install -r requirements.txt
```

----
