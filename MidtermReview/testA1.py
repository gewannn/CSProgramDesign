for a in (5, 6, 7, 8):          # 百位
    for b in (5, 6, 7, 8):      # 十位
        if b == a:
            continue
        for c in (5, 6, 7, 8):  # 个位
            if c == a or c == b:
                continue
            print(a*100 + b*10 + c)