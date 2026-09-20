#### Binary Trees

##### Leaf Detection
Pattern: The function takes in.
1. track.
2. root: choice list.
```python
def dfs(root):
    if not root:
        return
    # Make choice
    track+=root.val
    if not root.left and not root.right:
        # return True or res.append(track[:])
        return
    dfs(track,root.left)
    dfs(track,root.right)
```
Function call examples: 
1. helper(0,root) in Problem 112: hasPathSum.
2. helper(track,root) in Problem 257: binaryTreePaths.
<br></br>

Example: Problem 257: binaryTreePaths
```python
class TreeNode():
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution(object):
    def binaryTreePaths(self,root):
        res=[]
        track=[]
        def helper(track,root):
            if not root:
                return
            track.append(root.val)
            if not root.left and not root.right:
                res.append(track[:])
            helper(track,root.left)
            helper(track,root.right)
            track.pop()

        helper(track,root)
        return res

        # res=[]
        # track=""
        # def helper(track,root):
        #     if not root:
        #         return
        #     track+=str(root.val)
        #     if not root.left and not root.right:
        #         res.append(track[:])
        #     helper(track+"->",root.left)
        #     helper(track+"->",root.right)
        #     track=track[:-1]

        # helper(track,root)
        # return res
```
Note:  
1. `track.pop()` is used if track is a list, i.e. initialized as track=[]. 
2. `track=track[:-1]` is used when track is a string, i.e. initialized as track="".

#### Backtracking
Pattern: The function takes in.
1. track.
2. choice list: can be depth, used array, etc.
Pattern:
```python
res=[]
def dfs(track,choice_list):
    # Termination condition
    if termination_condition_met:
        res.append(track[:])
        return
    for choice in choice_list:
        # Make choice
        track.append(choice)
        dfs(track,choice_list)
        # Undo choice/backtrack
        track.pop()
```
        
Function call examples: 
1. helper(track,0) in Problem 78: Subsets.
2. helper(track,1) in Problem 77: Combination.
3. helper(track,0) in Problem 17: LetterCombinations.
<br></br>

Example: Problem 46: Permutation
```python
class Solution(object):
    def permute(self,nums):
        res=[]
        track=[]
        used=[False]*len(nums)
        def helper(track,used):
            if len(track)==len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Make choice
                used[i]=True
                track.append(nums[i])
                helper(track,used)
                # Backtrack
                used[i]=False
                track.pop()

        helper(track,used)
        return res
```