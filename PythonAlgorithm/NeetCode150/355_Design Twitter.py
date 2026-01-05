class Twitter:

    def __init__(self):
        self.inc = 1
        self.f_dict: [int, [int]] = {}
        self.tweet_by_user: [int, tuple] = {}


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