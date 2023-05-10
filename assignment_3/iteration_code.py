def iterate(c, z0, max_iter=20):
   """iterates z equation below
   
   c - equation for complex plane, c= x + iy
   z0 - initial z
   max_iter - maximum iteration
   """
   it=0
   z=z0
   escape_iter=np.zeros([c.shape[0],c.shape[1]])

   for it in range(max_iter):
       it+=1
       z= z*z + c
       r = np.abs(z)
       for i in range(c.shape[0]):
           for j in range(c.shape[1]): 
               if (escape_iter[i,j] == 0) & (r[i,j] > 10):
                   escape_iter[i,j]=it
   return escape_iter
               
