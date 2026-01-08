class Twitter:

    def __init__(self):
        self.inc = 1
        self.f_dict: [int, [int]] = {}
        self.tweet_by_user: [int, list[tuple]] = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_by_user.setdefault(userId, [])
        self.tweet_by_user[userId].append((self.inc, tweetId))
        self.inc += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        tuples = [t for followee in self.f_dict.get(userId, [])
                    for t in self.tweet_by_user.get(followee, [])]

        # add user's own feeds
        tuples += self.tweet_by_user.get(userId, [])
        tuples = sorted(tuples, reverse=True)
        return [t[1] for t in tuples[:10]]

    # use heap
    def getNewsFeed2(self, userId: int) -> List[int]:
        from heapq import heappush, heappop
        max_heap = []
        
        for t in self.tweet_by_user.get(userId, []):
            heappush(max_heap, (-t[0], t[1]))
        
        for followee_id in self.f_dict.get(userId, []):
            for t in self.tweet_by_user.get(followee_id, []):
                heappush(max_heap, (-t[0], t[1]))
        
        res = []
        for _ in range(min(10, len(max_heap))):
            _, tweet_id = heappop(max_heap)
            res.append(tweet_id)
            
        return res
    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.f_dict.setdefault(followerId, [])
        self.f_dict[followerId] = list(set(self.f_dict[followerId] + [followeeId]))


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.f_dict.get(followerId, []):
            self.f_dict.get(followerId, []).remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)