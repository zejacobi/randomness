# Randomness
Python module (hopefully? eventually?) to test distributions and strings of 
numbers/letters for randomness

## Installing
1) Install Python 3.X
1) Create a virtual environment in the project folder with `virtualenv -p python3 venv`
1) Activate the virtual environment with `source venv/bin/activate`

## Using
You can look at a comparison of the system PRNG and the Randu PRNG with `example.py`

## Glossary
* **PRNG**: Pseudo-random number generator. An algorithm that creates a string of numbers with many
  of the properties of true random numbers, but with a deterministic order. Should not be used for
  cryptographic purposes, because it is possible to guess all subsequent numbers if you know where
  in the sequence you are.
* **Seed**: A parameter that determines where to start in a PRNG sequence.
* **epsilon**: A Greek letter. Used in engineering to represent the absolute error between a 
  estimated value and the true value.