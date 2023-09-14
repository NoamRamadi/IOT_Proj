import socket

nb = 0  # open HiveMQ - broker.hivemq.com
brokers = [str(socket.gethostbyname('broker.hivemq.com'))]
ports = ['1883']
usernames = ['USER']  # should be modified for HIT
passwords = ['PASS']  # should be modified for HIT
broker_ip = brokers[nb]
port = ports[nb]
username = usernames[nb]
password = passwords[nb]

mzs = ['']
sub_topics = [mzs[nb] + '#']
pub_topics = [mzs[nb] + 'test']

broker_ip = brokers[nb]
broker_port = ports[nb]
username = usernames[nb]
password = passwords[nb]
sub_topic = sub_topics[nb]
pub_topic = pub_topics[nb]

conn_time = 0
comm_topic = 'pr/home/'
manag_time = 10
topic_alarm = comm_topic + "alarm"
trash_valume_THR = 500
log_file_path = "trash_log.txt"