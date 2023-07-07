from pathlib import Path
from rosbags.highlevel import AnyReader
import numpy as np

topic='/aft_mapped_to_init'
filename='/home/paulo/catkin_ws/bagfiles/volta_grande/lego_loam_data__2023-06-23-13-38-35_0.bag'


# create reader instance and open for reading
with AnyReader([Path(filename)]) as reader:
      #Adquirir Dados
     i=0
     connections = [x for x in reader.connections if x.topic == topic]

     NUM_ODOM=connections[0].msgcount
     plot_matrix=np.zeros([NUM_ODOM,3])
     time_group=np.zeros([NUM_ODOM,2])
     dif_time =np.zeros([NUM_ODOM-1,1])

     print("Bag lego_loam \n")
     print("Tópico Registado = ", topic)
     print("Número de Mensagens do Tópico = ", NUM_ODOM)
     
     print("\n \n Início de Aquisição de dados")


     for connection, timestamp, rawdata in reader.messages(connections=connections):
         msg = reader.deserialize(rawdata, connection.msgtype)

         x=msg.pose.pose.position.x
         y=msg.pose.pose.position.y
         z=msg.pose.pose.position.z
         time=msg.header.stamp.sec
         nanotime=msg.header.stamp.nanosec

         #Inserir dados em uma array
         plot_data = np.array([z,x,y], dtype='f')
         
         plot_matrix[i]=np.matrix(plot_data)
         
         plot_time = np.array([time , nanotime])

         time_group[i] = np.matrix(plot_time)

         i+=1
     time_total = time_group[i-1] - time_group[0]
# Confirmar adquisição de dados

print(plot_matrix)
print("Tempo total dos dados = ", time_total ," seg")
print("                  Concluído Aquisição de Dados da Bagfile  LeGO-LOAM                   ")



# make data
x_data_odom_lego = plot_matrix[:,0] 
y_data_odom_lego = plot_matrix[:,1]
z_data_odom_lego = plot_matrix[:,2]
time_group_sec = time_group[:,0]
time_group_ns  = time_group[:,1]

time_init= time_group_sec[0]
for j in range(NUM_ODOM-1):
       time_calculate = ((time_group_sec[j+1]-time_group_sec[j])* 1000000000 + time_group_ns[j+1])-time_group_ns[j]
       dif_time[j] = time_calculate / 1000000000
       time_group_sec[j]= time_group_sec[j] - time_init
time_group_sec[j+1]= time_group_sec[j+1] - time_init

periodo_pub = (np.sum(dif_time) / (NUM_ODOM-1))  #seg
frequencia_pub = 1 / periodo_pub

time_total = time_group_sec[i-1] - time_group_sec[0]

print("Tempo total dos dados = ", time_total ," seg")
print("                  Finish bagfile lego_loam                \n\n    ")