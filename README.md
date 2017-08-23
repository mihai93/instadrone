# instadrone

To run the drone, `python drone.py`

To run from SSH, run the following command before,
```
export DISPLAY=:0.0
```

## Dependencies
All are set to download in script.sh except for pyautogui, run:
```bash
sudo -s -H pyautogui
```

### To get shared folders working:
```bash
vagrant plugin install vagrant-vbguest
vagrant vbguest --do install
vagrant reload
vagrant vbguest --status -> should be ok
```