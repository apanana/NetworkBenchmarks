from scipy.stats import genextreme
from scipy.stats import genpareto

"""
Key-Size Distribution
We found the model that best fits key sizes in bytes (with a Kolmogorov-Smirnov distance of 10.5) 
to be Generalized Ex- treme Value distribution with parameters mu = 30.7984, sigma = 8.20449, k = 0.078688. 
We have verified that these param- eters remain fairly constant, regardless of time of day.
Value-Size Distribution
We found the model that best fits value sizes in bytes (with a Kolmogorov-Smirnov distance of 10.5), 
starting from 15 bytes, to be Generalized Pareto with parameters theta = 0, sigma = 214.476, k = 0.348238 
(this distribution is also independent of the time of day). The first 15 values of length and prob- abilities 
can be modeled separately as a discrete probability distribution whose values are given in Table 5.
"""
r = genextreme.rvs(c=0.078688, loc = 30.7984, scale = 8.20449, size=1000)
r = [int(x) for x in r]
print(r)

p = genpareto.rvs(c=0.348238 , loc = 0, scale = 214.476, size=1000)
p = [int(x) for x in p]
print(p)