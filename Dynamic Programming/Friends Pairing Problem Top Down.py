def pairing(N,memory):
    if N == 0 or N == 1 or N == 2:
        return N

    if memory[N] != -1:
        return memory[N]

    memory[N] = pairing(N-1,memory) + (N-1) * pairing(N-2,memory)

    return memory[N]

def pairFriends(N):
    memory = [-1] * (N+1)
    return pairing(N,memory)

print(pairFriends(4))