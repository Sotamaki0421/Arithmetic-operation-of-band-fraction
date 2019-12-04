def gcd(x,y):#ユークリッドの互除法        
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def add(value1,value2):
    (s1,n1,a1,b1) = value1
    (s2,n2,a2,b2) = value2

    bunsi1,bunsi2,A_bunbo = tsubun(a1,b1,a2,b2)
    K_bunsi = To_kabunsu(bunsi1,bunsi2,n1,n2,s1,s2,A_bunbo)
    taibunsu,T_bunsi,T_bunbo = To_taibunsu(K_bunsi,A_bunbo)

    if T_bunsi != 0:
        y = gcd(abs(T_bunsi),T_bunbo)
        return (int(K_bunsi/abs(K_bunsi)),abs(taibunsu),abs(int(T_bunsi/y)),abs(int(T_bunbo/y)))
    else:
        return (1,abs(taibunsu),abs(T_bunsi),1)

def tsubun(a1,b1,a2,b2):
    bunbo = b1*b2
    bunsi1 = a1 * b2
    bunsi2 = a2 * b1
    return bunsi1,bunsi2,bunbo

def To_kabunsu(bunsi1,bunsi2,n1,n2,s1,s2,bunbo):
    return s1*bunsi1+s1*n1*bunbo + s2*bunsi2+s2*n2*bunbo 

def To_taibunsu(K_bunsi,A_bunbo):
    if abs(K_bunsi) > abs(A_bunbo) and abs(K_bunsi)%abs(A_bunbo) != 0:
        return int(abs(K_bunsi)/A_bunbo),int(abs(K_bunsi)%A_bunbo),A_bunbo
    if abs(K_bunsi) < abs(A_bunbo):
        return 0,K_bunsi,A_bunbo
    if abs(K_bunsi)%abs(A_bunbo) == 0:
        return int(abs(K_bunsi)/A_bunbo),0,1
    if abs(K_bunsi) == 0:
        return 0,0,1

def sub(value1,value2):
    (s1,n1,a1,b1) = value1
    (s2,n2,a2,b2) = value2

    bunsi1,bunsi2,A_bunbo = tsubun(a1,b1,a2,b2)
    K_bunsi = To_kabunsu(bunsi1,bunsi2,n1,n2,s1,-s2,A_bunbo)
    taibunsu,T_bunsi,T_bunbo = To_taibunsu(K_bunsi,A_bunbo)

    if T_bunsi != 0:
        y = gcd(abs(T_bunsi),T_bunbo)
        return (int(K_bunsi/abs(K_bunsi)),abs(taibunsu),abs(int(T_bunsi/y)),abs(int(T_bunbo/y)))
    else:
        return (1,abs(taibunsu),abs(T_bunsi),1)

def mul(value1,value2):
    (s1,n1,a1,b1) = value1
    (s2,n2,a2,b2) = value2
    taibunsu,T_bunsi,T_bunbo = To_taibunsu(s1*s2*(a1+b1*n1)*(a2+b2*n2),b1*b2)
    print(taibunsu,T_bunsi,T_bunbo)
    if T_bunsi != 0:
        y = gcd(abs(T_bunsi),T_bunbo)
        print(y)
        return (s1*s2,abs(taibunsu),abs(int(T_bunsi/y)),abs(int(T_bunbo/y)))
    else:
        return (1,abs(taibunsu),abs(T_bunsi),1)

def div(value1,value2):
    (s1,n1,a1,b1) = value1
    (s2,n2,a2,b2) = value2
    taibunsu,T_bunsi,T_bunbo = To_taibunsu(s1*s2*(a1+b1*n1)*b2,b1*(a2+b2*n2))
    if T_bunsi != 0:
        y = gcd(abs(T_bunsi),T_bunbo)
        return (s1*s2,abs(taibunsu),abs(int(T_bunsi/y)),abs(int(T_bunbo/y)))
    else:
        return (1,abs(taibunsu),abs(T_bunsi),1)
