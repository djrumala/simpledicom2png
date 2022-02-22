# simpledicom2png
This is a simple python program to convert DICOM images to png format

1. Tekan Win + R
2. Ketik Cmd, tekan Enter. Command Prompt (Cmd) akan dibuka
3. Extract script.zip ke folder 'script' di folder 'Downloads'. Lalu buka folder 'script' tersebut.
4. Pada Cmd, ketik:
cd <path folder script>
contoh: cd C:\Users\Brain\Downloads\\script
5. [path folder script] didapatkan dengan mengcopy paste path script ke Cmd
6. Ketik ".\env\Scripts\Activate.bat" (tidak perlu tanda kutip)
7. Copy path folder data dicom
8. Pada Cmd, ketik
python convert.py '"<path folder>"' <tipe_gambar=[hitam/putih]>
Contoh -> python convert.py '"D:\Projects\Companies\Convert\data"' hitam (Perhatikan path folder diawali dan diakhiri oleh kutip satu + kutip dua)
9. Gambar akan muncul pada folder 'png' di dalam folder 'script'
