"""Constants for SMA WebConnect library for Python."""
URL_LOGIN = "/dyn/login.json"
URL_LOGOUT = "/dyn/logout.json"
URL_VALUES = "/dyn/getValues.json"
URL_ALL_VALUES = "/dyn/getAllOnlValues.json"
URL_ALL_PARAMS = "/dyn/getAllParamValues.json"
URL_LOGGER = "/dyn/getLogger.json"
URL_DASH_LOGGER = "/dyn/getDashLogger.json"
URL_DASH_VALUES = "/dyn/getDashValues.json"

USERS = {"user": "usr", "installer": "istl"}

DEFAULT_TIMEOUT = 15
DEFAULT_LANG = "en-US"

JMESPATH_VAL = "val"
JMESPATH_VAL_TAG = JMESPATH_VAL + "[0].tag"
JMESPATH_VAL_STR = "[?str==sum([`1`,`{}`])].val | [0]"
JMESPATH_VAL_IDX = "* | [0][{}].val"
JMESPATH_VAL_IDX_TAG = JMESPATH_VAL_IDX + "[0].tag"

JMESPATHS_TAG = (JMESPATH_VAL_IDX_TAG, JMESPATH_VAL_TAG)

LEGACY_MAP = {
    "pv_power": {"old_key": "6100_0046C200", "new_sensor": "pv_power_a"},
    "pv_voltage": {
        "old_key": "6380_40451F00",
        "new_sensor": "pv_power_a",
    },
    "pv_current": {
        "old_key": "6380_40452100",
        "new_sensor": "pv_current_a",
    },
}

FALLBACK_DEVICE_INFO = {
    "manufacturer": "SMA",
    "name": "SMA Device",
    "type": "",
    "serial": "9999999999",
}

GENERIC_SENSORS = "generic"
OPTIMIZERS_VIA_INVERTER = "optimizers"
ENERGY_METER_VIA_INVERTER = "energy-meter"
DEVICE_INFO = "device-info"


class Identifier():
    pv_power_a : str = "pv_power_a"
    pv_power_b : str = "pv_power_b"
    pv_power_c : str = "pv_power_c"
    pv_voltage_a : str = "pv_voltage_a"
    pv_voltage_b : str = "pv_voltage_b"
    pv_voltage_c : str = "pv_voltage_c"
    pv_current_a : str = "pv_current_a"
    pv_current_b : str = "pv_current_b"
    pv_current_c : str = "pv_current_c"
    insulation_residual_current : str = "insulation_residual_current"
    pv_power : str = "pv_power"
    grid_power : str = "grid_power"
    frequency : str = "frequency"
    power_l1 : str = "power_l1"
    power_l2 : str = "power_l2"
    power_l3 : str = "power_l3"
    grid_reactive_power : str = "grid_reactive_power"
    grid_reactive_power_l1 : str = "grid_reactive_power_l1"
    grid_reactive_power_l2 : str = "grid_reactive_power_l2"
    grid_reactive_power_l3 : str = "grid_reactive_power_l3"
    grid_apparent_power : str = "grid_apparent_power"
    grid_apparent_power_l1 : str = "grid_apparent_power_l1"
    grid_apparent_power_l2 : str = "grid_apparent_power_l2"
    grid_apparent_power_l3 : str = "grid_apparent_power_l3"
    grid_power_factor : str = "grid_power_factor"
    current_l1 : str = "current_l1"
    current_l2 : str = "current_l2"
    current_l3 : str = "current_l3"
    current_total : str = "current_total"
    voltage_l1 : str = "voltage_l1"
    voltage_l2 : str = "voltage_l2"
    voltage_l3 : str = "voltage_l3"
    total_yield : str = "total_yield"
    daily_yield : str = "daily_yield"
    metering_power_supplied : str = "metering_power_supplied"
    metering_power_absorbed : str = "metering_power_absorbed"
    metering_frequency : str = "metering_frequency"
    metering_total_yield : str = "metering_total_yield"
    metering_total_absorbed : str = "metering_total_absorbed"
    metering_current_l1 : str = "metering_current_l1"
    metering_current_l2 : str = "metering_current_l2"
    metering_current_l3 : str = "metering_current_l3"
    metering_voltage_l1 : str = "metering_voltage_l1"
    metering_voltage_l2 : str = "metering_voltage_l2"
    metering_voltage_l3 : str = "metering_voltage_l3"
    metering_active_power_feed_l1 : str = "metering_active_power_feed_l1"
    metering_active_power_feed_l2 : str = "metering_active_power_feed_l2"
    metering_active_power_feed_l3 : str = "metering_active_power_feed_l3"
    metering_active_power_draw_l1 : str = "metering_active_power_draw_l1"
    metering_active_power_draw_l2 : str = "metering_active_power_draw_l2"
    metering_active_power_draw_l3 : str = "metering_active_power_draw_l3"
    metering_current_consumption : str = "metering_current_consumption"
    pv_gen_meter : str = "pv_gen_meter"
    sps_voltage : str = "sps_voltage"
    sps_current : str = "sps_current"
    sps_power : str = "sps_power"
    optimizer_serial : str = "optimizer_serial"
    optimizer_power : str = "optimizer_power"
    optimizer_current : str = "optimizer_current"
    optimizer_voltage : str = "optimizer_voltage"
    optimizer_temp : str = "optimizer_temp"
    battery_soc_total : str = "battery_soc_total"
    battery_soc_a : str = "battery_soc_a"
    battery_soc_b : str = "battery_soc_b"
    battery_soc_c : str = "battery_soc_c"
    battery_voltage_a : str = "battery_voltage_a"
    battery_voltage_b : str = "battery_voltage_b"
    battery_voltage_c : str = "battery_voltage_c"
    battery_current_a : str = "battery_current_a"
    battery_current_b : str = "battery_current_b"
    battery_current_c : str = "battery_current_c"
    battery_temp_a : str = "battery_temp_a"
    battery_temp_b : str = "battery_temp_b"
    battery_temp_c : str = "battery_temp_c"
    battery_capacity_total : str = "battery_capacity_total"
    battery_capacity_a : str = "battery_capacity_a"
    battery_capacity_b : str = "battery_capacity_b"
    battery_capacity_c : str = "battery_capacity_c"
    battery_charging_voltage_a : str = "battery_charging_voltage_a"
    battery_charging_voltage_b : str = "battery_charging_voltage_b"
    battery_charging_voltage_c : str = "battery_charging_voltage_c"
    battery_power_charge_total : str = "battery_power_charge_total"
    battery_power_charge_a : str = "battery_power_charge_a"
    battery_power_charge_b : str = "battery_power_charge_b"
    battery_power_charge_c : str = "battery_power_charge_c"
    battery_charge_total : str = "battery_charge_total"
    battery_charge_a : str = "battery_charge_a"
    battery_charge_b : str = "battery_charge_b"
    battery_charge_c : str = "battery_charge_c"
    battery_power_discharge_total : str = "battery_power_discharge_total"
    battery_power_discharge_a : str = "battery_power_discharge_a"
    battery_power_discharge_b : str = "battery_power_discharge_b"
    battery_power_discharge_c : str = "battery_power_discharge_c"
    battery_discharge_total : str = "battery_discharge_total"
    battery_discharge_a : str = "battery_discharge_a"
    battery_discharge_b : str = "battery_discharge_b"
    battery_discharge_c : str = "battery_discharge_c"
    serial_number : str = "serial_number"
    device_name : str = "device_name"
    device_type : str = "device_type"
    device_manufacturer : str = "device_manufacturer"
    device_sw_version : str = "device_sw_version"
    inverter_power_limit : str = "inverter_power_limit"
    energy_meter : str = "energy_meter"
