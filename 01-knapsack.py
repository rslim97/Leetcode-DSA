import pprint

# 01 knapsack

if __name__ == '__main__':
    # # [0,1,2,3,4,5,6,7]
    # capacity=[i for i in range(7+1)]
    # # Value array
    # values=[0,50,40,70,80,10]
    # # Weight array
    # weights=[0,3,2,4,5,1]
    # assert len(weights)==len(values)
    # h,w=len(weights),len(capacity)
    # memo=[[0]*w for _ in range(h)]
    # for v in range(1,h):
    #     for c in capacity[1:]:
    #         # print(memo)
    #         if c>=weights[v]:
    #             memo[v][c]=max(memo[v-1][c-weights[v]]+values[v],
    #                            memo[v-1][c])
    #         else:
    #             memo[v][c]=memo[v-1][c]

    capacity=7
    values=[0,50,40,70,80,10]
    weights=[0,3,2,4,5,1]
    assert len(weights)==len(values)
    num_items=len(weights)
    h,w=num_items+1,capacity+1
    memo=[[0]*w for _ in range(h)]
    for i in range(1,num_items+1):
        weight=weights[i-1]
        value=values[i-1]
        for j in range(1,capacity+1):
            if j>=weight:
                memo[i][j]=max(memo[i-1][j-weight]+value,memo[i-1][j])
            else:
                memo[i][j]=memo[i-1][j]

    pprint.pprint(memo)