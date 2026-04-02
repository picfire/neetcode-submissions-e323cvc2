class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        equation = []

        for num in tokens:
            try:
                index = int(num)
                equation.append(index)

            except ValueError:
                val2= equation.pop()
                val1= equation.pop()
                    

                if num == '+':
                    equation.append(val1 + val2)
                elif num == '-':
                    equation.append(val1 - val2)
                elif num == '*':
                    equation.append(val1 * val2)
                elif num == '/':
                    equation.append(int(val1 / val2))
                    
                    
        return equation[-1]
        
