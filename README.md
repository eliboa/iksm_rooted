# iksm_rooted
Python script to extract iksm_session from Android rooted device through SSH.

## How to get your iksm_session
This is only for Android ROOTED device.
The iksm_session token can be found in the following file : /data/data/com.nintendo.znca/app_webview/Cookies

This Python script simply extract the token from this file through SHH connection. Just set your ip, username and password before executing.

## Use / Related
iksm_session token can be used to access the Splatnet API (Splatoon 2).

* [NintendoSwitchRESTAPI](https://github.com/ZekeSnider/NintendoSwitchRESTAPI) Reverse engineered REST API used in the Nintendo Switch app for iOS. Includes documentation on Splatoon 2's API.
* [stat.ink](https://github.com/fetus-hina/stat.ink) 
* [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink)
