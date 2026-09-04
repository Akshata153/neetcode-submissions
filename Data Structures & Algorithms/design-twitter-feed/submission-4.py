class Twitter:

    def __init__(self):
        self.count=0
        self.followingmap=defaultdict(set)
        self.tweetmap=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        self.followingmap[userId].add(userId)

        maxheap=[]
        #push latest tweet of all followees of userID
        for followingIds in self.followingmap[userId]:
            idx=len(self.tweetmap[followingIds])-1
            if idx >=0:
                cnt,tid=self.tweetmap[followingIds][idx]
                heapq.heappush(maxheap,[-cnt,tid,idx-1,followingIds])
        
        #get recent 10tweets
        res=[]
        # print(maxheap)
        while maxheap and len(res)<10:
            cnt,tid,idx,followingIds=heapq.heappop(maxheap)
            res.append(tid)
            if idx>=0:
                cnt,tid=self.tweetmap[followingIds][idx]
                
                heapq.heappush(maxheap,[-cnt,tid,idx-1,followingIds])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingmap[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingmap[followerId]:
            self.followingmap[followerId].remove(followeeId)

        
