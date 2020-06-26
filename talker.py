#!/usr/bin/python3
# -*- coding:UTF-8 -*-

# 上面两行一定不能少
import rospy  # ros在python语言中的头文件
from std_msgs.msg import String  # 消息头文件

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)  # 发布消息到话题 chatter 中,队列长度10

    rospy.init_node('talker', anonymous=True)  # 初始化节点名字为talker,加入一个随机数使得节点名称唯一

    rate = rospy.Rate(10)  # 10hz  设置发布频率

    while not rospy.is_shutdown():  # 当没有异常关闭时候执行如下程序(防止ctrl+c 终止程序)
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)  # 写入log日志
        pub.publish(hello_str)  # 发布字符串

        rate.sleep()  # 配合发布频率的休眠

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
