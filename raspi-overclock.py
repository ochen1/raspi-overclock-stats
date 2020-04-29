#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

def get_req_freq():
    try:
        # Get the kernel-requested CPU frequency
        # The frequency may not be the actual frequency, for example when throttling is triggered as a result of CPU overheating
        freq = float(os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").readline())
        # Change the CPU frequency to MHz
        freq = freq / 1000
        return freq
    except ValueError:
        return 0

def get_act_freq():
    try:
        # Get the current CPU frequency
        actfreq = float(os.popen("vcgencmd measure_clock arm").readline().replace("frequency(45)=", ''))
        # Change the CPU frequency to MHz
        actfreq = actfreq / 1000000
        return actfreq
    except ValueError:
        return 0

def get_core_freq():
    try:
        # Get the core frequency
        corefreq = float(os.popen("vcgencmd measure_clock core").readline().replace("frequency(1)=", ''))
        # Change the CPU frequency to MHz
        corefreq = corefreq / 1000000
        return corefreq
    except ValueError:
        return 0

def get_core_voltage():
    try:
        # Get the core voltage
        corevolt = float(os.popen("vcgencmd measure_volts core").readline().replace("volt=", '').replace('V', ''))
        return corevolt
    except ValueError:
        return 0

def get_sdram1_voltage():
    try:
        sdram1volt = float(os.popen("vcgencmd measure_volts sdram_c").readline().replace("volt=", '').replace('V', ''))
        return sdram1volt
    except ValueError:
        return 0

def get_sdram2_voltage():
    try:
        sdram2volt = float(os.popen("vcgencmd measure_volts sdram_i").readline().replace("volt=", '').replace('V', ''))
        return sdram2volt
    except ValueError:
        return 0

def get_sdram3_voltage():
    try:
        sdram3volt = float(os.popen("vcgencmd measure_volts sdram_p").readline().replace("volt=", '').replace('V', ''))
        return sdram3volt
    except ValueError:
        return 0

def get_CPU_temp():
    try:
        # Get the CPU temperature
        cputemp = float(os.popen("echo $((cpu))").readline())
        # Change the temperature to degrees Celsius
        cputemp = cputemp / 1000
        return cputemp
    except ValueError:
        return 0

def get_GPU_temp():
    try:
        # Get the GPU temperature
        gputemp = float(os.popen("vcgencmd measure_temp").readline().replace("temp=", '').replace("'C", ''))
        return gputemp
    except ValueError:
        return 0

def get_SoC_temp():
    try:
        # Get the SoC temperature
        soctemp = float(os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline())
        # Change the temperature to degrees Celsius
        soctemp = soctemp / 1000
        return soctemp
    except ValueError:
        return 0

if __name__ == "__main__":
    # Print text to the user
    date = os.popen("echo $(date)").readline().strip()
    hostname = os.popen("echo $(hostname)").readline().strip()
    print("""Raspberry Pi Overclocking Monitor
---------------------------------
%s @ %s
Kernel-requested CPU Frequency: %f MHz
ARM CPU Frequency: %f MHz
Core Frequency: %f MHz
Core Voltage: %f V
sdram_c Voltage: %f V
sdram_i Voltage: %f V
sdram_p Voltage: %f V
CPU Temperature: %f°C (via cpu)
GPU Temperature: %f°C (via vcgencmd (live GPU))
SoC Temperature: %f°C (via /sys/class/thermal/thermal_zone0/temp)""" % (date, hostname, get_req_freq(), get_act_freq(), get_core_freq(), get_core_voltage(), get_sdram1_voltage(), get_sdram2_voltage(), get_sdram3_voltage(), get_CPU_temp(), get_GPU_temp(), get_SoC_temp()))

