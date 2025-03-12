# This is the template code for the CNE335 Final Project
# Kaylie Velazquez
# CNE 335 Winter

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Kaylie")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    ec2_user = Server("54.218.9.30") #My ec2 public ip address from my instance
    # TODO - Call Ping method and print the results
    ec2_user.ping()
