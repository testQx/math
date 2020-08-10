#name,age,hometown
#用一个数据来表示一个班级所有学生的信息
#以数组or字典去存储，不同存储时，时间复杂度如何
#数据结构是一种封装后的一种高级数据结构，封装了基本数据类型：int,string,float

#
a=[
("zhangsan",24,"beijing"),
("zhangsan",24,"beijing"),
("zhangsan",24,"beijing")
 ]
# for i in a:
#     if a[0][0]=="zhangsan":
#         pass
#O(n)
#
b=[
{
    "name":"zhangsan",
    "age":24,
    "hometown":"beijing"
},{

    }
 ]

#
c={
    "zhansan":{
        "age":24,
        "hometown":"beijing"
    },
}
#c["zhangsan"]
#O(1)


#程序=数据结构+算法
#总结：算法是为了解决实际问题而设计的，数据结构是算法需求处理的问题载体


#class Stuent():
# def adds()  def pop() def sort() def modify
# 抽象数据类型（Abstract Data Type）：数据结构 + 对应数据结构支持的方法