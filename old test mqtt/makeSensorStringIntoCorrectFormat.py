from datetime import datetime
import json
now = datetime.now()
dateAndTime = now.strftime("%Y/%m/%d, %H:%M:%S")



sensorData = str(b'{"end_device_ids":{"device_id":"eui-a81758fffe075b66","application_ids":{"application_id":"ap-addiva-01"},"dev_eui":"A81758FFFE075B66","join_eui":"0000000000000000","dev_addr":"260B7CBF"},"correlation_ids":["as:up:01GF2VZ0VTX9XAFW302JNRGZ2N","gs:conn:01GF2N1DC1WH718809DF6YZK7T","gs:up:host:01GF2N1DC9H01SRWBBT65CQTXN","gs:uplink:01GF2VZ0NC4PW9APPZYM0M8TQ7","ns:uplink:01GF2VZ0ND22K6QCBH4FHE59MM","rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01GF2VZ0ND8JYZHRSJWNJH57EC","rpc:/ttn.lorawan.v3.NsAs/HandleUplink:01GF2VZ0VS9D608W3VS5NJG5FE"],"received_at":"2022-10-11T06:33:26.138030136Z","uplink_message":{"session_key_id":"AYPB0ECOhnp1uMUPjFkrxw==","f_port":5,"f_cnt":942,"frm_payload":"AQDiAiMHDicSAA==","decoded_payload":{"humidity":35,"temperature":22.6,"vdd":3623,"waterleak":0},"rx_metadata":[{"gateway_ids":{"gateway_id":"rg1xx2965f5","eui":"C0EE40FFFF2965F5"},"time":"2022-10-11T06:33:25.888335943Z","timestamp":2965795924,"rssi":-55,"channel_rssi":-55,"snr":9.75,"location":{"latitude":59.605889553757784,"longitude":16.552834510803226,"altitude":10,"source":"SOURCE_REGISTRY"},"uplink_token":"ChkKFwoLcmcxeHgyOTY1ZjUSCMDuQP//KWX1ENTomYYLGgwItZyUmgYQidvhvAMgoNDZuajTAQ==","received_at":"2022-10-11T06:33:25.912897349Z"}],"settings":{"data_rate":{"lora":{"bandwidth":125000,"spreading_factor":7,"coding_rate":"4/5"}},"frequency":"867900000","timestamp":2965795924,"time":"2022-10-11T06:33:25.888335943Z"},"received_at":"2022-10-11T06:33:25.933651342Z","confirmed":true,"consumed_airtime":"0.061696s","locations":{"user":{"latitude":59.60599410588323,"longitude":16.552834510803226,"source":"SOURCE_REGISTRY"}},"version_ids":{"brand_id":"elsys","model_id":"ems-lite","hardware_version":"1.0","firmware_version":"1.0","band_id":"EU_863_870"},"network_ids":{"net_id":"000013","tenant_id":"ttn","cluster_id":"eu1","cluster_address":"eu1.cloud.thethings.network"}}}')
sensorData = sensorData[2:-1]

document = json.loads(sensorData)

payloadlvl1 = document["uplink_message"]
payloadlvl2 = payloadlvl1["decoded_payload"]


idLvl1 = document["end_device_ids"]
idLvl2 = idLvl1["device_id"]
#x = document.get("end_device_ids"("device_id"))


# document = json.loads(sensorData)
# document["time"] = str(dateAndTime)

# fixed_document = {"Sensor address": "Addiva Test Sigurdsgatan"}
# fixed_document.update(document)


print(f"Decive id: {idLvl2}")
print(f"Payload: {payloadlvl2}")

