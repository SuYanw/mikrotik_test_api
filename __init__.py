
import routeros_api



MK_ADDRESS = '192.168.40.1'
MK_USER = 'glaubert'
MK_PASS = '123'


if __name__ == '__main__':


    connection = routeros_api.RouterOsApiPool(
            host=MK_ADDRESS, 
            username=MK_USER, 
            password=MK_PASS, 
            plaintext_login=True
    )

    api = connection.get_api()

    mk_AddrList = api.get_resource('/ip/firewall/address-list')

    print("Rules without change")
    for __rules in mk_AddrList.get():
        print(f"Listname: {__rules['list']} - Address: {__rules['address']} - Disabled: {__rules['disabled']}")


    print("Adding new ip on list")
    mk_AddrList.add(list="Confiaveis", address="192.168.40.41", disabled='false')

    print("Rules adding new ip addresses:")
    for __rules in mk_AddrList.get():
        print(f"Listname: {__rules['list']} - Address: {__rules['address']} - Disabled: {__rules['disabled']}")

    connection.disconnect()

    