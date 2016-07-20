import paramiko
import time
import getpass
import sys
import os
import subprocess
import re


# function to backup the configs
def bacukp_ns_confg(ip,USERNAME,PASSWORD,buffer_size,waittime,bash_var_exit):

    try:
        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()
        # Automatically add untrusted hosts (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # initiate SSH connection
        remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        print "SSH connection established to %s" % ip+"\n"
        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established\n"

    except paramiko.AuthenticationException:
        print "\nAuthentication Failed\n"
        sys.exit(bash_var_exit)
    except paramiko.SSHException:
        print "\nIssues with SSH service\n"
        sys.exit(bash_var_exit)
    except socket.error,e:
        print "\nConnection Error\n"
        sys.exit(bash_var_exit)

    # Strip the initial router prompt
    output = remote_conn.recv(buffer_size)
    # See what we have
    print output
    # Now let's try to send the NS a command

    remote_conn.send("shell\n")
    remote_conn.send("tar czf "+ip+"-mpx_bacukp.tar.gz /nsconfig\n")
    remote_conn.send("exit\n")
    remote_conn.send("exit\n")
    # Wait for the command to complete
    time.sleep(waittime)

    output = remote_conn.recv(buffer_size)

    # See what we have
    print output

    remote_conn.close()

# function to upload the imageto device
def upload_scp(myfile,destination):

    Result = subprocess.check_output("md5 "+ myfile ,stderr=None,shell=True)
    print "Result - "+ Result
    subprocess.call("sshpass -p '"+PASSWORD+"' scp "+myfile+" "+USERNAME+"@"+ip+":"+destination , shell=True)
    return True

# function to send the configs to device
def create_folder_on_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,version,bash_var_exit):

    try:
        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()
        # Automatically add untrusted hosts (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # initiate SSH connection
        remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        print "SSH connection established to %s" % ip+"\n"
        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established\n"

    except paramiko.AuthenticationException:
        print "\nAuthentication Failed\n"
        sys.exit(bash_var_exit)
    except paramiko.SSHException:
        print "\nIssues with SSH service\n"
        sys.exit(bash_var_exit)
    except socket.error,e:
        print "\nConnection Error\n"
        sys.exit(bash_var_exit)

    # Strip the initial router prompt
    output = remote_conn.recv(buffer_size)
    # See what we have
    print output
    # Now let's try to send the NS a command

    remote_conn.send("shell\n")
    remote_conn.send("cd /var/nsinstall/\n")
    remote_conn.send("mkdir build-folder-"+version+"\n")
    remote_conn.send("exit\n")
    remote_conn.send("exit\n")
    # Wait for the command to complete
    time.sleep(waittime)

    output = remote_conn.recv(buffer_size)

    # See what we have
    print output

    remote_conn.close()

# function to send the configs to device
def disable_ecmp_on_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,vlan_id,bash_var_exit):

    try:
        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()
        # Automatically add untrusted hosts (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # initiate SSH connection
        remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        print "SSH connection established to %s" % ip+"\n"
        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established\n"

    except paramiko.AuthenticationException:
        print "\nAuthentication Failed\n"
        sys.exit(bash_var_exit)
    except paramiko.SSHException:
        print "\nIssues with SSH service\n"
        sys.exit(bash_var_exit)
    except socket.error,e:
        print "\nConnection Error\n"
        sys.exit(bash_var_exit)

    # Strip the initial router prompt
    output = remote_conn.recv(buffer_size)
    # See what we have
    print output
    # Now let's try to send the NS a command

    remote_conn.send("vtysh\n")
    remote_conn.send("conf t\n")
    remote_conn.send("router ospf\n")
    remote_conn.send("passive-interface vlan"+vlan_id+"\n")
    remote_conn.send("end\n")
    remote_conn.send("wr\n")
    remote_conn.send("show ip ospf neighbor\n")
    remote_conn.send("sh run\n")
    # Wait for the command to complete
    time.sleep(waittime)

    output = remote_conn.recv(buffer_size)

    # See what we have
    print output

    remote_conn.close()

# function to send the configs to device
def enable_ecmp_on_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,vlan_id,bash_var_exit):

    try:
        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()
        # Automatically add untrusted hosts (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # initiate SSH connection
        remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        print "SSH connection established to %s" % ip+"\n"
        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established\n"

    except paramiko.AuthenticationException:
        print "\nAuthentication Failed\n"
        sys.exit(bash_var_exit)
    except paramiko.SSHException:
        print "\nIssues with SSH service\n"
        sys.exit(bash_var_exit)
    except socket.error,e:
        print "\nConnection Error\n"
        sys.exit(bash_var_exit)

    # Strip the initial router prompt
    output = remote_conn.recv(buffer_size)
    # See what we have
    print output
    # Now let's try to send the NS a command

    remote_conn.send("vtysh\n")
    remote_conn.send("conf t\n")
    remote_conn.send("router ospf\n")
    remote_conn.send("no passive-interface vlan"+vlan_id+"\n")
    remote_conn.send("end\n")
    remote_conn.send("wr\n")
    remote_conn.send("sh run\n")
    remote_conn.send("show ip ospf neighbor\n")
    # Wait for the command to complete
    time.sleep(waittime)

    output = remote_conn.recv(buffer_size)

    # See what we have
    print output

    remote_conn.close()

# function to send the configs to device
def check_image_upload_into_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,myfile,version,bash_var_exit):

    try:
        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()
        # Automatically add untrusted hosts (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # initiate SSH connection
        remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        print "SSH connection established to %s" % ip+"\n"
        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established\n"

    except paramiko.AuthenticationException:
        print "\nAuthentication Failed\n"
        sys.exit(bash_var_exit)
    except paramiko.SSHException:
        print "\nIssues with SSH service\n"
        sys.exit(bash_var_exit)
    except socket.error,e:
        print "\nConnection Error\n"
        sys.exit(bash_var_exit)

    # Strip the initial router prompt
    output = remote_conn.recv(buffer_size)
    # See what we have
    print output
    # Now let's try to send the NS a command

    remote_conn.send("shell\n")
    remote_conn.send("cd /var/nsinstall/build-folder-"+version+"/\n")
    result = remote_conn.send("md5 "+myfile+"\n")
    remote_conn.send("tar -xzvf "+myfile+"\n")
    # Wait for the command to complete
    time.sleep(waittime)

    output = remote_conn.recv(buffer_size)

    ### Check md5 on image
    if output.find(Result) != -1:
        print "############ Matched MD5 ############ \n\n"

    # See what we have
    print output

    remote_conn.close()

# function to send the configs to device

###Usage:
#      -F FIPS install
#      -h help
#      -Y Answer Yes to everything
#      -y Force Reboot
#      -n Don't Reboot
#      -c Force Clean up
#      -N Don't check ns.conf
#      -G no curses
#      -L Enable CallHome

def upgrade_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,myfile,bash_var_exit):

    try:
        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()
        # Automatically add untrusted hosts (make sure okay for security policy in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # initiate SSH connection
        remote_conn_pre.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)
        print "SSH connection established to %s" % ip+"\n"
        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established\n"

    except paramiko.AuthenticationException:
        print "\nAuthentication Failed\n"
        sys.exit(bash_var_exit)
    except paramiko.SSHException:
        print "\nIssues with SSH service\n"
        sys.exit(bash_var_exit)
    except socket.error,e:
        print "\nConnection Error\n"
        sys.exit(bash_var_exit)

    # Strip the initial router prompt
    output = remote_conn.recv(buffer_size)
    # See what we have
    print output
    # Now let's try to send the NS a command

    remote_conn.send("shell\n")
    remote_conn.send("cd /var/nsinstall/build-folder-10.5.59.13/\n")
    remote_conn.send("./installns -L -y\n")
    # Wait for the command to complete
    time.sleep(waittime)

    output = remote_conn.recv(buffer_size)

    # See what we have
    print output

    remote_conn.close()


if __name__ == '__main__':

    #Global Variables
    ip='xx.xx.xx.xx'
    version='10.5.59.13'
    destination= '/var/nsinstall/build-folder-'+version+'/'
    myfile='build-10.5-59.13_nc.tgz'
    buffer_size = 1900000
    waittime = 6
    vlan_id = 'xxx'
    bash_var_exit = 16
    Result =''

    try:
        #TACACS Credentials
        USERNAME = raw_input('\ninsert your username TACACS:')
        PASSWORD = getpass.getpass("Enter your password TACACS:")

        #Backup on Netscaler
        bacukp_ns_confg(ip,USERNAME,PASSWORD,buffer_size,waittime,bash_var_exit)
        #Create folder on Netscaler
        create_folder_on_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,version,bash_var_exit)

        #Upload the image into the folder
        if upload_scp(myfile,destination) == True:
            print "\n\n#################################################"
            print "File uploaded successfully  on Path - "+destination
            print "\n###################################################\n"
            #check image upload into ns with md5
            print "\n"
            print "############## Verify the Integrity of the NetScaler Firmware ###########"
            check_image_upload_into_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,myfile,version,bash_var_exit)
            time.sleep(2)
            #Disabled dinamyc Routing on netscaler
            print "\n"
            print "####### Disabled dinamyc Routing on netscaler (ECMP) #######"
            disable_ecmp_on_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,vlan_id,bash_var_exit)

            #Upgrade Appliance
            print "\n"
            print "####### Upgrade NetScaler #######"
            upgrade_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,myfile,bash_var_exit)

            time.sleep(480)
            for nping in range(1,480):
                subprocess.call("ping <IP>" , shell=True)
                print "\n - " + str(nping)

            #Enabled dinamyc Routing on netscaler
            print "\n"
            print "####### Enabled dinamyc Routing on netscaler (ECMP) #######"
            enable_ecmp_on_ns(ip,USERNAME,PASSWORD,buffer_size,waittime,vlan_id,bash_var_exit)

        else:
            print "File upload failed"
    except Exception as e:
        print str(e.message+"\n")
    finally:
            sys.exit(bash_var_exit)
