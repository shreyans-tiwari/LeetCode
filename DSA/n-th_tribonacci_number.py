"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""

def tribonacci(self, n: int) -> int:
  series = [0, 1, 1]

  if n < 3:
    return series[n]
        
  i = 3
  while i <= n:
    series.append(series[i-1]+series[i-2]+series[i-3])
    i += 1
        
  return(series[-1])
