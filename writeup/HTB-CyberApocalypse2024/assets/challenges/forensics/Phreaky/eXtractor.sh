#!/bin/bash
# sudo apt install 7zip

zip=('SecureFile.zip' 'SecureFile[1].zip' 'SecureFile[2].zip' 'SecureFile[3].zip' 'SecureFile[4].zip' 'SecureFile[5].zip' 'SecureFile[6].zip' 'SecureFile[7].zip' 'SecureFile[8].zip' 'SecureFile[9].zip' 'SecureFile[10].zip' 'SecureFile[11].zip' 'SecureFile[12].zip' 'SecureFile[13].zip' 'SecureFile[14].zip')

passwords=('S3W8yzixNoL8' 'r5Q6YQEcGWEF' 'TVm9aC1UycxF' 'jISlbC8145Ox' 'AdtJYhF4sFgv' 'j2SRRDraIvUZ' 'xh161WSXX7tB' 'yH5vqnkm7Ixa' 'tJPUTUfceO1P' '2qKlZHZlBPQz' 'mbkUvLZ1koxu' 'ZN4yKAYrtf8x' '0eA143t4432M' 'oea41WCJrWwN' 'gdOvbPtB0xCK')

for i in "${!zip[@]}"
	do
		7z x ${zip[$i]} -p${passwords[$i]}
	done
