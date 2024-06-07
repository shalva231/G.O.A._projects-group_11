def data_reverse(data):
    segments = []
    for i in range(0, len(data), 8):
        segment = data[i:i+8]
        segments.append(segment)

    segments.reverse()
    
    reversed_data = []
    for segment in segments:
        for bit in segment:
            reversed_data.append(bit)
    
    return reversed_data