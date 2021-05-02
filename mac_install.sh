#!/bin/bash
echo "Checking for mac-10.11"
COMMAND_RESULT=$(echo "$(command -v sw_vers >&/dev/null && echo "macOS `sw_vers -productVersion`" 2>/dev/null)")
echo "$COMMAND_RESULT" | grep -q "macOS[[:space:]]10\.11"
OS_MATCH=$?
if [[ $OS_MATCH -eq "0" ]]; then
  installer -pkg ./TaniumClient-7.4.4.1362.pkg -target /
  if [[ "$?" -eq "0" ]]; then
    echo "Installation successful. Copying tanium-init.dat."
    cp ./tanium-init.dat /Library/Tanium/TaniumClient/
    echo "Starting service."
    launchctl load /Library/LaunchDaemons/com.tanium.taniumclient.plist
  else
    echo "Install failed."
  fi
  exit
fi
echo "Checking for mac-10.11"
COMMAND_RESULT=$(echo "$(command -v sw_vers >&/dev/null && echo "macOS `sw_vers -productVersion`" 2>/dev/null)")
echo "$COMMAND_RESULT" | grep -q "macOS[[:space:]]10\.12"
OS_MATCH=$?
if [[ $OS_MATCH -eq "0" ]]; then
  installer -pkg ./TaniumClient-7.4.4.1362.pkg -target /
  if [[ "$?" -eq "0" ]]; then
    echo "Installation successful. Copying tanium-init.dat."
    cp ./tanium-init.dat /Library/Tanium/TaniumClient/
    echo "Starting service."
    launchctl load /Library/LaunchDaemons/com.tanium.taniumclient.plist
  else
    echo "Install failed."
  fi
  exit
fi
echo "Checking for mac-10.11"
COMMAND_RESULT=$(echo "$(command -v sw_vers >&/dev/null && echo "macOS `sw_vers -productVersion`" 2>/dev/null)")
echo "$COMMAND_RESULT" | grep -q "macOS[[:space:]]10\.13"
OS_MATCH=$?
if [[ $OS_MATCH -eq "0" ]]; then
  installer -pkg ./TaniumClient-7.4.4.1362.pkg -target /
  if [[ "$?" -eq "0" ]]; then
    echo "Installation successful. Copying tanium-init.dat."
    cp ./tanium-init.dat /Library/Tanium/TaniumClient/
    echo "Starting service."
    launchctl load /Library/LaunchDaemons/com.tanium.taniumclient.plist
  else
    echo "Install failed."
  fi
  exit
fi
echo "Checking for mac-10.11"
COMMAND_RESULT=$(echo "$(command -v sw_vers >&/dev/null && echo "macOS `sw_vers -productVersion`" 2>/dev/null)")
echo "$COMMAND_RESULT" | grep -q "macOS[[:space:]]10\.14"
OS_MATCH=$?
if [[ $OS_MATCH -eq "0" ]]; then
  installer -pkg ./TaniumClient-7.4.4.1362.pkg -target /
  if [[ "$?" -eq "0" ]]; then
    echo "Installation successful. Copying tanium-init.dat."
    cp ./tanium-init.dat /Library/Tanium/TaniumClient/
    echo "Starting service."
    launchctl load /Library/LaunchDaemons/com.tanium.taniumclient.plist
  else
    echo "Install failed."
  fi
  exit
fi
echo "Checking for mac-10.11"
COMMAND_RESULT=$(echo "$(command -v sw_vers >&/dev/null && echo "macOS `sw_vers -productVersion`" 2>/dev/null)")
echo "$COMMAND_RESULT" | grep -q "macOS[[:space:]]10\.15"
OS_MATCH=$?
if [[ $OS_MATCH -eq "0" ]]; then
  installer -pkg ./TaniumClient-7.4.4.1362.pkg -target /
  if [[ "$?" -eq "0" ]]; then
    echo "Installation successful. Copying tanium-init.dat."
    cp ./tanium-init.dat /Library/Tanium/TaniumClient/
    echo "Starting service."
    launchctl load /Library/LaunchDaemons/com.tanium.taniumclient.plist
  else
    echo "Install failed."
  fi
  exit
fi
echo "Checking for mac-10.11"
COMMAND_RESULT=$(echo "$(command -v sw_vers >&/dev/null && echo "macOS `sw_vers -productVersion`" 2>/dev/null)")
echo "$COMMAND_RESULT" | grep -q "macOS[[:space:]]11\.\d+"
OS_MATCH=$?
if [[ $OS_MATCH -eq "0" ]]; then
  installer -pkg ./TaniumClient-7.4.4.1362.pkg -target /
  if [[ "$?" -eq "0" ]]; then
    echo "Installation successful. Copying tanium-init.dat."
    cp ./tanium-init.dat /Library/Tanium/TaniumClient/
    echo "Starting service."
    launchctl load /Library/LaunchDaemons/com.tanium.taniumclient.plist
  else
    echo "Install failed."
  fi
  exit
fi