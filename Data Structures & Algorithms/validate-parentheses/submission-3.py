class Solution:
    def isValid(self, s: str) -> bool:
        temp = []

        matching = [(')', '('),(']', '['),('}', '{')]

        for char in s: 
            if char in "([{":
                temp.append(char)
            elif char in ")]}": 
                if not temp:
                    return False
                for closing, opening in matching:
                    if char == closing:
                        if temp[-1] == opening:
                            temp.pop()
                            found = True
                            break
                        else:
                            return False
                if not found:
                    return False
            else:
                return False
        return len(temp) == 0
