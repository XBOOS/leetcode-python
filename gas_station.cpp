/*
 * There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
 *
 * You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
 *
 * Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
 *
 * Note:
 * The solution is guaranteed to be unique.
 *
 */

//From others.
/* Great explanation:
 * We prove the following statement. If sum of all gas[i]-cost[i] is greater than or equal to 0, then there is a start position you can travel the whole circle. Let i be the index such that the the partial sum
 *
 * gas[0]-cost[0]+gas[1]-cost[1]+...+gas[i]-cost[i]
 * is the smallest, then the start position should be start=i+1 ( start=0 if i=n-1). Consider any other partial sum, for example,
 *
 * gas[0]-cost[0]+gas[1]-cost[1]+...+gas[i]-cost[i]+gas[i+1]-cost[i+1]
 * Since gas[0]-cost[0]+gas[1]-cost[1]+...+gas[i]-cost[i] is the smallest, we must have
 *
 * gas[i+1]-cost[i+1]>=0
 * in order for gas[0]-cost[0]+gas[1]-cost[1]+...+gas[i]-cost[i]+gas[i+1]-cost[i+1] to be greater. The same reasoning gives that
 *
 *  gas[i+1]-cost[i+1]>=0
 *   gas[i+1]-cost[i+1]+gas[i+2]-cost[i+2]>=0
 *    .......
 *     gas[i+1]-cost[i+1]+gas[i+2]-cost[i+2]+...+gas[n-1]-cost[n-1]>=0
 *     What about for the partial sums that wraps around?
 *
 *     gas[0]-cost[0]+gas[1]-cost[1]+...+gas[j]-cost[j] + gas[i+1]-cost[i+1]+...+gas[n-1]-cost[n-1]
 *     >=
 *     gas[0]-cost[0]+gas[1]-cost[1]+...+gas[i]-cost[i] + gas[i+1]-cost[i+1]+...+gas[n-1]-cost[n-1]
 *     >=0
 *     The last inequality is due to the assumption that the entire sum of gas[k]-cost[k] is greater than or equal to 0. So we have that all the partial sums
 *
 *     gas[i+1]-cost[i+1]>=0,
 *     gas[i+1]-cost[i+1]+gas[i+2]-cost[i+2]>=0,
 *     gas[i+1]-cost[i+1]+gas[i+2]-cost[i+2]+...+gas[n-1]-cost[n-1]>=0,
 *     ...
 *     gas[i+1]-cost[i+1]+...+gas[n-1]-cost[n-1] + gas[0]-cost[0]+gas[1]-cost[1]+...+gas[j]-cost[j]>=0,
 *     ...
 *     Thus i+1 is the position to start. Coding using this reasoning is as follows:
 *
 *     class Solution {
 *     public:
 *         int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
 *                 int n=gas.size();
*                  int total(0),subsum(INT_MAX),start(0);
 *                 for(int i=0;i<n;++i){
 *                    total+=gas[i]-cost[i];
 *                    if(total<subsum) {
 *                        subsum=total;
 *                        start=i+1;
 *                    }
 *                    }
 *                 return (total<0) ? -1: (start%n);
 *           }
 *         };
 *           proof solution cpp c
 *            asked Mar 12 in Gas Station by XBOX360555 (2,390 points)
 *            Answer  comment
 *            Did you consider when there are multiple, same, "min" value of total?
                  commented 4 days ago by xing2
 *             edited 4 days ago by xing2
 *             reply
 *             It does not matter, suppose there are multiple minimum values of the partial sum, for example given the gas[i] - cost[i] sequence:
 *
 *             0, 1, -1, 2, -2, 3, -3, 0
 *             the partial sum sequence is
 *
 *             0, 1, 0, 2, 0, 3, 0, 0
 *             As you can see that the partial sum sequence has multiple minimum values of 0, corresponding to index i = 0, 2, 4, 6, 7, so the start position can be start = i + 1 = 1, 3, 5, 7, 0. My algorithm just picks the first one i = 0, start = 1 to return.
 */
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        //vector<int> remain(n,0);
        int total=0,minSum=INT_MAX,idx=0;
        for(int i=0;i<n;++i){
            total+=(gas[i]-cost[i]);
            if(total<minSum){
                 minSum=total;
                 idx=i+1;
            }
        }

        return (total<0)?-1:idx%n;
    }
};
