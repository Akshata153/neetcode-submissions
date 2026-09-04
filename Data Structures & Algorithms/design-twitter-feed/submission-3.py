class Twitter:

    def __init__(self):
        self.count=0
        self.tweetmap=defaultdict(list) # userid: [cnt,tweetid]
        self.followermap=defaultdict(set)# userid : [followerid]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count+=1

        

    def getNewsFeed(self, userId: int) -> List[int]:

        maxheap=[]
        self.followermap[userId].add(userId)
        for followersid in self.followermap[userId]:
            #get idx of last tweet
            idx=len(self.tweetmap[followersid])-1
            #get latest post of followers and put in maxheap
            if idx>=0:
                cnt,tid=self.tweetmap[followersid][idx]
                heapq.heappush(maxheap,[-cnt,followersid,idx-1,tid])

        res=[]
        while maxheap and len(res)<10:
            cnt,followersid,idx,tid=heapq.heappop(maxheap)
            res.append(tid)
            if idx>=0 :
                cnt,tid=self.tweetmap[followersid][idx]
                heapq.heappush(maxheap,[-cnt,followersid,idx-1,tid])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followermap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followermap[followerId]:
            self.followermap[followerId].remove(followeeId)
        
