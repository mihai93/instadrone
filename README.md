# instadrone

To run the drone, `python drone.py`

## Dependencies
All are set to download in script.sh except for pyautogui, run:
```sudo -s -H pyautogui```

### To get shared folders working:
```vagrant plugin install vagrant-vbguest
vagrant vbguest --do install
vagrant reload
vagrant vbguest --status -> should be ok```