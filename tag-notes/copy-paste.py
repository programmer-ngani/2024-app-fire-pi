Mga Hakbang:

A. Pagbukas ng Thonny IDE at Pag-connect ng Pico
1) Buksan ang Thonny IDE.
2) Mula sa Menu Bar: pillin ang Tools, Options, Interpreter.
3) Piliin ang Local Python 3 na interpreter ng code (kung walang Pico).
4) Isaksak sa USB Port ang Pico.
5) Pumunta ulit sa Menu Bar: pillin ang Tools, Options, Interpreter.
6) Piliin ang MicroPython (Raspberry Pi Pico) na interpreter ng code.
7) Piliin ang Try to detect port automatically sa Port or WebREPL.
8) Shortcut: Select Interpreter sa bottom-right corner ng Thonny IDE window.
8.1) Select or re-select MicroPython (Raspberry Pi Pico) na backend.
8.2) Walang error na lalabas sa Shell sa baba ng Thonny IDE window.

B. Paggawa ng Python Script (Code) sa Thonny IDE at Pagsave ng File sa Pico
1) Magtype ng code sa editor.
print("testing lang.")
2) Para mag-testing ng code.
2.1) Mula sa Menu Bar: pillin ang Run, Run current script (F5).
2.2) Shortcut: pindutin ang Run Icon.
3) Para mag-save ng code.
3.1) Mula sa Menu Bar: pillin ang File, Save o Save As.
3.2) Shortcut: pindutin ang CTRL+S ng sabay.
3.3) Where to save to? Piliin ang Raspberry Pi Pico.
3.4) Mag-type ng pangalan ng file (test-print.py), click OK.
3.5) Pindutin ang CTRL+W ng sabay para mag-close ang editor.

C. Pagbukas ng Python Script (Code) mula sa Pico
1. Gawin ang mga hakbang sa Step A.
2. Para mag-open ng code.
3.1) Mula sa Menu Bar: pillin ang File, Open.
3.2) Shortcut: pindutin ang CTRL+O ng sabay.
3.3) Where to open from? Piliin ang Raspberry Pi Pico.
3.4) Piliin ang file (test-print.py), click OK.
3.5) Makikita ang laman ng file sa code editor.
3.6) Pwedeng mag-edit o type ng code.
3.7) Pwedeng mag-run o test ng code.

D. Gawain (Code)
1. Mag-save ng tatlong file sa Pico.
1.1) Ang unang file ay ssd1306.py
1.1.1) Ang laman ay:
#kuhain sa <ssd1306.py>
1.2) Ang sunod na file ay settings.py
1.2.1) Ang laman ay:
#kuhain sa <settings.py>
WIFI_SSID = "pangalan-ng-wifi"
WIFI_PASSWORD = "password-ng-wfi"
IPV4_ADDRESS = "192.168.1.171"
SUBNET_MASK = "255.255.255.0"
DEFAULT_GATEWAY = "192.168.1.1"
DEFAULT_DNS = "8.8.8.8"
1.2.2) Baguhin ang laman ng settings.py
# iba-iba ang IPV4_ADDRESS ng bawat Pico
1.3) Ang huling file ay main.py
1.3.1) Ang laman ay:
#kuhain sa <main.py>
1.3.2) Baguhin ang laman ng main.py
# iba-iba ang code ng bawat Pico
1st Pico - #kuhain sa <main-1-temperature.py>
2nd Pico - #kuhain sa <main-2-flame.py>
3rd Pico - #kuhain sa <main-3-gas.py>
4th Pico - #kuhain sa <main-4-smoke.py>

E. Gawain (Connection) - Temperature
1) Mag-save ng Table ng Wiring Connection.
2) Tingnan ang label sa board ng components.
# iba-iba ang code ng bawat Pico
Pico >> DS18B20 Temperature
Board29 (GPIO22) >> Out Pin
Board36 (Ground) >> - Pin
Board38 (3V3 Out) >> + Pin
3) Technique: Maghanap ng picture ng components sa Google.
3.1) Raspberry Pi Pico W https://picow.pinout.xyz/
3.2) DS18B20 Sensor Module (randomnerdtutorials.com/raspberry-pi-pico-ds18b20-micropython/)

F. Gawain (Connection) - Flame (Fire)
1) Mag-save ng Table ng Wiring Connection.
2) Tingnan ang label sa board ng components.
# iba-iba ang code ng bawat Pico
Pico >> Flame (Fire)
Board24 (GPIO18) >> D1 Pin
Board25 (GPIO19) >> D2 Pin
Board26 (GPIO20) >> D3 Pin
Board27 (GPIO21) >> D4 Pin
Board29 (GPIO22) >> D5 Pin
Board36 (Ground) >> VCC Pin
Board38 (3V3 Out) >> GND Pin
3) Technique: Maghanap ng picture ng components sa Google.
3.1) Raspberry Pi Pico W https://picow.pinout.xyz/
3.2) Flame (Fire) Sensor Module (srituhobby.com/how-to-use-the-5-way-flame-sensor
-module-with-an-arduino-5-channel-flame-sensor-module-with-arduino/?srsltid
=AfmBOoqSyU1M7e7qWXBo_5UkhEpPm_6SYfFUGwtDjSpe24cLMjVS-T07)






