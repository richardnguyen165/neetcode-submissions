class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        all_answers = []
        number_of_chars = n * 2

        def produceParenthesis(current_string, current_stack, open_bracket_count, close_bracket_count):
            
            
            if len(current_string) == number_of_chars:
                if len(current_stack) == 0:
                    all_answers.append(current_string)
                return
            
            # Add (
            if open_bracket_count < n:
                new_current_string = current_string[:]
                new_current_string += "("

                new_current_stack = current_stack[:]
                new_current_stack.append("(")
                
                produceParenthesis(new_current_string, new_current_stack, open_bracket_count + 1, close_bracket_count)
            
            # Add )
            # cannot have ")"
            if close_bracket_count < n and len(current_stack) > 0:
                new_current_string = current_string[:]
                new_current_string += ")"

                new_current_stack = current_stack[:]
                if current_stack[-1] == "(":
                    new_current_stack.pop()
                else:
                    new_current_stack.append(")")
                
                produceParenthesis(new_current_string, new_current_stack, open_bracket_count, close_bracket_count + 1)

            return 
        
        produceParenthesis("", [], 0, 0)
        return all_answers