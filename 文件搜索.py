import os, platform, time
from os import path

windows = [f'{chr(i)}:/' for i in range(97,123)] # for windows
linux_mac = '.'
findResult = []

def print_pa(root,target,list):
    for name in list:
        if target in name: #如果找到相似的名称就打印地址
            # print(path.join(root, name))
            findResult.append(path.join(root, name))


def print_path(target,pa,ty='all'):  
    for root, dirs, files in os.walk(pa):
        if ty=='file': # 只搜索文件
            print_pa(root, target, files)
        elif ty=='dir': # 只搜索文件夹
            print_pa(root, target, dirs)
        else: # 不区分文件和文件夹
            print_pa(root, target, dirs)
            print_pa(root, target, files)


def search_file(target, ty):
    sysstr = platform.system()
    """
    search_file_for_windows

    search_file_for_linux_mac
    """
    if sysstr == 'Windows':
        for name in reversed(windows):
            print_path(target, name, ty)
    elif(sysstr == "Linux" or sysstr == 'Darwin'):
        print_path(target, linux_mac, ty)
    else:
        print ("Other System tasks don't support,Only support Windows, Linux, Mac ")


def main():
    print('-----------------文件搜索系统-------------')
    print('请输入要搜索的文件名:')
    target = input()
    print('请输入要搜索的类型(只搜索目录：dir,只搜索文件：file, 不区分文件或目录：all)')
    ty = input()
    print('--------开始搜索，请稍等------------')
    print('----------------------------------')
    print('---                            ---')
    print('---           正               ---')
    print('---           在               ---')
    print('---           搜               ---')
    print('---           搜               ---')
    print('---                            ---')
    print('----------------------------------')
    start_time = time.time() # 开始时间
    search_file(target, ty) # 搜索过程
    end_time = time.time() # 结束时间
    run_time = end_time - start_time # 计算用时
    print('--------搜索完毕，请查看findResult文件查看搜索结果------------')
    #### 保存搜索结果
    targetFile = path.join(path.dirname(__file__), 'findResult.txt')
    fo = open(targetFile, 'w')
    fo.write(f'------------搜索:{target}，类型:{ty}，总共用时：{run_time}秒--------------\n')
    if len(findResult) == 0:
        fo.write(f'------------未找到{target}，类型:{ty}--------------\n')
    for find in findResult:
        fo.write(f'{find}\n')
    
    fo.close()
    ### 保存搜索结果
    print('-----------any keys to end-----------')
    input()

if __name__ == '__main__':
    main()

