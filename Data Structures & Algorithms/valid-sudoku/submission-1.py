class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSeen = defaultdict(set)
        rowSeen = defaultdict(set)
        squareSeen = defaultdict(set)


        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (board[i][j] in rowSeen[i] or 
                    board[i][j] in colSeen[j] or 
                    board[i][j] in squareSeen[(i // 3, (j // 3))]):
                    return False

                colSeen[j].add(board[i][j])
                rowSeen[i].add(board[i][j])
                squareSeen[(i // 3, j // 3)].add(board[i][j])

        return True


      # time complexity O(n * n) => O(1) since n is 9
      # space complexity O(n * n) => O(1) since n is 9
        
