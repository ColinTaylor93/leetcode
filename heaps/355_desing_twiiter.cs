using System;
using System.Collections.Generic;

/// <summary>
/// Class <c>Twitter</c> is am mock simplified version of Twitter
/// </summary>
public class Twitter
{

    private int time;
    private Dictionary<int, List<(int time, int tweetId)>> tweets;
    private Dictionary<int, HashSet<int>> follows;

    public Twitter()
    {
        // variable used for tracking when tweets are added so the most recent ones can be used
        time = 0;
        // hashmap for storing tweets
        tweets = new Dictionary<int, List<(int, int)>>();
        // again for followers
        follows = new Dictionary<int, HashSet<int>>();
    }

    public void PostTweet(int userId, int tweetId)
    {
        if (!tweets.ContainsKey(userId))
            tweets[userId] = new List<(int, int)>();

        tweets[userId].Add((time++, tweetId));
    }

    public IList<int> GetNewsFeed(int userId)
    {
        var result = new List<int>();
        var heap = new PriorityQueue<(int time, int tweetId), int>();

        // Ensure user exists
        if (!follows.ContainsKey(userId))
            follows[userId] = new HashSet<int>();

        // User should see their own tweets
        follows[userId].Add(userId);

        foreach (var followee in follows[userId])
        {
            if (!tweets.ContainsKey(followee)) continue;

            foreach (var tweet in tweets[followee])
            {
                // Use negative time to simulate max-heap
                heap.Enqueue(tweet, -tweet.time);
            }
        }

        // Get top 10 most recent tweets
        while (heap.Count > 0 && result.Count < 10)
        {
            result.Add(heap.Dequeue().tweetId);
        }

        return result;
    }

    public void Follow(int followerId, int followeeId)
    {
        if (followerId == followeeId) return;

        if (!follows.ContainsKey(followerId))
            follows[followerId] = new HashSet<int>();

        follows[followerId].Add(followeeId);
    }

    public void Unfollow(int followerId, int followeeId)
    {
        if (followerId == followeeId) return;

        if (follows.ContainsKey(followerId))
            follows[followerId].Remove(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.PostTweet(userId,tweetId);
 * IList<int> param_2 = obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */