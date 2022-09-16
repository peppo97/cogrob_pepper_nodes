#!/usr/bin/python3

import rospy
from pepper_nodes.srv import WakeUp, WakeUpRequest, WakeUpResponse
from pepper_nodes.srv import Rest, RestRequest, RestResponse

class Handler:
    def __init__(self):
        self.wakeup_service = rospy.ServiceProxy("wakeup", WakeUp)
        self.rest_service = rospy.ServiceProxy("rest", Rest)

    def wakeup(self):
        msg = WakeUpRequest()
        resp = self.wakeup_service(msg)
        rospy.loginfo(resp.ack)

    def rest(self):
        msg = RestRequest()
        resp = self.rest_service(msg)
        rospy.loginfo(resp.ack)

if __name__ == "__main__":
    NODE_NAME = "table_node_example"
    SLEEP = 3.0
    rospy.init_node(NODE_NAME)
    handler = Handler()
    rospy.loginfo("I am standing up")
    handler.wakeup()
    rospy.loginfo(f"Waiting for {SLEEP} seconds")
    rospy.loginfo("I'm going to rest")
    rospy.sleep(SLEEP)
    handler.rest()
