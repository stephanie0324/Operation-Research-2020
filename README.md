# Operation-Research-2020
## Week 1 (3/5)
    1. Case 1
    沒有使用任何演算法或是數學方法來做最佳化的排程
## Week 2 (3/12) - Linear Programming
    1. The Graphical Approach
    2. Three Types of Linear Program     
## Week 3 (3/19) - The simplex method
    1. The standard form
        * non-negative right hand side
        * non-negative variables
        * equality constraints (using slack var. to fill in the gaps)
    2. Basic solutions
        * bfs - basic feasible soultion 
        * adjacent bfs
    3. The simplex method
    4. The tableau represntation
        * maximization - negative numbers
        * minimization - positive numbers
    5. Unbounded LPs
    6.Infeasible LPs
## Week 4 (3/26) - Application of linear programming
    1. Material Blending
    2. Linearizing maximum/ minimum function
         * linearizing constraints
    3. AMPL
        * cd '' ;
        * model ;
        * data ;
        * solve ;

## Week 5 (4/9) - Linear Program Duality
     1. Primal-dual pairs
        * original -> primal , new -> dual
        * find upper bound
           < primal max => dual min >
                a. primal objectives  vs dual RHS
                    positive -> " >= " 
                    negatuve -> " <= "
                    free     -> " == "
                b. primal RHS => dual objectives
                    >= -> " <=0 "
                    <= -> " >=0 "
                    == -> free variable
            < primal min => dual max>
                all reverse
        * original -> primal , new -> dual
        * find upper bound
| obj.fun. | max | min | obj.fun. |
|---------:|----:|----:|---------:|
| constraints | <= | >=0 | variables |
|             | >= | <=0 |           |
|             | == | free |          |
| variables   | >=0 | >= | constraints |
|             | <=0 | <= |             |
|             | free | == |            |

     2. Duality theorems
     
     3. Shadow prices
