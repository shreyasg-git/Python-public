testnum = int(input())
main_list = []
for i in range(testnum):
    data = input()
    data = data.split()
    main_list.append([int(data[0]), int(data[1])])

for i in range(len(main_list)):
    N = main_list[i][0]
    K = main_list[i][1]
    beaker1 = 1  # Infinite capacity
    beaker2 = 0  # capacity == N
    amoeba_cnt = 0
    day_cnt = 1
    while amoeba_cnt < K:

        if beaker1*2 < N:
    #        print('still empty')
            beaker1 *= 2
            day_cnt += 1
        elif beaker1*2 > N:
    #        print('Overflow')
            beaker2 += N
            beaker1 = 1
            day_cnt += 2

        elif beaker1*2 == N:
            if beaker1*2 == K:
                continue
            else:
                beaker2 += N
                beaker1 = 2
            day_cnt += 1
    #    print(amoeba_cnt, K)
        amoeba_cnt = beaker1 + beaker2
    print(day_cnt)
