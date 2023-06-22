import numpy as np
import plot

class triangle_theta:
    
    def __init__(self):
       self.kpts =[]
        
    def figure1(self):
        a = a
        b = b
        
        # |a|
        length_of_vector_a = np.sqrt((np.power(a[0], 2)) + np.power(a[1], 2))

        # |b|
        length_of_vector_b = np.sqrt(np.power(b[0], 2) + np.power(b[1], 2))

        # |a|⋅|b|
        scalar = length_of_vector_a * length_of_vector_b

        # a ⋅ b
        dotproduct = np.dot(a.T, b)

        # cos_theta값
        cos_theta = dotproduct / scalar

        # 각 사이 값 theta
        theta = np.arccos(cos_theta)*57.3




    def getkpts(self, kpts):
        self.kpts.append(kpts)



        
        
        
    












