# instadrone

To run the drone, `python drone.py`

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
vagrant vbguest --status <b>-> should be ok</b>
```