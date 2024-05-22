# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        def recur(node):
            if not node:
                results.append("#")
                return
            results.append(str(node.val))
            recur(node.left)
            recur(node.right)
        #
        results = []
        recur(root)
        return ' '.join(results)
        

    def deserialize(self, data):
        ls = data.split()
        index = 0
        #
        def recur():
            nonlocal index
            if index >= len(ls):
                return None
            if ls[index] == "#":
                index += 1
                return None
            #
            n = TreeNode(ls[index])
            index += 1
            n.left = recur()
            n.right = recur()
            return n
        #
        return recur()
 
 
print(Codec().deserialize("1 2 # # 3 4 # # 5 # #"))           
      
class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: 
            return ""
        #
        res = []
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            if not node:
                res.append(None)
                continue
            #
            res.append(node.val)
            q.append(node.left if node.left else None)
            q.append(node.right if node.right else None)
        #
        return ','.join([str(v) for v in res])
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        #
        queue = [int(v) if v != "None" else None for v in data.split(",")]
        if len(queue) == 0:
            return None
        #
        print(f"queue: {queue}")
        root = TreeNode(queue.pop(0))
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            v_left = queue.pop(0)
            if v_left != None:
                node.left = TreeNode(v_left)
                q.append(node.left)
            #
            v_right = queue.pop(0)
            if v_right != None:
                node.right = TreeNode(v_right)
                q.append(node.right)
        #
        return root