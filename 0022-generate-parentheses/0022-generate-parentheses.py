class Solution:


    def generateParenthesis(self, n: int) -> List[str]:
        def opening(string):
            count = 0
            for i in string:
                if i == "(":
                    count += 1
            return count
        strings = []
    
        def dfs(open_count, close_count, string):
            if len(string) == n * 2:
                strings.append(string)
                return

            # Add an opening parenthesis if we still have some left
            if open_count < n:
                dfs(open_count + 1, close_count, string + "(")

            # Add a closing parenthesis if the number of closing parentheses is less than the number of open ones
            if close_count < open_count:
                dfs(open_count, close_count + 1, string + ")")

        dfs(0,0, "")

        return strings
            

        
            
        