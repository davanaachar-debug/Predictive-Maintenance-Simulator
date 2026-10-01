def detect_faults(data):

    faults = []

    # Temperature
    if data["temperature"] > 80:
        faults.append("CRITICAL: OVER TEMPERATURE")
    elif data["temperature"] > 70:
        faults.append("WARNING: HIGH TEMPERATURE")

    # Vibration
    if data["vibration"] > 6:
        faults.append("CRITICAL: EXCESSIVE VIBRATION")
    elif data["vibration"] > 4.5:
        faults.append("WARNING: HIGH VIBRATION")

    # Current
    if data["current"] > 8:
        faults.append("CRITICAL: OVER CURRENT")
    elif data["current"] > 6:
        faults.append("WARNING: HIGH CURRENT")

    # RPM
    if data["rpm"] < 1200:
        faults.append("CRITICAL: LOW RPM")
    elif data["rpm"] < 1350:
        faults.append("WARNING: LOW RPM")

    if data["rpm"] > 1700:
        faults.append("CRITICAL: EXCESSIVE RPM")
    elif data["rpm"] > 1600:
        faults.append("WARNING: HIGH RPM")

    return faults