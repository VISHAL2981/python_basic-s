def compoundintrest(principle,rate,time):
   
   Amount = principle*(pow((1+rate/100),time))

   CI = Amount - principle
   print("Compound interest is", CI)

compoundintrest(10000, 10.25, 5)


