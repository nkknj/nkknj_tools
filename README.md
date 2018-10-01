- pick_files.sh
Usage: pick_files.sh INPUTDIR FILENAME OUTPUTDIR  
INPUTDIR内のFILENAMEと適合するすべてのファイルを、リネームしてOUTPUTDIRにコピーします。  
(例) INPUTDIR/A/B/FILENAMEは、OUTPUTDIR/A_B_FILENAMEとしてコピーされる。

- get_ROI_timeseries.py
Usage: python3 get_ROI_timeseries.py [inputdir] [outputdir]
CONN toolboxによるpreprocessing後の各ROI信号値をCSVファイルで保存します。
[inputdir]: 通常はconn_project/preprocessingを選択。中にあるROI_*.matを処理にかけます。
[outputdir]: 作成したcsvファイルを保存するディレクトリ。
