import numpy as np
from numpy.fft import fft, ifft


# You're given two dice:
# Die A has faces: [1, 2, 3]
# Die B has faces: [2, 3, 4]

# Count how many ways you can roll the two dice 
# to get every possible total sum.


# Brute Force DP
# A = [1, 2, 3]
# B = [2, 3, 4]

# dp = [0] * 10

# for a in A:
#     for b in B:
#         dp[a+b] +=1

# for n in range(len(dp)):
#     print(f'dp[{n}] = {dp[n]}')
    
# dp[0] = 0, dp[1] = 0, dp[2] = 0, dp[3] = 1, dp[4] = 2, dp[5] = 3, dp[6] = 2
# dp[7] = 1, dp[8] = 0, dp[9] = 0

    
# FFT
A_poly = [0, 1, 1, 1] # Index is the face value and coefficient is the count
B_poly = [0, 0, 1, 1, 1]



n = len(A_poly) + len(B_poly) - 1
A_pad = np.pad(A_poly, (0, n-len(A_poly)))
print(A_pad)

B_pad = np.pad(B_poly, (0, n-len(B_poly)))
print(B_pad)

A_fft = fft(A_pad)
B_fft = fft(B_pad)
C_fft = A_fft * B_fft
C = np.round(ifft(C_fft).real).astype(int)

print(C)