# import keyboard
import time
import rospy
from std_msgs.msg import Float64

def command_publisher(command_string):
    mv_list = command_formatting(command_string)
    # print(mv_list)
    topics=["/rover_one/left_rocker_to_servo_mount_1_joint_position_controller/command",
            "/rover_one/left_bogie_to_servo_mount_2_joint_position_controller/command",
            "/rover_one/left_bogie_to_servo_mount_3_joint_position_controller/command",
            "/rover_one/right_rocker_to_servo_mount_4_joint_position_controller/command",
            "/rover_one/right_bogie_to_servo_mount_5_joint_position_controller/command",
            "/rover_one/right_bogie_to_servo_mount_6_joint_position_controller/command",
            "/rover_one/servo_mount_1_to_wheel_1_joint_velocity_controller/command",
            "/rover_one/servo_mount_2_to_wheel_2_joint_velocity_controller/command",
            "/rover_one/servo_mount_3_to_wheel_3_joint_velocity_controller/command",
            "/rover_one/servo_mount_4_to_wheel_4_joint_velocity_controller/command",
            "/rover_one/servo_mount_5_to_wheel_5_joint_velocity_controller/command",
            "/rover_one/servo_mount_6_to_wheel_6_joint_velocity_controller/command"]
    pub = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topics]
    rospy.init_node('command_sender', anonymous=True)
    for i in range(len(pub)):
        if i<=5:
            pub[i].publish(mv_list[i])
        elif i>5 and i<=8:
            pub[i].publish(mv_list[i])
        else:
            pub[i].publish(mv_list[i])

def command_formatting(command_string):
    motor_values = [0 for _ in range(6)]
    servo_values = [0 for _ in range(6)]
    
    if command_string[3]=="1" and command_string[2]!="1":
        servo_values[0]=-3.14159*(21.0/180)
        servo_values[2]=3.14159*(20.4/180)
        servo_values[3]=-3.14159*(43.9/180)
        servo_values[5]=3.14159*(46.4/180)

    elif command_string[2]=="1" and command_string[3]!="1":
        servo_values[0]=3.14159*(43.9/180)
        servo_values[2]=-3.14159*(46.4/180)
        servo_values[3]=3.14159*(21.0/180)
        servo_values[5]=-3.14159*(20.4/180)

    elif command_string[2]=="1" and command_string[3]=="1":
        servo_values[0]=-3.14159*(51.8/180)
        servo_values[2]=3.14159*(48.9/180)
        servo_values[3]=3.14159*(51.8/180)
        servo_values[5]=-3.14159*(48.9/180)        
    
    if command_string[0]=="1" or command_string[1]=="1":
        if command_string[0]=="1":
            motor_values = [x-1.0 for x in motor_values]
            if command_string[3]=="1" and command_string[2]=="1":
                for x in range(3,6):
                    motor_values[x]=1.0
        if command_string[1]=="1":
            motor_values = [x+1.0 for x in motor_values]
            if command_string[3]=="1" and command_string[2]=="1":
                for x in range(3,6):
                    motor_values[x]=-1.0
        # print('mv', motor_values)
        if command_string[3]=="1" and command_string[2]!="1":
            motor_values[3]*=(300)/200
            motor_values[5]*=(300)/200
            motor_values[0]*=(600)/200
            motor_values[1]*=(550)/200
            motor_values[2]*=(600)/200

        if command_string[2]=="1" and command_string[3]!="1":
            motor_values[0]*=(300)/200
            motor_values[2]*=(300)/200
            motor_values[3]*=(600)/200
            motor_values[4]*=(550)/200
            motor_values[5]*=(600)/200

        if command_string[2]=="1" and command_string[3]=="1":
            motor_values[0]*=(270)/180
            motor_values[2]*=(270)/180
            motor_values[3]*=(270)/180
            motor_values[5]*=(270)/180

    print(motor_values)
    return servo_values+motor_values

while True:
    f = open("thisFile.txt", "r")
    commands = f.readlines()
    i = len(commands)
    # print(i)
    if i>=1:
        # commands_formatted = [list([int(i[0]),int(i[1]),int(i[2]),int(i[3])]) for i in commands]
        for i in commands:
            # print(i)
            command_publisher(i)
        f.close()
        f = open("thisFile.txt", "w")
    else:
        pass
    f.close()

print("***END***")



