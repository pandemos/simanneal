# A reusable implementation of the Simulated Annealing metaheuristic for optimization problems

## Installation

1. Run build.bat (Windows) or build.sh (unix) (creates dist/ folder if absent)
2. Change to dist/ and unpack compressed distribution
3. Change to unpacked distribution folder
4. run: sudo python setup.py install

This will install the simaneal package to Libs/site-packages

## Files

- MANIFEST.in		-	Defines what will be in the final installer tarball
- README			-	This file
- runner			-	Python script to import this application's modules and launch
- setup.py		-	distutil setup file
- simanneal/		-	Simulated Annealing Package
	- \_\_init\_\_.py	-	Used by distutils to find the package root, should be empty
	- Annealer.py	-	Core implementation
- samples/	-	Sample package
	- \_\_init\_\_.py		-	Used by distutils to find the package root, should be empty
	- samplebase.py	-	Base class for samples, implements some simple defaults, children should only override what changes
	- trivial.py		-	Sample of using Annealer to optimize a small one-dimensional array
	- twodimensional.py	-	Sample of using Annealer to optimize a small two-dimensional array
	- threedimensional.py	-	Guess what this does.
	- visualizer.py		-	tkinter-based visualizer with threading for Annealer results (reusable for other data)
- tests/		-	Unit tests
	- annealer.py			- Unit tests for the core Annealer module
	- twodimensional.py	- Unit tests for Sample, as implemented in twodimesional (yeah, unusual)

## Interesting samples
    - `samples/twodimensional.py` - Command line run of simulated annealing in two dimensions using random starting data and interesting default values.
    - `samples/threedimensional.py` - Command line run of simulated annealing in three dimensions using random starting data and interesting default values.
    - `samples/sample_visualizer.py` - tkinter-based UI. Use 'random' to generate a random starting state or import some JSON data to start. the 'improve' button runs until the total energy of the system improves once. The 'anneal' button runs until a maximum energy threshold is reached. Requires tk to be installed on the host system.

## Tests

Unit test coverage exists in /test. To run it with code coverage:

```
coverage run test/annealer.py
coverage run test/twodimensional.py
```

Then view the code coverage report:

```
coverage report -m
```
## Call Graph

pycallgraph support is included. To use it, you must be in the appropriate directory. This example runs the two dimensional sample and generate the call graph in `pycallgraph.png`:

```
pushd samples ; pycallgraph graphviz -- ./twodimensional.py ; popd
```
