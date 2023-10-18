# method-dependent T & S complexity array and hashmap solution
class Twitter:
    def __init__(self):
        self.tweets = []    # array of [userId, tweetId] elements
        self.followers = {} # hashmap of (followeeId) -> set of followerId's

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if len(res) == 10:
                break
            posterId, tweetId = self.tweets[i]
            if (posterId == userId or
                (posterId in self.followers and
                userId in self.followers[posterId])):
                res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers:
            self.followers[followeeId] = set()
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers:
            self.followers[followeeId] = set()
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
