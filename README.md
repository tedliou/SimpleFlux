# 🚀 SimpleLux

這是一個基於 [iawia002/lux](https://github.com/iawia002/lux) 開發的多平台影音下載工具，目前專注於 **YouTube** 平台的影片下載。此工具提供影片 (.mp4) 與音樂 (.mp3) 兩種下載格式，並擁有一個簡潔的圖形介面。

本專案為 Side Project，以開源形式發布，不作任何營利，歡迎大家自由學習與使用。

### ✨ 主要功能

  * 支援 **YouTube** 影片與音樂下載。
  * 可選擇下載為 `.mp4` 影片格式。
  * 可選擇下載為 `.mp3` 音樂格式 (自動轉檔)。
  * 簡單易用的圖形使用者介面。
  * 開源發布，歡迎學習與貢獻。

-----

## 🛠️ 安裝說明

SimpleLux 提供兩種安裝方式，您可以選擇最適合您的方法：

### 方法一：從原始碼編譯

此方法會自動安裝所有必要的依賴套件並編譯程式，是推薦的安裝方式。

#### 必要依賴

  * [**scoop**](https://scoop.sh/): Windows 套件管理器，用於安裝 `ffmpeg` 和 `go`。
  * **ffmpeg**: 用於影片轉檔。
  * **go**: 用於編譯 Lux 和 SimpleLux。
  * **Git**: 用於克隆 lux 專案。
  * **Python**: 用於執行 `uv` 等腳本。

#### 安裝步驟

1.  克隆此專案。
2.  執行專案目錄下的 `install.bat`。

**※ Scoop 安裝問題**

若您的 Windows 版本較舊，在安裝 Scoop 時可能出現 `Invoke-Expression` 錯誤。您可以安裝 **PowerShell 7** 來解決：

```bash
winget install Microsoft.PowerShell
```

安裝完成後，使用以下指令安裝 Scoop：

```bash
pwsh Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

接著重新執行 `install.bat` 即可。

`install.bat` 執行完成後，SimpleLux 會自動啟動，並在您的 Windows 使用者桌面建立一個捷徑，方便您日後快速啟動。

### 方法二：使用預先編譯好的執行檔

此版本不需編譯，但您必須手動安裝 `ffmpeg` 並設定環境變數。

1.  **安裝 ffmpeg**
    Scoop 仍然是個方便的安裝方式：
    ```bash
    scoop install ffmpeg
    ```
2.  **解壓縮並執行**
    解壓縮下載的檔案，然後直接執行 `SimpleLux.exe` 即可使用。

-----

## ⚙️ 設定檔 (config.json)

SimpleLux 透過 `config.json` 檔案來進行一些基本設定，預設內容如下：

```json
{
    "name": "SimpleLux",
    "version": "1.0.0",
    "window_width": 600,
    "window_height": 250,
    "lux_path": "lux.exe",
    "ffmpeg_path": "ffmpeg",
    "output_path": "outputs"
}
```

  * `name`: 視窗標題名稱。
  * `version`: 程式版本號 (目前無實際作用)。
  * `window_width`: 視窗寬度 (單位為像素)。
  * `window_height`: 視窗高度 (單位為像素)。
  * `lux_path`: Lux 執行檔的路徑。
  * `ffmpeg_path`: FFMPEG 執行檔的路徑。若已透過 Scoop 安裝並設定好環境變數，僅需填寫 `"ffmpeg"` 即可。
  * `output_path`: 下載檔案的儲存資料夾名稱。

-----

## 🖥️ 軟體操作說明

### 啟動程式

  * **從原始碼編譯**: 執行桌面上的 SimpleLux 捷徑。
  * **預先編譯版本**: 直接執行 `SimpleLux.exe`。

### 操作流程

1.  **選擇下載格式**
    在軟體視窗中，選擇您想要的下載格式：**Video** 或 **Music**。

2.  **貼上 YouTube 網址**
    在文字輸入框中，使用 `Ctrl + V` 貼上 YouTube 影片網址。請注意，目前僅支援 `https://www.youtube.com/watch?v=ntIJMS1Jj7c` 這類乾淨的網址，請手動刪除多餘的 `&` 之後的參數。

3.  **按下下載按鈕**
    點擊 **Download** 按鈕開始下載。

      - 程式會自動呼叫 Lux 進行下載。
      - 如果您選擇 **Music** 格式，下載完成後會自動呼叫 FFMPEG 將檔案轉為 `.mp3`。
      - *提示*: 某些影片下載可能會被 Google 阻擋，進度卡住時可嘗試更換 IP 或使用代理伺服器。

4.  **完成**
    下載與轉檔完成後，程式會自動開啟已下載檔案的資料夾，您即可獲得您的 YouTube 媒體檔案。

![](doc/image.png)

-----

## 🤝 如何貢獻

如果您對本專案有任何建議或發現 Bug，歡迎隨時提出 **Issue** 或提交 **Pull Request**。

## 📞 聯絡我們

若有其他問題，請透過 GitHub Issue 聯繫。