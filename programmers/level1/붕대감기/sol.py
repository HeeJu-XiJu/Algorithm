def solution(bandage, health, attacks):
    now = health
    time = 0 # 연속시간
    before = 0 
    for second in range(1, attacks[-1][0]+1):
        # 몬스터 공격할 시 체력회복 못하므로 before 저장
        before = now
        # 시간에 따른 체력회복
        time += 1
        if time != bandage[0] :
            if now != health:
                now += bandage[1]
            if now >= health:
                now = health
        else :
            time = 0
            if now != health:
                now += bandage[1] + bandage[2]
                
            if now >= health:
                now = health

        for attack in attacks:
            if attack[0] == second:
                now = before - attack[1]
                time = 0
        
        if now <= 0:
            return -1
    return now


print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))


# 다른 풀이
def solution(bandage, health, attacks):
    hp = health
    start = 1
    for i, j in attacks:
        hp += ((i - start) // bandage[0]) * bandage[2] + (i - start) * bandage[1]
        start = i + 1
        if hp >= health:
            hp = health
        hp -= j
        if hp <= 0:
            return -1
    return hp


# while
def solution(bandage, health, attacks):
    
    attack_time = {}
    for attack in attacks:
        attack_time[attack[0]] = attack[1]


    time, combo = 0, 0
    maximum = health
    while time != attacks[-1][0]: 
        time += 1
        combo += 1

        # attacked
        if time in attack_time.keys():
            combo = 0
            health -= attack_time[time]
            if health <= 0:
                return - 1
        # heal
        else:
            health += bandage[1]
            if combo == bandage[0]:
                health += bandage[2]
                combo = 0
            if health > maximum:
                health = maximum
        
    return health