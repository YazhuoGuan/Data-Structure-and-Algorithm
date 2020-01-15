class Solution(object):
    def is_valid(self, parentheses:str):
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in parentheses:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] !=top_element:
                    return False
            else:
                stack.append(char)
        
        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack