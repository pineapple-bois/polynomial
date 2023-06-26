import numpy as np
import matplotlib.pyplot as plt


class Polynomial:
    """
    Attributes:
        coefficients (dict): A dictionary representing the polynomial coefficients in the form {power: coefficient}.
                             The keys are the powers and the values are the corresponding coefficients

    Example usage:
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

        # Multiply two polynomials:
        p4 = p1 * p2

        # Compute the derivative of the polynomial:
        dp = p.derivative()

        # Plot the polynomial:
        p.plot()
    """
    def __init__(self, coefficients: dict):
        if not isinstance(coefficients, dict):
            raise ValueError("Coefficients must be provided as a dictionary.")

        for power, coefficient in coefficients.items():
            if not (isinstance(power, int) and isinstance(coefficient, (int, float))):
                raise ValueError("Powers must be integers and coefficients may be integers or floats.")

        self._coeff = coefficients

    @property
    def coeff(self):
        return self._coeff

    @coeff.setter
    def coeff(self, value):
        self._coeff = value

    def __call__(self, x):
        value = 0
        for power, coeff in self.coeff.items():
            value += coeff * x ** power
        return value

    def __repr__(self):
        """" return code for regenerating this instance"""
        return f"Polynomial({self.coeff})"

    def __str__(self):
        terms = []
        for power, coeff in sorted(self.coeff.items(), reverse=True):
            if power == 0:
                term = str(coeff)
            elif power == 1:
                term = (
                    "-x" if coeff == -1.0 else
                    "x" if coeff == 1.0 else
                    f"{round(coeff, 4) if '.' in str(coeff) and len(str(coeff).split('.')[1]) > 4 else coeff} * x"
                )
            else:
                term = (
                    f"-x^{power}" if coeff == -1.0 else
                    f"x^{power}" if coeff == 1.0 else
                    f"{round(coeff, 4) if '.' in str(coeff) and len(str(coeff).split('.')[1]) > 4 else coeff} * x^{power}"
                )
            terms.append(term)

        string = " + ".join(terms)
        string = string.replace(" + -", " - ")
        string = string.replace("x^1 ", "x ")
        if string.startswith(" + "):
            string = string[3:]
        elif string.startswith(" - "):
            string = "-" + string[3:]

        return string

    def __add__(self, other):
        coeffsum = {}

        for power, coeff in self.coeff.items():
            coeffsum[power] = coeff

        for power, coeff in other.coeff.items():
                if power in coeffsum:
                    coeffsum[power] += coeff
                else:
                    coeffsum[power] = coeff

        return Polynomial(coeffsum)

    def __sub__(self, other):
        coeffdiff = {}

        for power, coeff in self.coeff.items():
            coeffdiff[power] = coeff

        for power, coeff in other.coeff.items():
            if power in coeffdiff:
                coeffdiff[power] -= coeff
            else:
                coeffdiff[power] = -coeff

        return Polynomial(coeffdiff)

    def __mul__(self, other):
        coeff = {}

        for power1, coeff1 in self.coeff.items():
            for power2, coeff2 in other.coeff.items():
                power = power1 + power2
                product = coeff1 * coeff2

                if power in coeff:
                    coeff[power] += product
                else:
                    coeff[power] = product

        return Polynomial(coeff)

    def plot(self, x_min=-10, x_max=10, num_points=1000):
        x = np.linspace(x_min, x_max, num_points)
        y = [self(x_val) for x_val in x]

        plt.plot(x, y)
        plt.axhline(0, color='r', linewidth=0.25)  #
        formula = self.__str__()
        formula = formula.replace('*', '')
        plt.title(f'${formula}$')
        plt.grid(True)
        plt.show()

    def newton(self, x0, max_it=20, tol=1e-3):
        """
        Performs Newton's method to find a root of a function.

        Args:
            x0 (float): The initial guess for the root.
            max_it (int, optional): The maximum number of iterations. Defaults to 20.
            tol (float, optional): The tolerance for convergence. Defaults to 1e-3.

        Returns:
            tuple: A tuple containing the following elements:
                - The estimated root of the function.
                - A boolean indicating whether convergence was achieved within the maximum number of iterations.
                - The number of iterations performed.
        """
        iter = 0  # Initialize the iteration counter

        # Check if the initial guess is very close to a root
        if abs(self(x0)) < tol:
            return x0, True, iter

        # Continue iterating until the maximum number of iterations is reached
        while iter < max_it:
            f0 = self(x0)  # Evaluate the function at the current guess
            dfdx0 = self.derivative()(x0)  # Evaluate the derivative of the function at the current guess

            if abs(f0) < tol:
                # Convergence achieved, return the estimated root, convergence status, and number of iterations
                return x0, True, iter

            if abs(dfdx0) < tol:
                # Newton's method fails to converge due to zero derivative
                raise RuntimeError("Newton's method failed to converge.")

            x1 = x0 - f0 / dfdx0  # Compute the next guess for the root
            if abs(x1 - x0) < tol:
                # Convergence achieved, return the estimated root, convergence status, and number of iterations
                return x1, True, iter

            x0 = x1  # Update the current guess
            iter += 1  # Increment the iteration counter

        return x0, False, iter

    def differentiate(self):
        coeff = {}
        for power, coefficient in self.coeff.items():
            if power > 0:
                if coefficient == 1:
                    if power == 1:
                        coeff[power - 1] = 1
                    else:
                        coeff[power - 1] = power
                elif coefficient == -1:
                    if power == 1:
                        coeff[power - 1] = -1
                    else:
                        coeff[power - 1] = -power
                else:
                    coeff[power - 1] = power * coefficient
        self.coeff = coeff
        if not self.coeff:  # If the resulting coefficients are empty, add the zero coefficient.
            self.coeff[0] = 0

    def derivative(self):
        dpdx = Polynomial(self.coeff.copy())  # Create a copy of self.coeff
        dpdx.differentiate()
        return dpdx

    def integrate(self):
        pass