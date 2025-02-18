#询问用户输入选择编码或解码，分支处理，定义主循环，可以通过特定输入回到主循环，
#编码部分：同上一段代码
#解码部分：分支：二进制或bytes，同时必须输入解码模式进行填充，输出解码后文本。先还原bytes，然后decode
import difflib
import ast
#判断条件
codin=['1','11','111','编码','编','前一个','前面的','字符串','字符','字','前面那个','11111','前','encode']
decodin=['2','22','222','2222','bytes','二进制','解码','解','后者','后面那个','二','decode','22222','222222']
goodbyemsg=['exit','退出','bye','拜拜','我要退出','byebye','goodbye','不用了','不了','no','nono','nonono','返回','quit','end','stop','cancel','back','return','主菜单','mainmenu','走了','再见']
rechoosemsg=['main','我要重新选','编码','解码']
OKmsg=['好','ok','转','OK','行','嗯嗯','嗯','摸摸头','摸摸','虎摸','对','yes','YES']
maincircle=True #主循环
while maincircle:
#定义处理函数，现在是编码部分
    def encodeprocess():        
        encodincircle=True
        def trygbormain(codintype):
            if codintype.lower() in goodbyemsg:
                return 'break'
            elif codintype.lower() in rechoosemsg:
                return 'break'
            else:
                return 'keep'
        while encodincircle:
            codintype=input('喵ヾ(=`ω´=)ノ，要用什么类型呢？猫猫的大尾巴魔法可以编码utf8/16/32/gbk/gb2312/shiftjis哦~：')#先不加别的，不然太多了，这里加一个退出逻辑                
            gbormainva=trygbormain(codintype)
            if gbormainva=='break':
                break
            else:
                standard=['utf-8','utf-16','utf-32','ascii','gbk','gb2312','shift_jis']
                corrcodintype=difflib.get_close_matches(codintype.lower(),standard,n=1,cutoff=0.6)#注意这里返回的是一个列表
                if len(corrcodintype)<1:
                    print('哇...猫猫的格式对比失败了呢...要么是difflib的问题，要么就是拼写不正确？')
                else:
                    bytelist=[]
                    corrusecodin=corrcodintype[0]
                    trycodinmsg=input(f'好的！喵喵知道了！已经用毛茸茸的大尾巴切换到{codintype}啦！请输入要编码的字符哦：')
                    typecodinmsg=trycodinmsg.encode(encoding=corrusecodin,errors="strict")
                    bytelist.append(typecodinmsg)
                    print(bytelist)
                    secondcommand=input('要不要转成二进制呢？是的话请给喵喵一个摸摸头~喵呜！：')
                    second=trygbormain(secondcommand)
                    if second=='break':
                        break
                    else:
                        binlist=[]
                        for every in typecodinmsg:                            
                            bindata=bin(every)[2:].zfill(8)
                            binlist.append(bindata)
                        print(' '.join(binlist))
#解码部分小函数，先在外部定义
    
    def ifbinary(decodinmsg): #decodinmsg用户输入文本的变量名
        return all(every in '01 ' for every in decodinmsg) #every是forin里面设置的变量,true/true/遍历 all和in都会检查然后返回布尔值
    def num(bin8list):#看一下list里每个长度是不是8，是的话true不是false
        return all(len(bin8)==8 for bin8 in bin8list)


#定义解码函数,流程：先询问编码类型，用户可能的需求有：二进制转bytes，二进制转文字/bytes转文字，自动检测输入的是bytes还是二进制，二进制的话给出相应的bytes和文字结果，bytes直接decode给出文字，再询问要不要换成二进制（嵌一个小处理函数进去
    def decodeprocess():
        decodincircle=True
        def decgbormain(decodintype):
            if decodintype.lower() in goodbyemsg:
                return 'break'
            elif decodintype.lower() in rechoosemsg:
                return 'break'
            else:
                return 'keep'
        while decodincircle:#解码循环正式开始
            decodintype=input('好的喵！ฅ●ω●ฅ 等等...编码标准是什么嘞？喵喵的毛茸茸星光魔法支持utf8/16/32（听说差不多涵盖所有人类语言？），以及gbk/gb2312（中文，五千年的中华传承！）以及shiftjis（日语，樱花，富士山哦！）：')
            decogbormainco=decgbormain(decodintype)#检测退出，开始分支，返回的是字符
            if decogbormainco=='break':
                decodincircle=False
                break
            else:
                
                standard2=['utf-8','utf-16','utf-32','gbk','gb2312','shift_jis']
                corrdecodintype=difflib.get_close_matches(decodintype.lower(),standard2,n=1,cutoff=0.6) #此处检测用户输入进入二进制/bytes分支，二进制进入转bytes而后尝试用decode解码，如果不是只包含0和1则进入bytes流程，解码成功返回中文，失败给出提示信息（回到解码最开始？
                if len(corrdecodintype)<1:
                    print("哇...猫猫的格式对比失败了喵(ฅ'ω'ฅ)要么是你在调戏本喵，要么就是拼写不正确？")
                    print("先贴贴喵！d(=^･ω･^=)b然后我们再来重新输入试一试喵！")
                    decodincircle=False
                    break
                else:
                    decodinmsg=input('喵~=( ^>w< ^)=快把文本投喂给本喵~，本喵只吃没有0b前缀，8位一组的二进制编码和不带b''格式的bytes文件喵~：')#这里先不用检查退出，应该不用？加一个吧还是
                    decoinmsgexit=decgbormain(decodinmsg)
                    if decoinmsgexit=='break':
                        decodincircle=False
                        break
                    else:
                        if ifbinary(decodinmsg):    #为true进入二进制处理流程，先转bytes一起输出，检测是不是只包含01和空格
                            bin8list=decodinmsg.split() #每八位一组以空格为分隔提取成list，把bin8list里面每一个八位二进制转换为整数再处理成byte，不加错误处理了，处理不了就报错吧
                            if8=num(bin8list)
                            if if8:#如果每个二进制字符串都是8位的话，进入二进制处理流程
                                #把bin8list里面每一个八位二进制转换为整数再处理成byte，不加错误处理了，处理不了就报错吧
                                bytebinary=bytes(int(n,2)for n in bin8list) #int()，切片操作格式：str[start:stop:step] range生成一个可迭代对象，格式：range[start,stop(不包括),step]，每八位一组变成bytes
                                print(bytebinary)#打印二进制的bytes
                                civiltext=bytebinary.decode(encoding=corrdecodintype[0],errors="strict")#把bytes按照给定的corrdecointype解码，这里返回的是直接字符串，所以可以直接打印，匹配失败加个break
                                print(civiltext)#我有个问题，这里跑起来啥情况？直接返回函数开头了，好
                            else:#不是8位的话，进入提示退出流程
                                print("(^˵◕ω◕˵^)二进制编码不是八位一组喵，一定是剪贴板的问题？再让猫猫试一次吧！")
                        else:#非二进制字符串处理流程,先按bytes处理，输入不是二进制的话可能是bytes或者十六进制或者随便啥脸滚键盘，二进制上面已经进入分支，bytes或者16进制
                             #在try部分已经处理过，那么只剩下三种可能：给的既不是bytes也不是十六进制，/随机脸滚键盘内容/trypart内部报错，分支处理。
                            try:
                                if isinstance(decodinmsg,str):
                                    try:
                                        tranbytestry=bytes.fromhex(decodinmsg) #最容易出错的地方，重点检查，此处是检查如果输入的是str（比如十六进制而不是bytes，尝试用fromhex变成bytes
                                    except ValueError:
                                        tranbytestry=ast.literal_eval(f'b"{decodinmsg}"')
                                else:#如果不是str而是bytes
                                    tranbytestry=decodinmsg #decodingmsg可能是bytes，十六进制，随机文本，try中允许bytes和十六进制通过，其余都会进入except，其他进制是不是没考虑？
                                decodedbyte=tranbytestry.decode(encoding=corrdecodintype[0],errors="strict")
                                print(decodedbyte)
                                ifneedmsg=input("喵喵咪~已经把bytes用闪亮魔法变成文本啦！要不要把这些bytes变成二进制，来玩1和0的魔法呢？：")
                                ifneedcorr=difflib.get_close_matches(ifneedmsg.lower(),OKmsg,n=1,cutoff=0.6)#模糊匹配输入意图,不在okmsg里就退回主菜单，直接退出需要两次操作，不过也在容忍范围内
                                if len(ifneedcorr)<1:
                                    print("喵呜~知道啦~")
                                    decodincircle=False
                                    break
                                else:
                                    secondbinarylist=[]
                                    for every1 in tranbytestry:                                            
                                        secondbinary=bin(every1)[2:].zfill(8)
                                        secondbinarylist.append(secondbinary)
                                    print(' '.join(secondbinarylist))
                            except Exception as e:
                                joking=input('喵咪！好像没办法被解析呢ฅ•ω•ฅ，是不是输入的不是bytes呀？')
                                jokingcorr=difflib.get_close_matches(joking.lower(),OKmsg,n=1,cutoff=0.6)
                                if len(jokingcorr)>0:
                                    print("原来是在逗猫猫玩啊...ฅ(•ㅅ•❀)ฅ")
                                    print("o( =•ω•= )m 人，你真可爱！")
                                    print("(･ω･)つ⊂(･ω･)贴贴~")   #꒰´ᗜ`꒱꒰´ᗜ`꒱ 这个也挺可爱的，保留备用一下
                                else:
                                    print('喵咪！尾巴被缠住啦！')
                                    print(e)
                                    print('总之...先试试重启大法！')
                                    decodincircle=False
                                    break                            
                            #为false进入bytes处理流程，这里有两个分支1.解析，2.解析失败-直接break还是内部循环？



#01110010 01100101 01100100 01100001 01101110 01100100 01100111 01101111 01101100 01100100这个是测试文本，是‘redandgold’的utf8二进制，是写的时候在听的一首歌，youndrisingsons的歌，真的挺好听的。


#方便阅读所以分割一下吧，下面是主流程：
    



#流程开始，询问用户意愿/是否需要模糊匹配？
    chooseone=input('喵~是要投喂字符串来编码，还是投喂bytes二进制来解码呢？编码扣1解码扣2~')
#定义一个对比第一步输入的函数，根据匹配结果返回特定值，方便后续分支处理
    def chooseoneprocess(chooseone):
        choosemsg=difflib.get_close_matches(chooseone.lower(),codin,n=1,cutoff=0.6)
        if len(choosemsg)>0:
            return 'encodin'
        else:
            choosemsg=difflib.get_close_matches(chooseone.lower(),decodin,n=1,cutoff=0.6)
            if len(choosemsg)>0:
                return 'decodin'
            else:
                choosemsg=difflib.get_close_matches(chooseone.lower(),goodbyemsg,n=1,cutoff=0.6)
                if len(choosemsg)>0:
                    return 'exit'
                else:
                    choosemsg=difflib.get_close_matches(chooseone.lower(),rechoosemsg,n=1,cutoff=0.6)
                    if len(choosemsg)>0:
                        return 'main'
                    else:
                        return 'randommsg'

    chooseoneprores=chooseoneprocess(chooseone) #获取第一个结果分支的值
#进入第一个编码分支，接下来还有解码分支，乱码和退出分支，记得每一个小分支里要加一行支持退出的代码，就是=gbmsg直接break
#随便了反正先写就行了，进入不同分支，这个分支先进行编码处理
    if chooseoneprores=='encodin':
        encodeprocess()    
    elif chooseoneprores=='decodin':
        decodeprocess()
    elif chooseoneprores=='exit':
        print('再见哇！喵喵期待着和你一起玩！ฅ( ̳• ◡ • ̳)ฅ')
        maincircle=False
        break
    elif chooseoneprores=='main':
        print('明明已经在主菜单啦！哈基人，你这家伙...o( =•ω•= )m是不是在调戏本猫哇')
    else:
        input('喵喵咪！咦？既不编码也不解码的话....猫猫来和你贴贴吧！')
        input('ฅ(^◕ᴥ◕^)ฅ喵咪！贴贴~蹭一下！')
        print('嘿嘿！好开心呀~o( =∩ω∩= )m')
        
#备忘：1.对于非二进制当作bytes处理，bytes处理不了被except捕获进入后续流程，因为用户本来就可能输入一些脸滚键盘的东西 2.报错就报错吧，早就跟用户说明了要输入八位一组二进制的
#跑一下测试：
#    utf8编解码  测试文本‘果冻橙’，文本→二进制√  二进制→文本√ bytes→文本二进制√
#    utf16      测试文本‘牦牛奶片’ 文本→二进制√ 二进制→文本√ bytes→文本二进制√
#    utf32      测试文本‘海藻糖’   文本→二进制√ 二进制→文本√ bytes→文本二进制√
#    随机方法随机脸滚键盘内容    1.选错解码方法 gbk编码‘白桃’，二进制解码选shiftjis 得出ｰﾗﾌﾒ （不同bytes序列在不同编码标准里指向不同内容，这没办法
#                              2.脸滚键盘 解码方法gbk ‘阿斯哦海大0qgfuoeqoiasclasncaohsdlansc？？@%￥……Ukcaspas’ 脸滚键盘内容，提示非bytes，进入和猫猫玩流程
#    gbk        测试文本‘红烧茄子和烩面’    文本→二进制√  二进制→文本√  bytes→文本二进制√
#    gb2312     测试文本‘汤圆汤圆汤圆这是一个柿子汤圆’      文本→二进制√  二进制→文本√  bytes→文本二进制√
#    shiftjis   测试文本‘今夜は月が綺麗ですね’   文本→二进制√    二进制→文本√     bytes→文本二进制√
