from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as xe_model

#CSR1kv1 Credentials
ip = '10.0.0.20'
port_n = 830
user = 'cisco'
paswd = 'cisco'
proto = 'ssh'

if __name__ == '__main__':

        provider = NetconfServiceProvider(address=ip, port=port_n, username=user, password=paswd, protocol=proto)

        crud = CRUDService()

        # get hold of onyl the fifth GigabitEthernet interface without the other interfaces
        xe_int_giga =  xe_model.Native.Interface.GigabitEthernet()
        xe_int_giga.name = '5'

        # read the interface 
        intf_data = crud.read(provider, xe_int_giga)

        # print the primary addres of the interface
        print(intf_data.ip.address.primary.address)
        
        # update the description of the interface
      
      

        # print the description of the interface
       
        
        exit()

