# !/usr/bin/python
# -*- coding:UTF-8 -*-

# 上面两行一定不能少
import rospy
from std_msgs.msg import String


def callback(data):
    print(data)
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)  # 写入日志


def listener():
    rospy.init_node('listener', anonymous=True)  # 设置名字为listener的节点,加入随机数
    rospy.Subscriber("chatter", String, callback)  # 订阅名字为 chatter的话题

    rospy.spin()


if __name__ == '__main__':
    listener()