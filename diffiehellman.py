import math

def is_primitive_root (g, p):
    phi = p - 1

    factors = set()
    n = phi
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)

            while n % i == 0:
                n //= i
        
        i += 1

    if n > 1:
        factors.add(n)
    
    for q in factors:
        if pow(g, phi // q, p) == 1:
            return False
    
    return True

def find_primitive_root (p):
    for g in range(2, p):
        if is_primitive_root (g, p):
            return g

def compute_public_key(X, g, p):
    return pow(g, X, p)

def compute_shared_key(Y, X, p):
    return pow(Y, X, p)

def userA_computes_key (Yb, Xa, q):
    result = pow(Yb, Xa, q)
    return result

def userB_computes_key (Ya, Xb, q):
    result = pow(Ya, Xb, q)
    return result

if __name__ == "__main__":
    q = int(input("ENTER PRIME NUMBER: "))

    Xa = int(input("USER A: ENTER PRIVATE INTEGER: "))
    Xb = int(input("USER B: ENTER PRIVATE INTEGER: "))

    if Xa > q or Xb > q:
        print(f"The Private Integer should be less than {q}.")
        exit()

    p = find_primitive_root (q)
    print(f"\nPrimitive Root: {p}")
    
    Ya = compute_public_key (Xa, p, q)
    Yb = compute_public_key (Xb, p, q)

    print("\nPrivate Key:")
    print(f"User A => Ya: {Ya}")
    print(f"User B => Yb: {Yb}")

    Ka = userA_computes_key (Yb, Xa, q)
    Kb = userB_computes_key (Ya, Xb, q)

    print(f"\nShared Key: ")
    print(f"User A: {Ka}")
    print(f"User B: {Kb}")