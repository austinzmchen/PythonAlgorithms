# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec0:
    """ inspired by "105. Construct Binary Tree from Preorder and Inorder Traversal"

        user both a preorder list and inorder list without "null" place holders
        to re-construct the tree
    """
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        p_ls = []
        def preorder(node):
            if not node:
                return None
            
            p_ls.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)

        in_ls = []
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            in_ls.append(node.val)
            inorder(node.right)
        inorder(root)

        print(f"{p_ls=}, {in_ls=}")
        return ",".join([str(n) for n in p_ls]) + ":" + ",".join([str(n) for n in in_ls])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        try:
            p_str, in_str = data.split(":")
            p_ls = p_str.split(",")
            in_ls = in_str.split(",")

            assert len(p_ls) == len(in_ls)
        except:
            raise("deserialize error")

        p = 0
        _dict = {v:i for i, v in enumerate(in_ls)}

        def recur(l, r):
            if l > r:
                return None
            
            nonlocal p
            v = p_ls[p]
            node = TreeNode(v)
            p += 1

            node.left = recur(l, _dict[v] - 1)
            node.right = recur(_dict[v] + 1, r)
            return node
        
        return recur(0, len(p_ls) - 1)
    

print(Codec0().deserialize("3,9,20,15,7:9,3,15,20,7"))
print(Codec0().deserialize(":"))

codec0 = Codec0()
codec0.serialize(codec0.deserialize("3,9,20,15,7:9,3,15,20,7"))
codec0.serialize(codec0.deserialize(":"))


class Codec:

    # use "#" in place of null
    def serialize(self, root):
        def recur(node):
            if not node:
                results.append("#")
                return
            results.append(str(node.val))
            recur(node.left)
            recur(node.right)

        results = []
        recur(root)
        return ' '.join(results)
        

    def deserialize(self, data):
        ls = data.split()
        idx = 0

        def recur():
            nonlocal idx
            if idx >= len(ls):
                return None
            if ls[idx] == "#":
                idx += 1
                return None

            node = TreeNode(ls[idx])
            idx += 1
            
            node.left = recur()
            node.right = recur()
            return node

        return recur()
 
 
print(Codec().deserialize("1 2 # # 3 4 # # 5 # #"))

codec = Codec()
codec.serialize(codec.deserialize("1 2 # # 3 4 # # 5 # #"))
      
      
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