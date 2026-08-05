def check_heatwave(temp):
    if temp >= 40:
        return "High"
    elif temp >= 35:
        return "Moderate"
    else:
        return "Low"
