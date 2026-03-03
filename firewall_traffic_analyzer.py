# FILE NAME - firewall_traffic_analyzer.py
# NAME: Connor Beer
# DATE: March 3, 2026
# BRIEF DESCRIPTION:  Uses inputted port numbers and data transfer numbers to determine if there is a threat to a firewall

########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    firewall_analyzer()

def firewall_analyzer():
    print('=== Network Traffic Security Analyzer ===')
    print()
    port_number = int(input('Enter the port number (e.g., 80, 22, 443, 3389): '))
    transfer_size = int(input('Enter the data transfer size in megabytes (MB): '))
    print()
    print('FIREWALL LOG:')

    if port_number == 22 or port_number == 3389 and transfer_size >= 100:
        print(f'Port: {port_number}, Transfer Size: {transfer_size} MB')
        print('Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!')
    elif port_number == 80 and transfer_size > 100:
        print(f'Port: {port_number}, Transfer Size: {transfer_size} MB')
        print('Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.')
    elif port_number == 443:
        print(f'Port: {port_number}, Transfer Size: {transfer_size} MB')
        print('Risk Assessment: LOW RISK: Secure encrypted transfer detected.')
    else:
        print(f'Port: {port_number}, Transfer Size: {transfer_size} MB')
        print('Risk Assessment: UNKNOWN: Unrecognized traffic pattern.')
    print('------------------------')

main()

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          REFLECTION QUESTIONS
########################################

'''
1. Did you get tripped up using the `or` or `and` operators? If so, how?
no I was able to easily use them separately and together with no issues
'''