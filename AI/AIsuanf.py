# -*- coding: cp936 -*-
import sys
from request import *
from tupip import *
board=[]#��¼ǰһ������״̬
arr='0'
step =0
op=[]
ans=[]
an=[]
# start = [3, 4, 0, 6, 1, 9, 8, 7,5]
# end = [1,0,3,4,5,6,7,8,9]
# cache = [start]
# cache2 = [end]
#��ȡ������
def get_reverse(a):
    # ��һά���е����������˴����Խ����Ż�
    ans = 0

    for i in range(len(a)):
        if a[i] != 0:
            for j in range(i + 1, len(a)):
                if a[j] != 0:
                    if a[i] > a[j]:
                        ans ^= 1
    return ans
def getPos(m):#��ȡ0����ɫͼƬ��λ��
    for i in range(len(m)):
        if m[i] == 0:
            return i
def result(state, cache, l, r):
    for i in range(l, r):
        if state == cache[i]:
            return i
    return -1
def operation(x):#�жϲ���
    if x==-1:
        return 'a'
    if x==1:
        return 'd'
    if x==-3:
        return 'w'
    if x==3:
        return 's'
    if x==0:
        return '0'#��ʼ��־
def print_after(cache, far, num):  # print ����
    if num == -1:
        return
    global board
    global arr
    global step
    print_after(cache, far, far[num])
    #print(cache[num])
    x=getPos(cache[num])
    y=getPos(board)
    z=x-y
    print(z)
    board=cache[num]
    print(board)
    #an[step - 1] = z
    an.append(z)
    # cache.pop(num)
    #
    # num=num-1
    if step>=1:
        op.append(operation(z))

    if step ==1:
        arr = operation(z)
    elif step > 1:
        arr = str(arr) + operation(z)

    step += 1
def printf_before(cache2, far2, num):  # print ǰ��
    if num == -1:
        return
    global board
    global arr,an
    global step
    #print(cache2[num])
    x = getPos(cache2[num])
    y = getPos(board)
    z=x-y
    an.append(z)
    #an[step-1]=z
    print(x-y)
    board = cache2[num]
    print(board)
    if step>=1:
        op.append(operation(z))
    # x = getPos(cache2[num])
    # y = getPos(cache2[num+1])
    # print(x-y-3)
    # cache2.pop(num)
    # num=num-1
    if step == 1:
        arr = operation(z)
    elif step > 1:
        arr = str(arr) + operation(z)
    step += 1
    printf_before(cache2, far2, far2[num])
def do_with(cache, cache2, far, l, r, l2, r2):#��������
    flag = 0
    t = cache[l]
    # �õ�0���ڵ�������x��y
    pos = getPos(t)
    x, y = divmod(pos, 3)
    # �ĸ�����������״̬
    newpos = []
    if y < 2:
        newpos.append(pos + 1)
       # print('��')
    if y > 0:
        newpos.append(pos - 1)
       # print('��')
    if x < 2:
        newpos.append(pos + 3)
        #print('��')
    if x > 0:
        newpos.append(pos - 3)
        #print('��')
    for ipos in newpos:
        tt = cache[l][:]
        tt[ipos] = cache[l][pos]
        tt[pos] = cache[l][ipos]
        # �����״̬û��cache�оͼ���cache������β��r+1
        if tt not in cache:
            cache.append(tt)
            far.append(l)
            r += 1
            # �����״̬�������cache2���ҵ�����ô��״̬���ǽӿ�״̬
            # �ҵ��ӿ�״̬�Ϳ���ֱ�Ӵ�ӡ�ˣ����ؽӿ�״̬���±�res����ֵ��flag
            res = result(tt, cache2, l2, r2)
            if res != -1:
                flag = res
    l += 1
    #print(after)
   # print(cache2)
    return cache, cache2, far, l, r, l2, r2, flag
def do_with_print(before, after):
    print_after(cache, far, before)
    printf_before(cache2, far2, far2[after])# ������ﲻ��far2[flag]����flag���ظ������м�Ľӿ�״̬
    #print(after)
    #print(cache2)
    print(step - 1) # ��ȥһ��ʼ��״̬�����㲽��
    print(arr)
    print(op)
    print(an)
    headers = {'content-type': "application/json"}
    anserurl = "http://47.102.118.1:8089/api/challenge/submit"
    answer = {
        "uuid": uuid,
        "teamid": 41,
        "token": "38f216cd-c9fb-47ac-8075-c37f650c6892",
        "answer": {
            "operations":arr,
            "swap": swap
        }
    }
    print(answer)
    response = requests.request("post", anserurl, headers=headers, json=answer)
    print(response.text)
    print("�ɹ�")
    sys.exit(0)
def restore():
    global l, l2, r, r2,cache,cache2,far,far2
    while (l != r) and (l2 != r2):  # BFS��left == right��ʾ����Ϊ��
        flag = -1  # �����м�ӿ�״̬���±�
        cache, cache2, far, l, r, l2, r2, flag = do_with(cache, cache2, far, l, r, l2, r2)
        if flag:
            do_with_print(r - 1, flag)
        cache2, cache, far2, l2, r2, l, r, flag = do_with(cache2, cache, far2, l2, r2, l, r)
        if flag:
            do_with_print(flag, r - 1)
if __name__=="__main__":
    global end,start,l,l2,r,r2,cache,cache2,far,far2
    board,end=pipeitu()
    start=board
    print(board)
    print(end)
    l = l2 = 0
    r = r2 = 1
    far = [-1]
    far2 = [-1]
    cache = [start]
    cache2 = [end]
    restore()





