'''
打印一个Unicode的字符串"hello world"
'''


str1 = u"hello world"

print(str1,type(str1))


'''
python3默认编码为unicode，由str类型进行表示。二进制数据使用byte类型表示
字符串通过编码转换成字节码，字节码通过解码成为字符串
encode：str –> bytes
decode：bytes – > str
'''