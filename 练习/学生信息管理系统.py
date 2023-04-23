import os.path
import sys
import time
faill = 'student.txt'
Faill = 'Stt.txt' #保存登陆用户名和密码
def zhuche():   # 注册
    print('======如以注册则直接登陆，否则请先注册，注册后可直接登录！！！！！！')
    student__list = []
    #还没检查用户名是否相同
    用户名 = input('请输入用户名(12位数字): ')
    密码 = input('请输入密码:')
    if len(用户名) == 12:
        if os.path.exists(Faill):
            with open(Faill,'r',encoding='utf-8')as FFaill:
                检查 = FFaill.readlines()
                if 检查 :
                    for i in 检查:
                        zidian = dict(eval(i))
                        if zidian['用户名'] == 用户名 and zidian['密码'] == 密码:
                            print('用户已经存在!登陆成功！')
                            break
                        elif zidian['用户名'] == 用户名 and zidian['密码'] != 密码:
                            print('密码错误！！！')
                            sys.exit()
                        else:
                            if zidian['用户名'] != 用户名 :
                               Student = {'用户名': 用户名, '密码': 密码}
                               student__list.append(Student)
                               save2(student__list)
                               print('注册成功！')
                               break
                else:
                    Student = {'用户名': 用户名, '密码': 密码}
                    student__list.append(Student)
                    save2(student__list)
                    print('注册成功！')
    else:
        print('用户名错误！注册失败')
        sys.exit()
def save2(lstt):
    try:
        stu__txt = open(Faill,'a',encoding='utf-8')
    except:
        stu__txt = open(Faill,'w',encoding='utf-8')
    for i in lstt:
         stu__txt.write(str(i)+'\n')
    stu__txt.close()
def main():   #主函数
    while True:
        menu()
        choice=eval(input('请选择相应的操作：'))
        if choice in [1,2,3,4,5,6,7,8,9,10,11,0]:
          if choice==0:
             anwers = input('你确定要退出系统吗？退出请输入yes（yes或者no）')
             if anwers == 'yes':
               print('正在退出系统·····')
               time.sleep(5)
               print('=========已退出学生管理系统========')
               sys.exit()
             else:
                main()
          if choice == 1:
              insert()
          if choice == 2:
              search()
          if choice==3:
              delete()
          if choice==4:
             modify()
          if choice==5:
              sort()
          if choice==6:
             total()
          if choice==7:
              show()
          if choice == 8:
              sort2()
          if choice == 9:
              show账号和密码()  ## 查 询 所 有 学 生 密 码
          if choice == 10:  # 显示男生 或者 女生 信息
              show_man_men()
          if choice == 11:
              show_name()
        else:
            print('输入错误！！！！！！是否继续？？？继续请按数字1，其他则会退出整个系统。')
            继续 = eval(input('请选择：'))
            if 继续 == 1:
                main()
            else:
                sys.exit()
def menu():
    s1 = '欢迎进入学生管理系统'.center(30,'=')
    print(s1)
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.对学生成绩排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示全部学生信息')
    print('\t\t\t\t8.对学生信息按学号大小排序')
    print('\t\t\t\t9.查询所有学生账号和密码')
    print('\t\t\t\t10.显示男生(或者女生)信息')
    print('\t\t\t\t11.显示所有学生的名字')
    print('\t\t\t\t0.退出学生管理系统···')
    print('====================================')
def insert(): #  录 入 系 统
    sums = 0
    student_list=[] # 空列表
    while True:
        try:
            学号 = input('请输入学号：')
            if len(学号) != 12:
                sys.exit()
            姓名 = input('请输入姓名：')
            性别 = input('请输入性别：')
            计算机网络 = int(input('请输入计算机网络成绩：'))
            if 计算机网络 > 100:
                sys.exit()
            组成原理 = int(input('请输入组成原理成绩：'))
            if 组成原理 > 100:
                sys.exit()
            英语 = int(input('请输入英语成绩：'))
            if 英语 > 100:
                sys.exit()
        except:
            print('输入无效，请重新输入：')
            continue
        student = {'学号':学号,'姓名':姓名,'性别':性别,'计算机网络':计算机网络,'组成原理':组成原理,'英语':英语}
        student_list.append(student)
        sums += 1
        print(f'本次操作第{sums}个学生信息录入成功。')
        是否添加 = input('是否继续添加学生信息？（按n退出整个程序）')
        if 是否添加 != 'n':
            continue
        elif 是否添加 == 'n' :
            print('学生管理系统已退出!')
            break
       #  将信息保存到磁盘文件当中
    save(student_list)
    show()
    sys.exit()
def save(lst):
    try:
        stu_txt = open(faill,'a',encoding='utf-8')
    except:
        stu_txt = open(faill,'w',encoding='utf-8')
    for i in lst:
         stu_txt.write(str(i)+'\n')
    stu_txt.close()
def search():
    student_ss=[]
    while True:
        ###判断磁盘文件是否存在
     Id=''
     xingming=''
     if os.path.exists(faill):
        chazhao = eval(input('根据学号查询请选择1，根据姓名查询请选择2：'))
        if chazhao == 1:
           Id = input('请输入要查询的学生的学号：')
        elif chazhao == 2:
            xingming = input('请输入要查找的学生的姓名：')
        else:
            print('输入有误，请重新输入:')
            search()
        ###打开文件
        with open(faill,'r',encoding='utf-8')as rfile:
            ##读取它并把它放到一个变量中
            studentt = rfile.readlines()
            for iu in studentt:###将字符串转化为字典类型
                zidian = dict(eval(iu))
                if Id:
                  if zidian['学号'] == Id:
                    student_ss.append(zidian)
                elif xingming:
                  if zidian['姓名']==xingming:
                    student_ss.append(zidian)
     ##显示查询结果
        show_student(student_ss)
     ##防止第二次查询时列表有数据，所以先清空列表
        student_ss.clear()
        anwerr=input('请问要继续查询吗？（需要则y,其他则会结束）\n')
        if anwerr == 'y':
            continue
        else:
            print('查询结束，正在退出系统。。。。')
            time.sleep(4)
            print('-----已成功退出!------')
            sys.exit()
     else:
         print('该学生信息还未录入!')
         print('还继续其他操作吗？（按q退出）')
         want2 = input('请选择：')
         if want2 != 'q':
             main()
         else:
             sys.exit()
def show_name(): # B   显示所有学生的名字
        student_name = []
        while True:
            ###判断磁盘文件是否存在
            if os.path.exists(faill):
                    with open(faill, 'r', encoding='utf-8') as rfile:
                        ##读取它并把它放到一个变量中
                        studentt = rfile.readlines()
                        for iu in studentt:  ###将字符串转化为字典类型
                            zidian = dict(eval(iu))
                            student_name.append(zidian['姓名'])
                    ##显示查询结果
                    # print('所有学生名字如下：：：：')
                    后台显示所有学生名字(student_name)  #显示查询结果
                    ##防止第二次查询时列表有数据，所以先清空列表
                    student_name.clear()
                    print('还继续其他操作吗？（按q退出）')
                    want2 = input('请选择：')
                    if want2 == 'q':
                        sys.exit()
                    else:
                        main()
def 后台显示所有学生名字(ff):
    if len(ff) == 0:
        print('暂未查到，可能还没有注册!!!')
        return
    format__tile = '{}\t'
    print(format__tile.format('所有学生姓名如下: '))
    ##内容格式
    format__data = '{}\t'
    for i in ff:
        print(format__data.format(i))
def show_student(lst):##显示查询结果
    if len(lst)==0:
        print('未查到该学生信息!!!')
        return
    ##标题格式
    format_tile='{:^10}{:^10}{:^2}{:^9}{:^4}{:^6}{:^6}'
    print(format_tile.format('学号','姓名','性别','计算机网络','组成原理','英语','总成绩'))
    ##内容格式
    format_data = '{:^8}{:^9}{:^4}{:^4}{:^16}{:^1}{:^11}'
    for item in lst:
        print(format_data.format(item.get('学号'),item.get('姓名'),item.get('性别'),item.get('计算机网络'),
                                 item.get('组成原理'),
                                 item.get('英语'),
        int(item.get('英语'))+int(item.get('计算机网络')) +int(item.get('组成原理'))))
def show_man_men():
        student_man = []
        while True:
            ###判断磁盘文件是否存在
            if os.path.exists(faill):
                want = input('请输入性别（男\\女）: ')
                if want == "男":###打开文件
                    性别 = True
                    with open(faill, 'r', encoding='utf-8') as rfile:
                        ##读取它并把它放到一个变量中
                        studentt = rfile.readlines()
                        for iu in studentt:  ###将字符串转化为字典类型
                            zidian = dict(eval(iu))
                            if 性别:
                                if zidian['性别'] == '男':
                                    student_man.append(zidian)
                            else:
                                pass
                    ##显示查询结果
                    show_student(student_man)
                    ##防止第二次查询时列表有数据，所以先清空列表
                    student_man.clear()
                    print('还继续其他操作吗？（按q退出）')
                    want2 = input('请选择：')
                    if want2 == 'q':
                        sys.exit()
                    else:
                        main()
                elif want == '女':
                    性别 = False
                    with open(faill, 'r', encoding='utf-8') as rfile:
                        ##读取它并把它放到一个变量中
                        studentt = rfile.readlines()
                        for iu in studentt:  ###将字符串转化为字典类型
                            zidian = dict(eval(iu))
                            if 性别 == False:
                                if zidian['性别'] == '女':
                                    student_man.append(zidian)
                            else:
                                pass
                    ##显示查询结果
                    show_student(student_man)
                    ##防止第二次查询时列表有数据，所以先清空列表
                    student_man.clear()
                    print('还继续其他操作吗？（按q退出）')
                    want2 = input('请选择：')
                    if want2 == 'q':
                        sys.exit()
                    else:
                        main()
                else:
                    print('输入有误!')
                    show_man_men()
def delete():#(删除操作)
   while True:
     ids = input('请输入要删除的学生信息（其学号）：')
     if len(ids) != 12:
         print('------学号错误！！！')
         sys.exit()
     if ids :
        if os.path.exists(faill):
            with open(faill,'r',encoding='utf-8') as file:
                d = file.readlines()
        else:
            d = []
        flag = False#标记是否删除
        if d:
            with open(faill,'w',encoding='utf-8')as wfile:
                dt = {}
                for i in d:
                    dt = dict(eval(i))#将字符串转换为字典
                    if dt['学号'] != ids:
                        wfile.write(str(dt)+'\n')
                    else:
                        flag=True
                if flag:
                    print('学生信息已经删除！')
                else:
                    print(f'没有找到学号为{ids}的学生信息！')
        else:
            print('系统为空，暂未录入学生信息！')
            break
        answeer=input('是否继续删除?y\n')
        if answeer == 'y':
           continue
        else:
          print('还继续其他操作吗？（按n终止整个程序）')
          want1 = input('请选择：')
          if want1 != 'n':
              main()
          elif want1 == 'n':
             sys.exit()
def modify():#(修改操作)
    show()
    listttt = []
    if os.path.exists(faill):
        with open(faill,'r',encoding='utf-8')as rfile:
            listttt=rfile.readlines()
    else:
        return
    a = input('请输入要修改的学生学号：')
    if len(a) != 12:
        print('------学号错误！！！程序终止 ')
        sys.exit()
    with open(faill, 'w', encoding='utf-8') as wfile:
        for i in listttt:
            b = dict(eval(i))
            if b['学号'] == a:
                print('-----已经找到该学生-----')
                while True:
                    try:
                        b['姓名'] = input('请输入修改的值：(姓名)')
                        b['性别'] = input('请输入修改的性别：')
                        b['计算机网络'] = int(input('请输入修改的值：(计算机网络)'))
                        if b['计算机网络'] > 100:
                            sys.exit()
                        b['组成原理'] = int(input('请输入修改的值：(组成原理)'))
                        if b['组成原理'] > 100:
                            sys.exit()
                        b['英语'] = int(input('请输入修改的值：(英语)'))
                        if b['英语'] > 100:
                            sys.exit()
                    except:
                        print('你输入有误，请重新输入: ')
                    else:
                        break
                wfile.write(str(b) + '\n')
                print('修改成功！！！')
            else:
                wfile.write(str(b) + '\n')
        anwerrr = input('是否继续修改？（按y继续，其余退出。）')
        if anwerrr == 'y':
            modify()
        else:
            sys.exit()  #终止整个程序
def sort2():#按照学号大小排序,( 从小到大 )
    lise_学号=[]
    if os.path.exists(faill):
        with open(faill,'r',encoding='utf-8')as rfiel:
            listtt=rfiel.readlines()
            for i in listtt:
                lise_学号.append(dict(eval(i)))
    else:
        print('暂未保存任何学生信息！')
        return
    lise_学号.sort(key=lambda lise_学号: int(lise_学号['学号']), reverse = False )
    show_student(lise_学号)
def sort():#成绩排序
    lise=[]
    if os.path.exists(faill):
        with open(faill,'r',encoding='utf-8')as rfiel:
            listt=rfiel.readlines()
            for i in listt:
                lise.append(dict(eval(i)))
    else:
        print('暂未保存任何学生信息！')
        return
    anwers=eval(input('请选择排序方式：（1为升序，2为降序）'))
    if anwers==1:
      fangshii = False
    elif anwers==2:
      fangshii = True
    else:
      print('输入错误！请重新输入：')
      sort()
    print('1:按计算机网络方式排序\n2:按组成原理方式排序\n3：按英语方式排序\n4:按总成绩排序')
    paixu=eval(input('请选择按什么科目排序：'))
    if paixu==1:
      lise.sort(key=lambda lise:int(lise['计算机网络']),reverse=fangshii)
    elif paixu==2:
      lise.sort(key=lambda lise:int(lise['组成原理']),reverse=fangshii)
    elif paixu==3:
       lise.sort(key=lambda lise:int(lise['英语']),reverse=fangshii)
    elif paixu==4:
        lise.sort(key=lambda lise:int(lise['计算机网络'])+int(lise['组成原理'])+int(lise['英语'])
                  ,reverse=fangshii)
    else:
       print('输入有误，请重新输入：')
       sort()
    show_student(lise)
def total():
    while True:
        if os.path.exists(faill):
            with open(faill,'r',encoding='utf-8')as rfiel:
                list = rfiel.readlines()
                if list:
                  numbers = len(list)
                  print('学生总人数为: ')
                  print(numbers)
                  print('还继续其他操作吗？（按q终止整个程序）')
                  want = input('请选择：')
                  if want != 'q':
                      main()
                  elif want == 'q':
                      sys.exit()
                else:
                    print('学生总人数为 0 ，提示：还没有录入学生信息!')
                    print('还继续其他操作吗？（按q终止整个程序）')
                    want = input('请选择：')
                    if want != 'q':
                        break
                    else:
                        sys.exit()
        else:
            print('暂未保存数据信息!')
            print('还继续其他操作吗？（按q终止整个程序）')
            want = input('请选择：')
            if want != 'q':
                break
            else:
                sys.exit()
def 后台显示账号和密码(liae):
    if len(liae)==0:
        print('暂未查到，可能还没有注册!!!')
        return
    format_tile = '{}\t\t\t\t{}'
    print(format_tile.format('用户名', '密码'))
    ##内容格式
    format_data = '{}\t\t{}'
    for item in liae:
        print(format_data.format(item.get('用户名'), item.get('密码')))
def show账号和密码():
    list_user_mima = []
    if os.path.exists(Faill):
        with open(Faill,'r',encoding='utf-8') as rFaill:
            listtt = rFaill.readlines()
        for ii in listtt:
            list_user_mima.append(eval(ii))
        if list_user_mima:
            print('所有学生账号密码如下: ')
            后台显示账号和密码(list_user_mima)
        else:
            print('暂未查到，可能还没有注册！！！！！')
def show(): # 显示所有学生信息
        list2=[]
        if os.path.exists(faill):
            with open(faill,'r',encoding='utf-8')as rfiel:
                listr=rfiel.readlines()
            for i in listr:
                list2.append(eval(i))
            if list2:
                show_student(list2)
            else:
              print('暂未保存学生信息！\n')
              print('还继续其他操作吗？（按q退出）')
              want2 = input('请选择：')
              if want2 != 'q':
                main()
              else:
                sys.exit()
if __name__ == '__main__':
    zhuche()
    main()