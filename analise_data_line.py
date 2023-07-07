from pathlib import Path
import numpy as np
from rosbags.highlevel import AnyReader
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

import a_loam_data_linha_reta as aloam_data
import kiss_icp_linha_reta as kiss_icp_data
import lego_loam_data_linha_reta as lego_loam_data

print(" \n \n Start plot    ")

plt.style.use('_mpl-gallery')

# Criação de PLOT'S
# plot X,Y odometry
plt.figure(1)
fig, xy = plt.subplots(layout='constrained')

xy.plot(aloam_data.x_data_odom_line_aloam, 
        aloam_data.y_data_odom_line_aloam, 
        linewidth=2.0, label='odometry_aloam',
        color='blue')
xy.plot(kiss_icp_data.x_data_odom_line_kiss,
        kiss_icp_data.y_data_odom_line_kiss, 
        linewidth=2.0, label='odometry_kiss',
        color='red')
xy.plot(lego_loam_data.x_data_odom_line_lego, 
        lego_loam_data.y_data_odom_line_lego, 
        linewidth=2.0, label='odometry_lego',
        color='green')

xy.set(xlim=(0, 15.5), xticks=np.arange(1, 16),
       ylim=(-0.15, 0.15), yticks=(-0.15, -0.1 , -0.05 , 0 , 0.05, 0.1 , 0.15))       
xy.set_xlabel('Distância percorrida no eixo X (m)')
xy.set_ylabel('Distância Percorrida no eixo Y (m)')     
xy.legend()  
xy.set_title("Experiência Linha Reta - Odometria Registada dos Eixos X e Y")

#plot x,Z odometry
plt.figure(2)
fig, xz = plt.subplots(layout='constrained')
xz.plot(aloam_data.x_data_odom_line_aloam, 
        aloam_data.z_data_odom_line_aloam, 
        linewidth=2.0, label='odometry_aloam',
        color='blue')
xz.plot(kiss_icp_data.x_data_odom_line_kiss, 
        kiss_icp_data.z_data_odom_line_kiss, 
        linewidth=2.0, label='odometry_kiss',
        color='red')
xz.plot(lego_loam_data.x_data_odom_line_lego, 
        lego_loam_data.z_data_odom_line_lego,
        linewidth=2.0, label='odometry_lego',
        color='green')

xz.set(xlim=(0, 15.5), xticks=np.arange(1, 16),
       ylim=(-0.15, 0.55), yticks=(-0.15, -0.1 , -0.05 , 0 , 0.05, 0.1 , 0.15, 0.2 , 0.25 ,0.3 , 0.35 , 0.4 , 0.45 , 0.5))       
xz.set_xlabel('Distância percorrida no eixo X (m)')
xz.set_ylabel('Altura detetada pelo sensor (m)')  
xz.legend()     
xz.set_title("Experiência Linha Reta - Odometria Registada dos Eixos X e Z")

#plot odometry final
plt.figure(3)
fig, of = plt.subplots(layout='constrained')
of.scatter([15] , [0] , label='point estimated', color='orange')
of.scatter(aloam_data.x_data_odom_line_aloam[(aloam_data.i)-1],
           aloam_data.y_data_odom_line_aloam[(aloam_data.i)-1],
           label='Point Final ALOAM', color='blue')
of.scatter(kiss_icp_data.x_data_odom_line_kiss[(kiss_icp_data.i)-1],
           kiss_icp_data.y_data_odom_line_kiss[(kiss_icp_data.i)-1],
           label='Point Final KISS-ICP', color='red')
of.scatter(lego_loam_data.x_data_odom_line_lego[(lego_loam_data.i)-1],
           lego_loam_data.y_data_odom_line_lego[(lego_loam_data.i)-1],
           label='Point Final LeGO', color='green')
of.set(xlim=(14.4,15.2), xticks = (14.5,15,15.1,15.2),
       ylim=(-0.2,0.2) , yticks = (-0.2,-0.1,0,0.1,0.2))
of.legend()
of.set_xlabel('Distância Total Percorrida durante o eixo dos X (em m)')
of.set_ylabel('Offset da Linha Horizontal')
of.set_title("Experiência Linha Reta - Odometria Registada do Final")


#plot x,y,Z in time
plt.figure(4)
fig, cart_time = plt.subplots(3, 1, layout='constrained')

#x to time
cart_time[0].plot(aloam_data.time_group_sec, 
        aloam_data.x_data_odom_line_aloam, 
        linewidth=2.0, label='odometry_aloam',
        color='blue')
cart_time[0].plot(kiss_icp_data.time_group_sec, 
        kiss_icp_data.x_data_odom_line_kiss, 
        linewidth=2.0, label='odometry_kiss',
        color='red')
cart_time[0].plot(lego_loam_data.time_group_sec, 
        lego_loam_data.x_data_odom_line_lego,
        linewidth=2.0, label='odometry_lego',
        color='green')

cart_time[0].set(xlim=(0, 166), xticks=np.arange(1, 166, 3),
       ylim=(-0.1, 15.5), yticks=np.arange(0,15.5))       
cart_time[0].set_xlabel('Tempo Decorrido (seg)')
cart_time[0].set_ylabel('Eixo dos X ao longo do Tempo (m)')  
cart_time[0].legend()     
cart_time[0].set_title("Experiência Linha Reta - Odometria Registada ao Longo do Tempo sobre o Eixo dos X")

#y to time
cart_time[1].plot(aloam_data.time_group_sec, 
        aloam_data.y_data_odom_line_aloam, 
        linewidth=2.0, label='odometry_aloam',
        color='blue')
cart_time[1].plot(kiss_icp_data.time_group_sec, 
        kiss_icp_data.y_data_odom_line_kiss, 
        linewidth=2.0, label='odometry_kiss',
        color='red')
cart_time[1].plot(lego_loam_data.time_group_sec, 
        lego_loam_data.y_data_odom_line_lego,
        linewidth=2.0, label='odometry_lego',
        color='green')

cart_time[1].set(xlim=(0, 166), xticks=np.arange(1, 166, 3),
       ylim=(-0.15, 0.15), yticks=(-0.15, -0.1 , -0.05, 0, 0.05, 0.1, 0.15) )       
cart_time[1].set_xlabel('Tempo Decorrido (seg)')
cart_time[1].set_ylabel('Eixo dos Y ao longo do Tempo (m)')  
cart_time[1].legend()     
cart_time[1].set_title("Experiência Linha Reta - Odometria Registada ao Longo do Tempo sobre o Eixo dos Y")

#z to time
cart_time[2].plot(aloam_data.time_group_sec, 
        aloam_data.z_data_odom_line_aloam, 
        linewidth=2.0, label='odometry_aloam',
        color='blue')
cart_time[2].plot(kiss_icp_data.time_group_sec, 
        kiss_icp_data.z_data_odom_line_kiss, 
        linewidth=2.0, label='odometry_kiss',
        color='red')
cart_time[2].plot(lego_loam_data.time_group_sec, 
        lego_loam_data.z_data_odom_line_lego,
        linewidth=2.0, label='odometry_lego',
        color='green')

cart_time[2].set(xlim=(0, 166), xticks=np.arange(1, 166, 4),
       ylim=(-0.15, 0.6), yticks=(-0.1, 0 , 0.1, 0.2 , 0.3 ,0.4 , 0.5))       
cart_time[2].set_xlabel('Tempo Decorrido (seg)')
cart_time[2].set_ylabel('Altura detetada pelo sensor (m)')  
cart_time[2].legend()     
cart_time[2].set_title("Experiência Linha Reta - Odometria Registada ao Longo do Tempo sobre o Eixo dos Z")

#plot period time

plt.figure(5)
fig, dt_al = plt.subplots(1 , 2, tight_layout=True)
dt_al[0].hist(aloam_data.dif_time, (aloam_data.NUM_ODOM-1))
dt_al[1].hist(aloam_data.dif_time, (aloam_data.NUM_ODOM-1),density=True)
dt_al[1].yaxis.set_major_formatter(PercentFormatter(xmax=(aloam_data.NUM_ODOM-1)))
dt_al[0].set_xlabel('Período de Tempo entre Tópicos (Seg)')
dt_al[1].set_xlabel('Período de Tempo entre Tópicos (Seg)')
dt_al[0].set_ylabel('Frequência Absoluta')
dt_al[1].set_ylabel('Frequência Relativa')
dt_al[0].set_title("Experiência Linha Reta - Frequência Absoluta do Período de Tempo entre Tópicos de Odometria do A-LOAM")
dt_al[1].set_title("Experiência Linha Reta - Frequência Relativa do Período de Tempo entre Tópicos de Odometria do A-LOAM")

plt.figure(6)
fig, dt_kiss = plt.subplots(1 , 2, tight_layout=True)
dt_kiss[0].hist(kiss_icp_data.dif_time, (kiss_icp_data.NUM_ODOM-1))
dt_kiss[1].hist(kiss_icp_data.dif_time, (kiss_icp_data.NUM_ODOM-1),density=True)
dt_kiss[1].yaxis.set_major_formatter(PercentFormatter(xmax=(kiss_icp_data.NUM_ODOM-1)))
dt_kiss[0].set_xlabel('Período de Tempo entre Tópicos (Seg)')
dt_kiss[1].set_xlabel('Período de Tempo entre Tópicos (Seg)')
dt_kiss[0].set_ylabel('Frequência Absoluta')
dt_kiss[1].set_ylabel('Frequência Relativa')
dt_kiss[0].set_title("Experiência Linha Reta - Frequência Absoluta do Período de Tempo entre Tópicos de Odometria do KISS-ICP")
dt_kiss[1].set_title("Experiência Linha Reta - Frequência Relativa do Período de Tempo entre Tópicos de Odometria do KISS-ICP")

plt.figure(7)
fig, dt_lego = plt.subplots(1 , 2, tight_layout=True)
dt_lego[0].hist(lego_loam_data.dif_time, (lego_loam_data.NUM_ODOM-1))
dt_lego[1].hist(lego_loam_data.dif_time, (lego_loam_data.NUM_ODOM-1),density=True)
dt_lego[1].yaxis.set_major_formatter(PercentFormatter(xmax=(lego_loam_data.NUM_ODOM-1)))
dt_lego[0].set_xlabel('Período de Tempo entre Tópicos (Seg)')
dt_lego[1].set_xlabel('Período de Tempo entre Tópicos (Seg)')
dt_lego[0].set_ylabel('Frequência Absoluta')
dt_lego[1].set_ylabel('Frequência Relativa')
dt_lego[0].set_title("Experiência Linha Reta - Frequência Absoluta do Período de Tempo entre Tópicos de Odometria do LeGO-LOAM")
dt_lego[1].set_title("Experiência Linha Reta - Frequência Relativa do Período de Tempo entre Tópicos de Odometria do LeGO-LOAM")



#print Relatorio
print("\n Relatório de Dados")


print("Coordenadas dos pontos finais: \n kiss_icp  =  X = ",
      kiss_icp_data.x_data_odom_line_kiss[(kiss_icp_data.i)-1]," Y = ",
      kiss_icp_data.y_data_odom_line_kiss[(kiss_icp_data.i)-1],
      " m \n A-LOAM    =  X = ",
      aloam_data.x_data_odom_line_aloam[(aloam_data.i)-1]," Y = ",
      aloam_data.y_data_odom_line_aloam[(aloam_data.i)-1] , 
      " m \n LeGO-LOAM =  X = ",
      lego_loam_data.x_data_odom_line_lego[(lego_loam_data.i)-1]," Y = ",
      lego_loam_data.y_data_odom_line_lego[(lego_loam_data.i)-1], " m \n")

print(" \n Duração dos dados: \n kiss_icp = ",
       kiss_icp_data.time_total,"seg\n A-LOAM = ",
       aloam_data.time_total,"seg\n LeGO-LOAM =",
       lego_loam_data.time_total," seg\n")

print("Perído Médio entre Tópicos de Odometria \n kiss_icp  = ", kiss_icp_data.periodo_pub,
       "seg \n A-LOAM    = ", aloam_data.periodo_pub ,
       "seg \n LeGO-LOAM = ", lego_loam_data.periodo_pub , "seg\n")

print("Frequência Média entre Tópicos de Odometria \n kiss_icp  = ", kiss_icp_data.frequencia_pub,
       "Hz \n A-LOAM    = ", aloam_data.frequencia_pub ,
       "Hz \n LeGO-LOAM = ", lego_loam_data.frequencia_pub , "Hz\n")

print(" \n Show PLOT's'")

plt.show()






