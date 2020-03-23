def get_frames(signal, size, overlap):
    step = int(size * overlap)
    start = 0
    while start < len(signal) - 1:
        yield signal[start: start + size]
        start += step


signal = [1, 2, 3, 4, 5, 6, 7, 8]
for el in get_frames(signal,4,0.5):
	print(el)