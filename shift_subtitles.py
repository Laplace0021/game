import pysrt

def shift_subtitles(file_path, shift_ms):
    subs = pysrt.open(file_path)
    subs.shift(milliseconds=shift_ms)
    subs.save('output.srt', encoding='utf-8')

# Mengubah semua subtitle 20 detik lebih lambat
shift_subtitles('your_file.srt', 20000)
