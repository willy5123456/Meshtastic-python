# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: radioconfig.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11radioconfig.proto\"\xca\x18\n\x0bRadioConfig\x12\x31\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x1c.RadioConfig.UserPreferences\x1a\x87\x18\n\x0fUserPreferences\x12\x1f\n\x17position_broadcast_secs\x18\x01 \x01(\r\x12 \n\x18position_broadcast_smart\x18\x11 \x01(\x08\x12\x1b\n\x13send_owner_interval\x18\x02 \x01(\r\x12\x1b\n\x13wait_bluetooth_secs\x18\x04 \x01(\r\x12\x16\n\x0escreen_on_secs\x18\x05 \x01(\r\x12\x1a\n\x12phone_timeout_secs\x18\x06 \x01(\r\x12\x1d\n\x15phone_sds_timeout_sec\x18\x07 \x01(\r\x12\x1d\n\x15mesh_sds_timeout_secs\x18\x08 \x01(\r\x12\x10\n\x08sds_secs\x18\t \x01(\r\x12\x0f\n\x07ls_secs\x18\n \x01(\r\x12\x15\n\rmin_wake_secs\x18\x0b \x01(\r\x12\x11\n\twifi_ssid\x18\x0c \x01(\t\x12\x15\n\rwifi_password\x18\r \x01(\t\x12\x14\n\x0cwifi_ap_mode\x18\x0e \x01(\x08\x12\x1b\n\x06region\x18\x0f \x01(\x0e\x32\x0b.RegionCode\x12&\n\x0e\x63harge_current\x18\x10 \x01(\x0e\x32\x0e.ChargeCurrent\x12\x11\n\tis_router\x18% \x01(\x08\x12\x14\n\x0cis_low_power\x18& \x01(\x08\x12\x16\n\x0e\x66ixed_position\x18\' \x01(\x08\x12\x17\n\x0fserial_disabled\x18( \x01(\x08\x12(\n\x0elocation_share\x18  \x01(\x0e\x32\x10.LocationSharing\x12$\n\rgps_operation\x18! \x01(\x0e\x32\r.GpsOperation\x12\x1b\n\x13gps_update_interval\x18\" \x01(\r\x12\x18\n\x10gps_attempt_time\x18$ \x01(\r\x12\x15\n\rgps_accept_2d\x18- \x01(\x08\x12\x13\n\x0bgps_max_dop\x18. \x01(\r\x12\x18\n\x10\x66requency_offset\x18) \x01(\x02\x12\x13\n\x0bmqtt_server\x18* \x01(\t\x12\x15\n\rmqtt_disabled\x18+ \x01(\x08\x12(\n\ngps_format\x18, \x01(\x0e\x32\x14.GpsCoordinateFormat\x12\x15\n\rfactory_reset\x18\x64 \x01(\x08\x12\x19\n\x11\x64\x65\x62ug_log_enabled\x18\x65 \x01(\x08\x12\x17\n\x0fignore_incoming\x18g \x03(\r\x12\x1c\n\x14serialplugin_enabled\x18x \x01(\x08\x12\x19\n\x11serialplugin_echo\x18y \x01(\x08\x12\x18\n\x10serialplugin_rxd\x18z \x01(\r\x12\x18\n\x10serialplugin_txd\x18{ \x01(\r\x12\x1c\n\x14serialplugin_timeout\x18| \x01(\r\x12\x19\n\x11serialplugin_mode\x18} \x01(\r\x12\'\n\x1f\x65xt_notification_plugin_enabled\x18~ \x01(\x08\x12)\n!ext_notification_plugin_output_ms\x18\x7f \x01(\r\x12\'\n\x1e\x65xt_notification_plugin_output\x18\x80\x01 \x01(\r\x12\'\n\x1e\x65xt_notification_plugin_active\x18\x81\x01 \x01(\x08\x12.\n%ext_notification_plugin_alert_message\x18\x82\x01 \x01(\x08\x12+\n\"ext_notification_plugin_alert_bell\x18\x83\x01 \x01(\x08\x12\"\n\x19range_test_plugin_enabled\x18\x84\x01 \x01(\x08\x12!\n\x18range_test_plugin_sender\x18\x85\x01 \x01(\r\x12\x1f\n\x16range_test_plugin_save\x18\x86\x01 \x01(\x08\x12%\n\x1cstore_forward_plugin_enabled\x18\x94\x01 \x01(\x08\x12\'\n\x1estore_forward_plugin_heartbeat\x18\x95\x01 \x01(\x08\x12%\n\x1cstore_forward_plugin_records\x18\x89\x01 \x01(\r\x12\x30\n\'store_forward_plugin_history_return_max\x18\x8a\x01 \x01(\r\x12\x33\n*store_forward_plugin_history_return_window\x18\x8b\x01 \x01(\r\x12=\n4environmental_measurement_plugin_measurement_enabled\x18\x8c\x01 \x01(\x08\x12\x38\n/environmental_measurement_plugin_screen_enabled\x18\x8d\x01 \x01(\x08\x12\x44\n;environmental_measurement_plugin_read_error_count_threshold\x18\x8e\x01 \x01(\r\x12\x39\n0environmental_measurement_plugin_update_interval\x18\x8f\x01 \x01(\r\x12;\n2environmental_measurement_plugin_recovery_interval\x18\x90\x01 \x01(\r\x12;\n2environmental_measurement_plugin_display_farenheit\x18\x91\x01 \x01(\x08\x12v\n,environmental_measurement_plugin_sensor_type\x18\x92\x01 \x01(\x0e\x32?.RadioConfig.UserPreferences.EnvironmentalMeasurementSensorType\x12\x34\n+environmental_measurement_plugin_sensor_pin\x18\x93\x01 \x01(\r\x12\x17\n\x0eposition_flags\x18\x96\x01 \x01(\r\x12\x1a\n\x11is_always_powered\x18\x97\x01 \x01(\x08\x12\"\n\x19\x61uto_screen_carousel_secs\x18\x98\x01 \x01(\r\x12\'\n\x1eon_battery_shutdown_after_secs\x18\x99\x01 \x01(\r\x12\x12\n\thop_limit\x18\x9a\x01 \x01(\r\x12\x16\n\rmqtt_username\x18\x9b\x01 \x01(\t\x12\x16\n\rmqtt_password\x18\x9c\x01 \x01(\t\x12\x1c\n\x13is_lora_tx_disabled\x18\x9d\x01 \x01(\x08\x12\x18\n\x0fis_power_saving\x18\x9e\x01 \x01(\x08\x12\x18\n\x0frotary1_enabled\x18\xa0\x01 \x01(\x08\x12\x16\n\rrotary1_pin_a\x18\xa1\x01 \x01(\r\x12\x16\n\rrotary1_pin_b\x18\xa2\x01 \x01(\r\x12\x1a\n\x11rotary1_pin_press\x18\xa3\x01 \x01(\r\x12*\n\x10rotary1_event_cw\x18\xa4\x01 \x01(\x0e\x32\x0f.InputEventChar\x12+\n\x11rotary1_event_ccw\x18\xa5\x01 \x01(\x0e\x32\x0f.InputEventChar\x12-\n\x13rotary1_event_press\x18\xa6\x01 \x01(\x0e\x32\x0f.InputEventChar\x12&\n\x1d\x63\x61nned_message_plugin_enabled\x18\xaa\x01 \x01(\x08\x12\x31\n(canned_message_plugin_allow_input_source\x18\xab\x01 \x01(\t\x12+\n\x1e\x63\x61nned_message_plugin_messages\x18\xac\x01 \x01(\tB\x02\x18\x01\x12(\n\x1f\x63\x61nned_message_plugin_send_bell\x18\xad\x01 \x01(\x08\x12 \n\x17mqtt_encryption_enabled\x18\xae\x01 \x01(\x08\x12 \n\x17\x61\x64\x63_multiplier_override\x18\xaf\x01 \x01(\x02\"\x82\x01\n\"EnvironmentalMeasurementSensorType\x12\t\n\x05\x44HT11\x10\x00\x12\x0b\n\x07\x44S18B20\x10\x01\x12\t\n\x05\x44HT12\x10\x02\x12\t\n\x05\x44HT21\x10\x03\x12\t\n\x05\x44HT22\x10\x04\x12\n\n\x06\x42ME280\x10\x05\x12\n\n\x06\x42ME680\x10\x06\x12\x0b\n\x07MCP9808\x10\x07J\x06\x08\x88\x01\x10\x89\x01*f\n\nRegionCode\x12\t\n\x05Unset\x10\x00\x12\x06\n\x02US\x10\x01\x12\t\n\x05\x45U433\x10\x02\x12\t\n\x05\x45U865\x10\x03\x12\x06\n\x02\x43N\x10\x04\x12\x06\n\x02JP\x10\x05\x12\x07\n\x03\x41NZ\x10\x06\x12\x06\n\x02KR\x10\x07\x12\x06\n\x02TW\x10\x08\x12\x06\n\x02RU\x10\t*\xd1\x01\n\rChargeCurrent\x12\x0b\n\x07MAUnset\x10\x00\x12\t\n\x05MA100\x10\x01\x12\t\n\x05MA190\x10\x02\x12\t\n\x05MA280\x10\x03\x12\t\n\x05MA360\x10\x04\x12\t\n\x05MA450\x10\x05\x12\t\n\x05MA550\x10\x06\x12\t\n\x05MA630\x10\x07\x12\t\n\x05MA700\x10\x08\x12\t\n\x05MA780\x10\t\x12\t\n\x05MA880\x10\n\x12\t\n\x05MA960\x10\x0b\x12\n\n\x06MA1000\x10\x0c\x12\n\n\x06MA1080\x10\r\x12\n\n\x06MA1160\x10\x0e\x12\n\n\x06MA1240\x10\x0f\x12\n\n\x06MA1320\x10\x10*j\n\x0cGpsOperation\x12\x0e\n\nGpsOpUnset\x10\x00\x12\x13\n\x0fGpsOpStationary\x10\x01\x12\x0f\n\x0bGpsOpMobile\x10\x02\x12\x11\n\rGpsOpTimeOnly\x10\x03\x12\x11\n\rGpsOpDisabled\x10\x04*\x83\x01\n\x13GpsCoordinateFormat\x12\x10\n\x0cGpsFormatDec\x10\x00\x12\x10\n\x0cGpsFormatDMS\x10\x01\x12\x10\n\x0cGpsFormatUTM\x10\x02\x12\x11\n\rGpsFormatMGRS\x10\x03\x12\x10\n\x0cGpsFormatOLC\x10\x04\x12\x11\n\rGpsFormatOSGR\x10\x05*@\n\x0fLocationSharing\x12\x0c\n\x08LocUnset\x10\x00\x12\x0e\n\nLocEnabled\x10\x01\x12\x0f\n\x0bLocDisabled\x10\x02*\xbc\x01\n\rPositionFlags\x12\x11\n\rPOS_UNDEFINED\x10\x00\x12\x10\n\x0cPOS_ALTITUDE\x10\x01\x12\x0f\n\x0bPOS_ALT_MSL\x10\x02\x12\x0f\n\x0bPOS_GEO_SEP\x10\x04\x12\x0b\n\x07POS_DOP\x10\x08\x12\r\n\tPOS_HVDOP\x10\x10\x12\x0f\n\x0bPOS_BATTERY\x10 \x12\x11\n\rPOS_SATINVIEW\x10@\x12\x10\n\x0bPOS_SEQ_NOS\x10\x80\x01\x12\x12\n\rPOS_TIMESTAMP\x10\x80\x02*\x83\x01\n\x0eInputEventChar\x12\x0c\n\x08KEY_NONE\x10\x00\x12\n\n\x06KEY_UP\x10\x11\x12\x0c\n\x08KEY_DOWN\x10\x12\x12\x0c\n\x08KEY_LEFT\x10\x13\x12\r\n\tKEY_RIGHT\x10\x14\x12\x0e\n\nKEY_SELECT\x10\n\x12\x0c\n\x08KEY_BACK\x10\x1b\x12\x0e\n\nKEY_CANCEL\x10\x18\x42M\n\x13\x63om.geeksville.meshB\x11RadioConfigProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3')

_REGIONCODE = DESCRIPTOR.enum_types_by_name['RegionCode']
RegionCode = enum_type_wrapper.EnumTypeWrapper(_REGIONCODE)
_CHARGECURRENT = DESCRIPTOR.enum_types_by_name['ChargeCurrent']
ChargeCurrent = enum_type_wrapper.EnumTypeWrapper(_CHARGECURRENT)
_GPSOPERATION = DESCRIPTOR.enum_types_by_name['GpsOperation']
GpsOperation = enum_type_wrapper.EnumTypeWrapper(_GPSOPERATION)
_GPSCOORDINATEFORMAT = DESCRIPTOR.enum_types_by_name['GpsCoordinateFormat']
GpsCoordinateFormat = enum_type_wrapper.EnumTypeWrapper(_GPSCOORDINATEFORMAT)
_LOCATIONSHARING = DESCRIPTOR.enum_types_by_name['LocationSharing']
LocationSharing = enum_type_wrapper.EnumTypeWrapper(_LOCATIONSHARING)
_POSITIONFLAGS = DESCRIPTOR.enum_types_by_name['PositionFlags']
PositionFlags = enum_type_wrapper.EnumTypeWrapper(_POSITIONFLAGS)
_INPUTEVENTCHAR = DESCRIPTOR.enum_types_by_name['InputEventChar']
InputEventChar = enum_type_wrapper.EnumTypeWrapper(_INPUTEVENTCHAR)
Unset = 0
US = 1
EU433 = 2
EU865 = 3
CN = 4
JP = 5
ANZ = 6
KR = 7
TW = 8
RU = 9
MAUnset = 0
MA100 = 1
MA190 = 2
MA280 = 3
MA360 = 4
MA450 = 5
MA550 = 6
MA630 = 7
MA700 = 8
MA780 = 9
MA880 = 10
MA960 = 11
MA1000 = 12
MA1080 = 13
MA1160 = 14
MA1240 = 15
MA1320 = 16
GpsOpUnset = 0
GpsOpStationary = 1
GpsOpMobile = 2
GpsOpTimeOnly = 3
GpsOpDisabled = 4
GpsFormatDec = 0
GpsFormatDMS = 1
GpsFormatUTM = 2
GpsFormatMGRS = 3
GpsFormatOLC = 4
GpsFormatOSGR = 5
LocUnset = 0
LocEnabled = 1
LocDisabled = 2
POS_UNDEFINED = 0
POS_ALTITUDE = 1
POS_ALT_MSL = 2
POS_GEO_SEP = 4
POS_DOP = 8
POS_HVDOP = 16
POS_BATTERY = 32
POS_SATINVIEW = 64
POS_SEQ_NOS = 128
POS_TIMESTAMP = 256
KEY_NONE = 0
KEY_UP = 17
KEY_DOWN = 18
KEY_LEFT = 19
KEY_RIGHT = 20
KEY_SELECT = 10
KEY_BACK = 27
KEY_CANCEL = 24


_RADIOCONFIG = DESCRIPTOR.message_types_by_name['RadioConfig']
_RADIOCONFIG_USERPREFERENCES = _RADIOCONFIG.nested_types_by_name['UserPreferences']
_RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE = _RADIOCONFIG_USERPREFERENCES.enum_types_by_name['EnvironmentalMeasurementSensorType']
RadioConfig = _reflection.GeneratedProtocolMessageType('RadioConfig', (_message.Message,), {

  'UserPreferences' : _reflection.GeneratedProtocolMessageType('UserPreferences', (_message.Message,), {
    'DESCRIPTOR' : _RADIOCONFIG_USERPREFERENCES,
    '__module__' : 'radioconfig_pb2'
    # @@protoc_insertion_point(class_scope:RadioConfig.UserPreferences)
    })
  ,
  'DESCRIPTOR' : _RADIOCONFIG,
  '__module__' : 'radioconfig_pb2'
  # @@protoc_insertion_point(class_scope:RadioConfig)
  })
_sym_db.RegisterMessage(RadioConfig)
_sym_db.RegisterMessage(RadioConfig.UserPreferences)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\021RadioConfigProtosH\003Z!github.com/meshtastic/gomeshproto'
  _RADIOCONFIG_USERPREFERENCES.fields_by_name['canned_message_plugin_messages']._options = None
  _RADIOCONFIG_USERPREFERENCES.fields_by_name['canned_message_plugin_messages']._serialized_options = b'\030\001'
  _REGIONCODE._serialized_start=3170
  _REGIONCODE._serialized_end=3272
  _CHARGECURRENT._serialized_start=3275
  _CHARGECURRENT._serialized_end=3484
  _GPSOPERATION._serialized_start=3486
  _GPSOPERATION._serialized_end=3592
  _GPSCOORDINATEFORMAT._serialized_start=3595
  _GPSCOORDINATEFORMAT._serialized_end=3726
  _LOCATIONSHARING._serialized_start=3728
  _LOCATIONSHARING._serialized_end=3792
  _POSITIONFLAGS._serialized_start=3795
  _POSITIONFLAGS._serialized_end=3983
  _INPUTEVENTCHAR._serialized_start=3986
  _INPUTEVENTCHAR._serialized_end=4117
  _RADIOCONFIG._serialized_start=22
  _RADIOCONFIG._serialized_end=3168
  _RADIOCONFIG_USERPREFERENCES._serialized_start=89
  _RADIOCONFIG_USERPREFERENCES._serialized_end=3168
  _RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE._serialized_start=3030
  _RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE._serialized_end=3160
# @@protoc_insertion_point(module_scope)
