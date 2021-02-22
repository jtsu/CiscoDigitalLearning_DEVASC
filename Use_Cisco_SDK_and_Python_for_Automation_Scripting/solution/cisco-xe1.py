from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as xe_model

# CSR1kv1 Credentials
ip = '10.0.0.20'
port_n = 830
user = 'cisco'
paswd = 'cisco'
proto = 'ssh'

if __name__ == '__main__':

        provider = NetconfServiceProvider(address=ip, port=port_n, username=user, password=paswd, protocol=proto)

        # open the connection w/ CRUDService
        crud = CRUDService()

        # create a new instance of Native Interface object
        xe_interfaces = xe_model.Native.Interface()

        # read the interfaces with the help of read function
        interfaces_data = crud.read(provider, xe_interfaces)

        # print the primary address of the fifth gigabitethernet interface
        print(interfaces_data.gigabitethernet[4].ip.address.primary.address)

        exit()

