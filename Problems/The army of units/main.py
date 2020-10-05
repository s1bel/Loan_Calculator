units = int(input())

if units >= 1000:
    print('legion')
elif units >= 500:
    print('swarm')
elif units >= 50:
    print('horde')
elif units >= 10:
    print('pack')
elif units >= 1:
    print('few')
else:
    print('no army')
