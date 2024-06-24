print("WELCOME TO CALCULATOR")
while True:
   try:
       cal= input("Enter the calculation (or 'quit' to exit): ")
       if cal.lower() == 'quit':
           break
       
       else:
           result = eval(cal)
           print(f"The result is: {result:.2f}")

   except Exception as e:
       print(f"Error: {e}")
    
           
           
