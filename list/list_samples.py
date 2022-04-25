monthly_distance_list = [
    4000,
    11000,
    14000,
    16000,
    21000
]

print('\nSample 1: list(配列)の要素に順番にアクセスする方法')
for distance in monthly_distance_list:
    print(distance)


print('\nSample 2: list(配列)の要素に番号を指定してアクセスする方法')
print(monthly_distance_list[0])
print(monthly_distance_list[1])
print(monthly_distance_list[2])


print('Sample 3: ループを使いながら、前の要素にアクセスする方法')
for i in range(len(monthly_distance_list)):
    # i は 0 から開始される
    if i == 0:
        # i == 0 のときはスキップする（前がないため）
        continue
    print('---------------------------')
    print('先月：', monthly_distance_list[i - 1])
    print('今月：', monthly_distance_list[i])    
