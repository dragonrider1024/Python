#!/usr/bin/python
import wordsearch
s=wordsearch.Solution()
board=[ ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
	]
word="ABCB"
print len(board)
print len(board[0])
print len(word)
print s.exist(board,word)
