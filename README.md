### Mikrotik API Testing without cert
This is an Mikrotik testing api without certificate, tested on RouterOS 6.47.10! Using [RouterOS-api](https://github.com/socialwifi/RouterOS-api) by Social WIFI



### Clent credentials:
Please, before this, check api_port(8728) already acivated or change api_port adding 'port=' parameter on connection.

```python
MK_ADDRESS = '192.168.40.1'
MK_USER = 'glaubert'
MK_PASS = '123'
```


### code example result
![out-put](https://i.ibb.co/qkZyhBD/testimg.png)



### dependencies
This code neeeded installing the package via PIP
```pip
#pip install routeros_api
```

