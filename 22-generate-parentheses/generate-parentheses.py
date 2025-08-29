class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, "", 0, 0, n)
        return result
    
    def backtrack(self, result:List[str], current:str, open_count:int, close_count: int, max_count:int):
        if len(current) == max_count*2:
            result.append(current)
            return
        
        if open_count < max_count:
            self.backtrack(result, current + "(", open_count + 1, close_count, max_count)
        
        if close_count < open_count:
            self.backtrack(result, current + ")", open_count, close_count + 1, max_count)
