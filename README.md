# Task 1

## Project setup:

1) ### Clone the project:
                
        git  clone git@github.com:Blank000/PythonScripts.git
2) ### Installing the project dependencies:

         Having python installed is sufficient (better to have 3.x version)
3) ### Running the script:

         cd scripts
   
         python run.py x y z

### Script Response:
   1) 
          When all of the parameters passed to the script i.e x, y, z are integral values 
          
          Then after filtering the numbers from the range [13, 14] and [17, 19] inclusive, the script 
          should return the sum of all these three numbers.

   2) 
          If any one of x, y, z is not an integer value,
          Expected output from the script:

          >> "All inputs must be numeric"
      
   3) 
          When the number of paremeters passed to the function is less than or 
          more than three, then below is the response expected from the script:
          
          >> "Exactly 3 numbers are required"

## Testing:
   Unittest framework is integrated. To run all the tests, run the below command:
    
    python -m unittest

