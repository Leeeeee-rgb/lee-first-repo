def add(a, b):
    result=round((a+b)*1.1,2)
    return result

if __name__=="__main_":
    print("计算结果（含税费+四舍五入）：",add(10,20))
