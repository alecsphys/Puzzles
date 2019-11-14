Problem
-----------------------------------------
You are on a grid of integers NxN in the position (0,0) and you have to go to the position (N,N).
Only steps toward North and East  directions are allowed. How many different paths you can build that live 
totally above the diagonal connecting (0,0) with (N,N)? Can you design an efficient (in time and space) 
algorithm to fully enumerate all those paths?

Notes
-----------------------------------------
- The second algorithm is absolutely much faster, even without implementing any parallelization, but using it sequentially.

References
-----------------------------------------
- Matej Crepinsek and Luka Mernik2. AN EFFICIENT REPRESENTATION FOR SOLVING CATALAN NUMBER RELATED PROBLEMS. 
International Journal of Pure and Applied Mathematics. Volume 56 No. 4 2009, 589-604
          
ERRATA CORRIGE:
-----------------------------------------
- into the pseudocode of the first algorithm the function expanding East is wrong. Essentially the condition to add the East step must be:
EastSteps < NorthSteps
