class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1. DFS algo
        2. Visited set so that we don't use the same letter twice
        3. Out of bounds check
        4. Backtrack
        """
        if not word or not board:
            return False
        
        def dfs(i, j, word):
            """
            backtracking with side-effect,
            the matched letter in the board would be marked with "#".
            """
            # bottom case: we find match for each letter in the word
            if len(word) == 0:
                return True
            
            # Check the current status, before jumping into backtracking
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
                return False
        
            board[i][j] = "#"
            
            for row_offset, col_offset in directions:
                if dfs(i + row_offset, j + col_offset, word[1:]):
                    return True
            
            # backtracking
            board[i][j] = word[0]
            
            return False
        
        R = len(board)
        C = len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                    if dfs(i, j, word):
                        return True
                    
        return False
            
        