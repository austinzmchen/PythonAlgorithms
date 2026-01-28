class Twitter:

    def __init__(self):
        self.inc = 1
        self.followees: [int, set] = {}
        self.tweet_by_user: [int, list[tuple]] = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_by_user.setdefault(userId, [])
        self.tweet_by_user[userId].append((self.inc, tweetId))
        self.inc += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        tuples = [t for followee in self.followees.get(userId, [])
                    for t in self.tweet_by_user.get(followee, [])]

        # add user's own feeds
        tuples += self.tweet_by_user.get(userId, [])
        tuples = sorted(tuples, reverse=True)
        return [t[1] for t in tuples[:10]]

    # use heap
    def getNewsFeed2(self, userId: int) -> List[int]:
        from heapq import heappush, heappop
        max_heap = []
        
        for inc, tweet_id in self.tweet_by_user.get(userId, []):
            heappush(max_heap, (-inc, tweet_id))
        
        for followee_id in self.followees.get(userId, []):
            for inc, tweet_id in self.tweet_by_user.get(followee_id, []):
                heappush(max_heap, (-inc, tweet_id))
        
        res = []
        for _ in range(min(10, len(max_heap))):
            _, tweet_id = heappop(max_heap)
            res.append(tweet_id)
        return res
    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees.setdefault(followerId, set())
        self.followees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees.get(followerId, set()):
            self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)