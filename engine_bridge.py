# ==========================================================
#  ENGINE BRIDGE MODULE
#  INTERNAL USE ONLY
# ==========================================================

import time

_ENGINE_STATUS = "IDLE"

def connect_engine():
    global _ENGINE_STATUS
    _ENGINE_STATUS = "CONNECTED"
    time.sleep(0.2)
    return True

def disconnect_engine():
    global _ENGINE_STATUS
    _ENGINE_STATUS = "DISCONNECTED"
    return True

def engine_status():
    return _ENGINE_STATUS