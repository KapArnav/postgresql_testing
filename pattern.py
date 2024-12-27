class Pyramid:
    def __init__(self, num_lines):
        self.num_lines = num_lines
        self.print_pyramid()
    
    def print_pyramid(self):
        
        for i in range(self.num_lines):
            for j in range(self.num_lines - i - 1):
                print(" ", end="")
                
            for k in range(2*i+1):
                print("*", end="")
                
            print()
            
num_lines = int(input("Enter the number of lines for the pyramid: "))

Pyramid = Pyramid(num_lines)

