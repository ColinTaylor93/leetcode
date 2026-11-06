using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] CountServers(int n, int[][] logs, int x, int[] queries) {
        // Sort logs by their timestamp
        var sortedLogs = logs.OrderBy(l => l[1]).ToArray();
        
        // Pair queries with their original indices and sort by query time value
        var sortedQueries = queries
            .Select((q, index) => new { Query = q, Index = index })
            .OrderBy(q => q.Query)
            .ToArray();

        int[] result = new int[queries.Length];
        var serverCounts = new Dictionary<int, int>();
        
        int addIdx = 0;
        int remIdx = 0;
        int m = sortedLogs.Length;

        // Process each query chronologically using a sliding window
        foreach (var qObj in sortedQueries) {
            int r = qObj.Query;
            int l = r - x;

            // Add logs that fall into the window's upper bound (time <= r)
            while (addIdx < m && sortedLogs[addIdx][1] <= r) {
                int serverId = sortedLogs[addIdx][0];
                if (!serverCounts.ContainsKey(serverId)) {
                    serverCounts[serverId] = 0;
                }
                serverCounts[serverId]++;
                addIdx++;
            }

            // Remove old logs that fall outside the window's lower bound (time < l)
            while (remIdx < m && sortedLogs[remIdx][1] < l) {
                int serverId = sortedLogs[remIdx][0];
                serverCounts[serverId]--;
                if (serverCounts[serverId] == 0) {
                    serverCounts.Remove(serverId);
                }
                remIdx++;
            }

            // The servers with zero requests are the total servers minus those in the window
            result[qObj.Index] = n - serverCounts.Count;
        }

        return result;
    }
}