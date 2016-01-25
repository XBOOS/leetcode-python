#!/usr/bin/env python
# encoding: utf-8

"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated."""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows= [set() for _ in xrange(9)]
        columns = [set() for _ in xrange(9)]
        squares = [[set() for _ in xrange(3)]for _ in xrange(3)]
        for i in xrange(9):
            for j in xrange(9):
                char = board[i][j]
                if char == '.':
                    continue
                if char in rows[i]: return False
                else: rows[i].add(char)
                if char in columns[j]: return False
                else: columns[j].add(char)
                if char in squares[i/3][j/3]: return False
                else: squares[i/3][j/3].add(char)
        return True



