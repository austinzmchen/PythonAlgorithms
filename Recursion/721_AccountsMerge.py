from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        visited = set()
        dict = defaultdict(list)
        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                dict[account[j]].append(i)
        #
        # Perform DFS for accounts and add to results.
        res = []
        for i, account in enumerate(accounts):
            if i in visited:
                continue
            #
            name, emails = account[0], set()
            self.dfs(accounts, i, emails, visited, dict)
            res.append([name] + sorted(emails))
        return res
      
    # DFS code for traversing accounts.
    def dfs(self, accounts, curr_idx, emails, visited, dict):
        if curr_idx in visited:
            return
        #
        visited.add(curr_idx)
        for j in range(1, len(accounts[curr_idx])):
            email = accounts[curr_idx][j]
            emails.add(email)
            for idx in dict[email]:
                self.dfs(accounts, idx, emails, visited, dict)