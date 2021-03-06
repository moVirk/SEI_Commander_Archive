#!/usr/bin/env python3

import socket, errno, sys, struct, subprocess, re
import threading
from athena_messages import Waypoint, Principal_Athena_Message, Artemis_Message, Artemis_General_Order, Mars_General_Order, Mars_Message, Scan_Point, Athena_Orders, Nike_Message

import numpy as np
import argparse
import asyncio
from asyncio import DatagramProtocol
from datetime import datetime

class AthenaReceiver(object):

    def __init__(self):
        #self.athena_ip = "127.0.0.1"
        #self.athena_ip = "192.168.1.21"
        self.athena_ip = "192.168.1.8"
        self.athena_port = 3636
        messageToSend = ""
        self.set_up_connections()
        print("in init")

    def set_up_connections(self):
        try:
            """
            Socket for Receiving Protobuff to Athena.
            """
            print("1")
            self.athena_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print("4")
            self.athena_socket.bind((self.athena_ip, self.athena_port));
            print("receiving from ",self.athena_ip, self.athena_port)
            self.athena_socket.settimeout(20.0);
            print("receiver set_up_connections socket set up")
        except:
            print('receiver set_up_connections error')

    def receive(self):
        #for socket_instance in self.send_sockets:
        print("IN receive")
        try:
            print("1")
            if self.athena_socket != None:
                print("1a")
                data = self.athena_socket.recv(1024)        
                print("2")
                principal_message = Principal_Athena_Message()
                print("3")
                principal_message.ParseFromString(data)
                print(principal_message)
            else:
                print('No receiving socket')
        except:
            print('receive error')



class AthenaSender(object):

    def __init__(self):
        #self.athena_ip = "127.0.0.1"
        self.athena_ip = "192.168.1.21"
        #self.athena_ip = "192.168.1.8"
        self.athena_port = 3636
        messageToSend = ""
        self.set_up_connections()
        print("in init")

    def set_up_connections(self):
        try:
            """
            Socket for Sending Protobuff to Athena.
            """
            print("1")
            self.athena_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print("2")
            #self.send_sockets.append([self.athena_socket, self.athena_ip, self.athena_port, "athena"])
            print("Send protobuf to Athena socket set up")
        except:
                print('protobuff socket send error')

    def send(self):
        #for socket_instance in self.send_sockets:
        print("IN send")
        try:
            self.athena_socket.connect((self.athena_ip, self.athena_port));
            print("sending to ",self.athena_ip, self.athena_port)
            # Send data to server
            data = self.messageToSend;
            self.athena_socket.send(data);
        except:
            print('set_up_connections error')



def build_message():
    header_message = Principal_Athena_Message()
    header_message.sender_uuid = "SEI 21351"
    header_message.message_type = "Command"
    header_message.destination_id.append('0')
    time = datetime.utcnow()
    str_time = time.isoformat()
    header_message.timestamp_utc_time = str_time

    order = Athena_Orders()
    order.weapon_control_order = int(control_order) 
    order.behavior = 2
    header_message.athena_orders.append(order);


    # Artemis message

    arti_message = Artemis_Message()
    arti_message.uuid = "practice_artemi_145"
    #status only fields
    '''
    arti_message.ptu_pan = 0
    arti_message.ptu_tilt = 0
    arti_message.latitude = 39.119551
    arti_message.longitude = -87.363750
    arti_message.altitude = 0
    arti_message.heading = 0
    arti_message.zoom = 0
    arti_message.ammo_count = 100000
    '''

    # Message command to Artemis
    current_general_order = Artemis_General_Order()
    current_general_order.trigger = "general"
    current_general_order.weapon_control_order = int(control_order)
    current_general_order.behavior = 2
    current_general_order.select_scan_pattern = 1
    #current_general_order.left_aor = 1
    #current_general_order.right_aor = 1
    current_general_order.continuing_order = "general"

    # ScanPoints
    scanPoint1 = Scan_Point()
    scanPoint1.point_number  = 1
    scanPoint1.pan = float(angle)
    scanPoint1.zoom = 0
    scanPoint1.tilt = 0
    current_general_order.create_scan_pattern.append(scanPoint1)

    # ActionPoints
    '''
    action1 = 1
    current_general_order.action_point.append(action1)
    action2 = 2
    current_general_order.action_point.append(action2)
    action3 = 3
    current_general_order.action_point.append(action3)
    '''
    
    arti_message.orders.append(current_general_order)

    header_message.artemis.append(arti_message)

    # mars message
    '''
    mars_message = Mars_Message()
    mars_message.uuid = "kairos"

   
    mars_order = Mars_General_Order()
    mars_order.trigger = "general"
    mars_order.behavior = 1
    mars_order.driving_control_order = 1
    
    waypoint = Waypoint()
    waypoint.point_number = 1
    waypoint.latitude = 34.2413508
    waypoint.longitude = -116.0747637
    waypoint.heading = 90
    mars_order.waypoints.extend([waypoint])
    
    waypoint = Waypoint()
    waypoint.point_number = 2
    waypoint.latitude = 34.2414074
    waypoint.longitude = -116.0748388
    waypoint.heading = 194
    mars_order.waypoints.extend([waypoint])
    
    waypoint = Waypoint()
    waypoint.point_number = 3
    waypoint.latitude = 34.2414340
    waypoint.longitude = -116.0749233
    waypoint.heading = 7
    mars_order.waypoints.extend([waypoint])    
    
    waypoint = Waypoint()
    waypoint.point_number = 4
    waypoint.latitude = 34.2413952
    waypoint.longitude = -116.0749112
    waypoint.heading = 194
    mars_order.waypoints.extend([waypoint])
    
    waypoint = Waypoint()
    waypoint.point_number = 5
    waypoint.latitude = 34.2413686
    waypoint.longitude = -116.0748817
    waypoint.heading = 7
    mars_order.waypoints.extend([waypoint])
    
    waypoint.point_number = 6
    waypoint.latitude = 34.2413508
    waypoint.longitude = -116.0747637
    waypoint.heading = 90
    mars_order.waypoints.extend([waypoint])
    mars_message.orders.append(mars_order)
    header_message.mars.append(mars_message)
    '''
    '''
    # Nike Message example

    nike_message = Nike_Message()
    nike_message.uuid = "nike3"
    nike_message.latitude = 39.119649
    nike_message.longitude = -87.363789
    nike_message.altitude = 32
    header_message.nike.append(nike_message)
    '''
   
    print(header_message)
    return header_message.SerializeToString()


async def main():
    global control_order
    global angle

    while True:
        """
        print("Receiving message")
        node = AthenaReceiver()
        node.receive()
        """

        control_order = input("Please enter weapon control order (1 or 3): ")
        print ("control order is: " + control_order)
        angle = input("Please enter pan angle: ")
        print ("pan angle is: " + angle)

        print("Sending message")
        msg = build_message()
        print(msg)
        node = AthenaSender()
        node.messageToSend = msg
        node.send()

if __name__ == '__main__':
    asyncio.run(main())
