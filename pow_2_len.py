def pow_2_len(power, display=False):
    length = 0
    all_pow_len = dict()
    for p in range(1,power):
        pwr = 2**p
        power_len = len(str(pwr))
        
        if power_len > length:
            length = power_len
            if display: print(f'\n{length}: ', end = '')
        
        all_pow_len.setdefault(length,0)
        all_pow_len[length] = 1
        
        if display: print(p,end=' ')
    return all_pow_len
