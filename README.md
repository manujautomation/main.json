=================
Current output:
=================


{
    "enb": {
        "s1c_bind_port": 5847, 
        "mnc": "50", 
        "log": {
            "pdcp_level": "info", 
            "udp_remote_ip": "172.29.241.1", 
            "gtpu_level": "info", 
            "phy_level": "info", 
            "udp_remote_port": 30020, 
            "mac_level": "info"
        }, 
        "s1c_bind_addr": "192.168.1.115", 
        "mcc": "050", 
        "gtp_bind_addr": "192.168.1.115", 
        "tm": 7, 
        "n_prb": 25, 
        "mme_addr": "192.168.1.47", 
        "pcap": {
            "s1ap_enable": true, 
            "enable": false, 
            "mac_net_enable": true
        }, 
        "id": "0xc9"
    }, 
    "rr": {
        "cell_list": [
            {
                "ho_active": true, 
                "meas_cell_list": [
                    {
                        "pci": 210, 
                        "allowed_meas_bw": 25, 
                        "dl_earfcn": 60075, 
                        "eci": 51201, 
                        "tac": "0x7"
                    }, 
                    {
                        "pci": 13, 
                        "allowed_meas_bw": 25, 
                        "dl_earfcn": 60275, 
                        "eci": 31492, 
                        "tac": "0x7"
                    }
                ], 
                "cell_id": 2, 
                "target_pusch_sinr": 21, 
                "allowed_meas_bw": 25, 
                "direct_forward_path_enable": "true", 
                "pci": 211, 
                "tac": "0x7", 
                "dl_earfcn": 60075, 
                "meas_gap_period": 40
            }
        ]
    }, 
    "enodeb": {
        "demon_stdout": "/var/log/enodeb.out", 
        "run_enodeb": 1
    }, 
    "snmp": {
        "trapAuthPassword": "auth_password", 
        "trapUser": "username", 
        "authProtocol": "SHA-256", 
        "privProtocol": "AES", 
        "engineID": "0x0070000002", 
        "trapPrivProtocol": "AES", 
        "user": "username", 
        "privPassword": "priv_password", 
        "trapPrivPassword": "priv_password", 
        "trapAuthProtocol": "SHA-256", 
        "trapManagerAddress": "172.29.250.16:33947", 
        "authPassword": "auth_password", 
        "alarmType": "trap"
    }, 
    "sib": {
        "sib3": {
            "intra_freq_reselection": {
                "allowed_meas_bw": 25
            }
        }, 
        "sib1": {
            "sched_info": [
                {
                    "si_mapping_info": [], 
                    "si_periodicity": 32
                }, 
                {
                    "si_mapping_info": [
                        3, 
                        9
                    ], 
                    "si_periodicity": 64
                }
            ]
        }, 
        "sib9": {
            "latitude": 39.01755, 
            "altitude": 0, 
            "site_id": 1, 
            "longitude": -77.421549999999996
        }
    }, 
    "phy": {
        "enable_sector_1": 0, 
        "enable_sector_2": 1, 
        "enable_sector_3": 1
    }
}




=============================
Required Output:
=============================

{"snmp":{"alarmType":"trap","engineID":"0x0070000002","user":"username","authProtocol":"SHA-256","privProtocol":"AES","authPassword":"auth_password","privPassword":"priv_password","trapUser":"username","trapAuthProtocol":"SHA-256","trapPrivProtocol":"AES","trapAuthPassword":"auth_password","trapPrivPassword":"priv_password","trapManagerAddress":"172.29.250.16:36116"},"phy":{"enable_sector_1":0,"enable_sector_2":1,"enable_sector_3":1},"enodeb":{"demon_stdout":"/var/log/enodeb.out","run_enodeb":1},"enb":{"pcap":{"enable":false,"s1ap_enable":true,"mac_net_enable":true},"log":{"phy_level":"info","pdcp_level":"info","gtpu_level":"info","mac_level":"info","udp_remote_ip":"172.29.241.1","udp_remote_port":30020},"id":"0xc9","mcc":"050","mnc":"50","mme_addr":"192.168.30.26","gtp_bind_addr":"172.29.241.9","s1c_bind_addr":"172.29.241.9","s1c_bind_port":5847,"n_prb":25,"tm":7,"n_prb_by_bandwidth":{"LTE_10_MHz":25,"LTE_5_MHz":50}},"sib":{"sib1":{"sched_info":[{"si_periodicity":32,"si_mapping_info":[]},{"si_periodicity":64,"si_mapping_info":[3,9]}]},"sib3":{"intra_freq_reselection":{"allowed_meas_bw":50}},"sib9":{"site_id":1,"latitude":39.01755,"longitude":-77.42155,"altitude":0}},"rr":{"cell_list":[{"cell_id":11,"tac":"0x7","pci":211,"dl_earfcn":60275,"meas_gap_period":80,"ho_active":true,"target_pusch_sinr":21,"meas_cell_list":[{"eci":51210,"dl_earfcn":60250,"pci":210,"tac":"0x7","allowed_meas_bw":50},{"eci":31492,"dl_earfcn":60150,"pci":13,"tac":"0x7","allowed_meas_bw":50}],"direct_forward_path_enable":"true","allowed_meas_bw":50}]}}

