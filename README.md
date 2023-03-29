# HW-Proxy-Checker
Script for verifying signal assignments in T3000 non-fail safe HW proxies against HW_assignment_list

## Constraints

- The script in meant to verify assignments only for non-fail safe ET200 modules.

- The script will ignore evaluation of rows which satisfy any of the following criteria. It is the responsibility of the user to check these rows manually as may be needed.
    - "MLFB" field is not defined in config.toml file (MLFBs are defined in 'modules' key in the config file).
    - Empty "KKS" field. Whitespace count as empty.
    - Any character in "change_token" field is '$'.
    - Any string in "change_token" field is 'spare'.
    
- The format for ET200 HW proxy tagname (as used in T3000) is considered as following. Key **tagname_t3k_hw_proxy** defined in the **config.toml** file would need to be modified to handle any change in this naming convention. It is assumed that this tag naming convention is consistent for all non-fail safe ET200 proxies.

    ```
    [tagname_t3k_hw_proxy]
    'format' = 'cabinet + station + "|SLOT " + slot'
    ```
  

## Procedure

1. Set file paths and project specific settings (map between fields of T3000 data and HW_assignment_list) in the file **config.toml**. Further instructures are provided in the **config.toml** file.

2. To run the script -> open **cmd.exe** -> change directory to this folder -> run **main**
