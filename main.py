__author__      = "Nandan Sharma"


"""
Constraints:

1. The script in meant to verify assignments only for non-fail safe ET200 modules.

2. The script will ignore evaluation of rows which satisfy any of the following criteria.
   It is the responsibility of the user to check these rows manually as may be needed.
       2.1. "MLFB" field is not defined in p4.toml config file (check entries in list "mlfb")
       2.2. Empty "KKS" field. Whitespace count as empty.
       2.3. Any character in "change_token" field is '$'.

3. The format for ET200 HW proxy tagname (as used in T3000) is considered as following:
       prefix + cabinet + station + "|SLOT " + slot    (eg. 51CPA01FB|SLOT 27) 
   Key 'tagname_t3k_hw_proxy_format' of the config.toml file would need to be modified to handle any change in this naming convention.
   It is assumed that this tag naming convention is consistent for all non-fail safe ET200 proxies.

"""


from utils import hwProxyChecker
hwProxyChecker.write_diff()