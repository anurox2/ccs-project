from scapy.all import *
import logging

attack_log = {
    "incoming_1":0,
    "incoming_2":0,
    "outgoing_1":0,
    "outgoing_2":0,
}

def pkt_callback(pkt):
    len_of_packet = len(pkt.sprintf("%Raw.load%"))
    if(len_of_packet > 2):
        if(len_of_packet == 807):
            print("\n\nAttacker detected. Packet size is more than 2 on port 9000. -------" + str(len_of_packet))
            if(attack_log["incoming_1"] == 0):
                print("\n\tHeartbleed Attack on vulnerable server. Packet 1 length is logged.")
                attack_log["incoming_1"] = len_of_packet
            elif((attack_log["incoming_2"] == 0) & (attack_log["incoming_1"] == 807)):
                print("\n\tHeartbleed Attack on vulnerable server. Packet 2 length is logged.")
                attack_log["incoming_2"] = len_of_packet
        elif(len_of_packet == 65584):
            print("\n\nAttacker detected. Packet size is more than 2 on port 9000. -------" + str(len_of_packet))
            if(attack_log["outgoing_1"] == 0):
                print("\n\tPacket 1 length is logged. Returning packet")
                attack_log["outgoing_1"] = len_of_packet
            elif((attack_log["outgoing_2"] == 0) & (attack_log["outgoing_1"] == 65584)):
                print("\n\tPacket 2 length is logged. Returning packet")
                attack_log["outgoing_2"] = len_of_packet


sniff(iface="lo", prn=pkt_callback, filter="dst port 9000")
print("\n\n\n")
print(attack_log)





####### OLD CODE BACKUP ########
## 101 ##
        # elif(len_of_packet == 65584):
        #     print("Attacker detected. Packet size is more than 2 on port 9000.")
        #     if(attack_log["outgoing_1"] == 0):
        #         print("Attack on vulnerable server. Packet 1 length is logged.")
        #         attack_log["outgoing_1"] = len_of_packet
        #     elif((attack_log["outgoing_2"] == 0) & (attack_log["outgoing_1"] == 65584)):
        #         print("Attack on vulnerable server. Packet 2 length is logged.")
        #         attack_log["outgoing_2"] = len_of_packet