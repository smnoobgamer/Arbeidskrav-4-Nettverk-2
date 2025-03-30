import serial
import sys
import time

#This loop sets up the port connection for Windows or Linux
while True:
    osnr=int(input("\nWindows=1 Linux=2: "))
    if osnr==1:
        os="COM"
        break
    elif osnr==2:
        os="/dev/ttyS"
        break
    else:
        print("Invalid OS try again")

#Sets the value of what port i being used
comport=input("\nCOM port number: ")

#Connection to the port
console = serial.Serial(
            port=os+comport,
            baudrate=9600,
            parity="N",
            stopbits=1,
            bytesize=8,
            timeout=8
        )
print(console.name)
if not console.isOpen():
    sys.exit()

#Loop that decides if it is a router or switch being set up 
while True:
    device = int(input("\nRouter=1 Switch=2: "))
    #Router set up
    if device==1:
        
        #This secion contains all the inputs and makes the commands that use inputs
        
        #Inputs hostname and makes the command that changes the hostname
        hostname=input("\nHostname: ")
        hostname="hostname " + hostname + "\r\n"

        #Inputs the device password and username and makes commands using it
        username=input("\nDevice username: ")
        password=input("\nDevice password: ")
        sshlogin="username " + username +" privilege 15 secret " + password +"\r\n"
        localpassword="enable secret "+ password +"\r\n"

        #Inputs the port that is being set up and makes commands that needs it
        port=input("\nOutside port: ")
        port1="int "+ port +"\r\n"

        #Innputs vlan number and creates commands using it and the port number
        Rvlan=input("\nwhat Vlan ID are you using: ")
        intRvlan="int " + port + "." + Rvlan +"\r\n"
        enqvlan="encapsulation dot1Q " + Rvlan + "\r\n"

        #Inputs the ipadress and subnettmask and makes the command using it
        ip1=input("\nIP and Mask: ")
        ip1="ip address "+ip1+"\r\n"


        
        #Starts the setup by rejecting the startup config
        console.write("\r\n".encode())
        console.write("no\r\n".encode())
        console.write("yes\r\n".encode())
        time.sleep(20)

        #Goes into Configuration terminal
        console.write("\r\n".encode())
        console.write("enable\r\n".encode())
        console.write("conf t\r\n".encode())

        #SSH Setup
        console.write(hostname.encode())
        console.write("ip domain name mylocal.local\r\n".encode())
        console.write("crypto key generate rsa modulus 2048\r\n".encode())
        time.sleep(5)
        console.write(sshlogin.encode())
        console.write("ip ssh version 2\r\n".encode())
        console.write("line vty 0 15\r\n".encode())
        console.write("transport input ssh\r\n".encode())
        console.write("login local\r\n".encode())
        console.write("exit\r\n".encode())
        console.write(localpassword.encode())

        #Port setup
        console.write(port1.encode())
        console.write("no shut\r\n".encode())
        console.write("exit\r\n".encode())
        console.write(intRvlan.encode())
        console.write(enqvlan.encode())
        console.write(ip1.encode())

        #End
        console.write("end\r\n".encode())
        console.write("write memory\r\n".encode())
        console.write("exit\r\n".encode())
        print("Done")
        break

    #Switch set up
    elif device==2:
        
        #This secion contains all the inputs and makes the commands that use inputs

        #Inputs hostname and makes the command that changes the hostname
        hostname=input("\nHostname: ")
        hostname="hostname " + hostname + "\r\n"

        #Inputs the device password and username and makes commands using it
        username=input("\nDevice username: ")
        password=input("\nDevice password: ")
        sshlogin="username " + username +" privilege 15 secret " + password +"\r\n"
        localpassword="enable secret "+ password +"\r\n"

        #Inputs the vlan id and name and makes commands using these inputs
        vlanID=input("\nMGMT Vlan ID: ")
        vlan="vlan "+vlanID +"\r\n"
        vlanName=input("\nVlan name: ")
        vlanName="name " + vlanName + "\r\n"
        intvlan="int vlan "+ vlanID +"\r\n"

        #Inputs the ipadress and subnettmask and makes the command using it
        ip1=input("\nIP and Mask: ")
        ip1="ip address "+ip1+"\r\n"

        #Inputs the default gateway and makes commnds using it
        gateway=input("\nMGMT Nettwork Gateway: ")
        gateway="ip default-gateway " + gateway +"\r\n"

        #Inputs the port name format (Excludes the last number) and trunks all ports
        portname=input("\nwhat is the name of the ports(exclude last number): ")
        trunk="int range " + portname + "1-24\r\n"
        
        #This loop is for setting up a acces port
        while True:
            access=int(input("\nDo you need a access port?(1=Yes 2=No): "))
            if access==1:
                #If the need one it asks what port i should be and changes it to a access port using the Portname format and vlan id from earlier
                accessportnr=input("\nWhat port number for access: ")
                accessport="int " + portname + accessportnr + "\r\n"
                swportmode="switchport mode access\r\n"
                swportaccess="switchport access vlan " + vlanID + "\r\n"
                break
            elif access==2:
                #If no turn the commands values to just spamming enter
                accessport="\r\n"
                swportmode="\r\n"
                swportaccess="\r\n"
                break
            else:
                print("Invalid input")


        #Starts the setup by rejecting the startup config
        console.write("\r\n".encode())
        console.write("no\r\n".encode())
        console.write("yes\r\n".encode())
        time.sleep(20)

        #Goes into Configuration terminal
        console.write("\r\n".encode())
        console.write("enable\r\n".encode())
        console.write("conf t\r\n".encode())

        #SSH Setup
        console.write(hostname.encode())
        console.write("ip domain name mylocal.local\r\n".encode())
        console.write("crypto key generate rsa modulus 2048\r\n".encode())
        time.sleep(5)
        console.write(sshlogin.encode())
        console.write("ip ssh version 2\r\n".encode())
        console.write("line vty 0 15\r\n".encode())
        console.write("transport input ssh\r\n".encode())
        console.write("login local\r\n".encode())
        console.write("exit\r\n".encode())
        console.write(localpassword.encode())

        #Vlan setup and IP configuration
        console.write(vlan.encode())
        console.write(vlanName.encode())
        console.write("exit\r\n".encode())
        console.write(intvlan.encode())
        console.write("no shut\r\n".encode())
        console.write(ip1.encode())
        console.write("exit\r\n".encode())
        console.write(gateway.encode())

        #Port setup
        console.write(trunk.encode())
        console.write("switchport mode trunk\r\n".encode())
        console.write(accessport.encode())
        console.write(swportmode.encode())
        console.write(swportaccess.encode())

        #End
        console.write("end\r\n".encode())
        console.write("write memory\r\n".encode())
        console.write("exit\r\n".encode())
        print("Done")
        break
    else:
        print("Invalid device Try again")