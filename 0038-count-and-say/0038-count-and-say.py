class Solution:
    def countAndSay(self, n: int) -> str:
        rle = {1:'1'}

        def traverse(string):
            freq = 1
            curr = string[0]
            res = ''
            for index in range(1,len(string)):
                if string[index] == curr:
                    freq +=1
                else:
                    res = res  + str(freq) + str(curr)
                    freq = 1
                    curr = string[index]
            res = res + str(freq) + str(curr)
            return res


        def dfs(n):
            if n == 1:
                return rle[1]
            if n not in rle:
                rle[n] = traverse(dfs(n-1))
            return rle[n]
        return dfs(n)
        
            
                



                    

            
            


        