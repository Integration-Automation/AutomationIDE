結構化審查
=======================================================

在所選 Python 直譯器安裝目前的 prthinker 套件與對應 JEditor 轉接器。使用 prthinker 選單審查已存檔檔案，結果顯示於 Problems，亦可取消進行中的審查。問題提供 Quick Fix 建議，狀態列顯示進度與終止狀態。審查使用持續運作的隔離 JSONL 子行程，Git 差異在背景準備。設定與憑證透過環境變數傳遞；儲存或發布前請測試並核准建議。

JEditor 使用 Plugins → prthinker；PyBreeze 使用 Automation → prthinker → 在 Problems 審查。取消動作會要求工作進入終止狀態。兩個編輯器變更須一起安裝；共用轉接器採協定版本 1。審查動作不會建立 PR。
