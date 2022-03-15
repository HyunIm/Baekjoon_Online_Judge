T = int(input())

for _ in range(T):
    hp, mp, attack, defense, eq_hp, eq_mp, eq_atk, eq_def = map(int, input().split())
    
    hp = hp + eq_hp
    hp = hp if hp > 1 else 1
    mp = mp + eq_mp
    mp = mp if mp > 1 else 1
    attack = attack + eq_atk
    attack = attack if attack > 0 else 0
    defense = defense + eq_def

    ability = 1*hp + 5*mp + 2*attack + 2*defense
    print(ability)
