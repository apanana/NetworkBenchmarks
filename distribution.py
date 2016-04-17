from scipy.stats import genextreme
from scipy.stats import genpareto
import sys

if sys.argv == None or len(sys.argv)!= 2:
	sys.exit()
n = int(sys.argv[1])

"""
Following is taken from the paper. (wrote greek letter names in full bc they don't exist in this character encoding)


	Key-Size Distribution
	We found the model that best fits key sizes in bytes (with a Kolmogorov-Smirnov distance of 10.5) 
	to be Generalized Ex- treme Value distribution with parameters mu = 30.7984, sigma = 8.20449, k = 0.078688. 
	We have verified that these param- eters remain fairly constant, regardless of time of day.
	Value-Size Distribution
	We found the model that best fits value sizes in bytes (with a Kolmogorov-Smirnov distance of 10.5), 
	starting from 15 bytes, to be Generalized Pareto with parameters theta = 0, sigma = 214.476, k = 0.348238 
	(this distribution is also independent of the time of day). The first 15 values of length and prob- abilities 
	can be modeled separately as a discrete probability distribution whose values are given in Table 5.


Below: c = k, loc = mu/theta, scale = sigma, size = user-specified
"""
rs = genextreme.rvs(c=0.078688, loc = 30.7984, scale = 8.20449, size=n)
rs = [str(int(r)) for r in rs]

ps = genpareto.rvs(c=0.348238 , loc = 0, scale = 214.476, size=n)
ps = [(p+1) for p in ps]
ps = [str(int(p)) for p in ps]

def p_to_c(xs):
	out = ""
	for x in xs:
		out += x + " "
	out += "\n"
	return out

outstring = p_to_c(rs) + p_to_c(ps)
print(outstring)