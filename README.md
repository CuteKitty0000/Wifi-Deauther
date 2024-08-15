# Wi-Fi Deauthentication Script

This script automates the process of scanning for Wi-Fi networks and deauthenticating users from a selected wireless network. It is intended for educational purposes only, to understand how wireless security works and the importance of securing your own networks.

## Disclaimer

**This script is for educational purposes only.**  
**Do not use this against any network that you do not own or have explicit permission to test.**  
Unauthorized use of this script could result in severe legal consequences. Always ensure that you have the proper authorization before using this tool on any network.

## Features

- Scans and lists available Wi-Fi networks.
- Allows you to select a target network for deauthentication.
- Automatically deauthenticates users from the selected Wi-Fi network.
- Backs up any existing CSV files in the current directory before creating new ones.

## Prerequisites

To run this script, you need the following:

- A Linux-based OS (Kali Linux is recommended).
- Python 3.x installed.
- Wireless network adapter that supports monitor mode.
- Installed dependencies:
  - `airmon-ng` (part of the Aircrack-ng suite)
  - `iwconfig`

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Cutekitty0000/WiFi-Deauth-Script.git
    cd WiFi-Deauth-Script
    ```

2. **Run the script with sudo privileges:**

    ```bash
    sudo python3 wifi_deauth_script.py
    ```

3. **Follow the on-screen instructions:**

    - The script will scan and list available wireless networks.
    - Select the network you want to target by entering the corresponding number.
    - The script will then attempt to deauthenticate users from that network.

4. **To stop the deauthentication process, press `Ctrl+C`.**

## How It Works

- The script uses `iwconfig` to check for available wireless interfaces.
- It then uses `airodump-ng` to scan for nearby Wi-Fi networks and lists them.
- After selecting a target network, the script utilizes `aireplay-ng` to deauthenticate users from the specified network.

## Important Notes

- Ensure your wireless adapter supports monitor mode.
- Always back up your data before running the script, as it can move existing `.csv` files to a backup directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

**Navaneetha Krishnan M**  
- GitHub: [Cutekitty0000](https://github.com/Cutekitty0000)
- LinkedIn: [Navaneetha Krishnan M](https://in.linkedin.com/in/navaneetha-krishnan-m-8b41b52a1)
