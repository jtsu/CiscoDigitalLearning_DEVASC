from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as xe_model

# CSR1kv1 Credentials
ip = '0.0.0.0'
port_n = 0
user = 'username'
paswd = 'password'
proto = 'protocol'

if __name__ == '__main__':

        provider = NetconfServiceProvider(address=ip, port=port_n, username=user, password=paswd, protocol=proto)

        # create a CRUD service
        

        # create a new istance of Native Inteface object
        

        # read the interfaces with the help of read function
        

        # print the primary address of the fifth gigabitethernet interface
        
        
        exit()
