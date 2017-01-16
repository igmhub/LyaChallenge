# LyaChallenge

Repository used to coordinate different Lyman-alpha data challenges.

We will start by a data challenge on P1D emulators, with the idea of extending it to P3D and bispectra emulators. Other future ideas include data challenges related to estimator of power spectra / correlation functions and BAO fitters.

Modules required:
 - numpy
 - pylab
 - matplotlib
 - decimal

Main parts: 
 - ResultsP1D: compilation of published P1D measurements, and simple objects to read them.
 - TheoryP1D: compilation of P1D theories, used to generate mocks.
 - MockP1D: code to make mock P1D measurements using a given covariance matrix.
 - Examples: short python code to make plots and mocks.
