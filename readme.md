# Screensaver Toggle

This Python script provides a simple graphical interface to toggle the screensaver on and off in a Linux Mint Cinnamon environment. It uses GTK and AppIndicator3 libraries to create a system tray icon that allows the user to enable or disable the screensaver with a click.

![Peek 2023-06-11 12-35](https://github.com/Gk1mtd/Teainit/assets/15696019/01bc4ebf-e3f3-48fc-9235-a8a3fe7edfc5)

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3
- gi package (provides the Python bindings for GTK and AppIndicator3 libraries)

## Installation

1. Clone the repository or download the script file `screensaver_toggle.py` to your local machine.
2. install required packages: ```bash
sudo apt-get install python3 python3-gi gir1.2-gtk-3.0 gir1.2-appindicator3-0.1
```
3. Open a terminal and navigate to the directory where the script is located.
4. Add it to your Start Applications, if you want

## Usage

To run the script, execute the following command in the terminal:

```shell
python3 screensaver_toggle.py
```

Once the script is running, you will see a system tray icon appear. Clicking on the icon will show the menu, to toggle the screensaver on or off. When the toggle is enabled, the system will not go into screensaver mode. teainit will change the screensaver time to "never". When the toggle is disabled, the screensaver time will set to 15 minutes.

To quit the script, right-click on the system tray icon and select "Quit" from the menu.

## Notes

- This script assumes a Linux environment with the Cinnamon desktop environment. If you are using a different desktop environment, you may need to modify the `org.cinnamon.desktop.session` value in the `toggle_screensaver` function.
- The script saves a placeholder image (`teeinit.png`) in the `/tmp` directory. You can replace this image with your own icon by modifying the `save_image_to_file` function.
- The script requires appropriate permissions to modify the screensaver settings. Make sure you have the necessary privileges to run the `gsettings` commands. Might work for any user though.
