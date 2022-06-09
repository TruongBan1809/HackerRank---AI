
# Cong chua bi mac ket o trong ma tran vuong. Ban dang o trung tam cua
# ma tran do. Nhiem vu cua ban la di chuyen tung buoc mot theo bat ky
# huong nao de giai cuu cong chua
# 3<N<100 : kich thuoc cua ma tran
# m : vi tri cua bot
# p : vi tri cua cong chua
# Let's start!!! 

# tim kiem vi tri(toa do) cua m va p va so sanh
def displayPathtoPrincess(n, gird):

    pos_col = {}
    pos_row = {}
    not_find = True

    for i in range(n):
        line = len(gird[i])
        for j in range(line):
            if(gird[i][j] == 'm'):
                pos_col['m'] = j
                pos_row['m'] = i
            elif(girl[i][j] == 'p'):
                pos_col['p'] = j
                pos_row['p'] = i
    # print(pos_col['m'])
    # print(pos_col['p'])

    while(not_find):
        if(pos_row['m'] < pos_row['p']):
            pos_row['m'] += 1
            print('DOWN')
        elif(pos_row['m'] > pos_row['p']):
            pos_row['m'] -= 1
            print('UP')

        if(pos_col['m'] > pos_col['p']):
            pos_col['m'] -= 1
            print('LEFT')
        elif(pos_col['m'] < pos_col['p']):
            pos_col['m'] += 1
            print('RIGHT')
        
        if( pos_col['m'] == pos_col['p'] and pos_row['m'] == pos_row['p']):
            not_find = False

if __name__ == '__main__' :
    m = int(input())
    girl = []
    for i in range(0, m):
        girl.append(input().strip())

    displayPathtoPrincess(m, girl)