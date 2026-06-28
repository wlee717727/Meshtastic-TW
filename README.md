# Meshtastic Apple 繁體中文化版

<p align="center">
  <strong>基於 Meshtastic-Apple 開源專案的繁體中文（台灣）在地化分支</strong><br>
  iOS · iPadOS · macOS · watchOS · visionOS
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL%20v3-blue.svg" alt="License: GPL v3"></a>
  <a href="https://github.com/meshtastic/Meshtastic-Apple">上游專案 Meshtastic-Apple</a>
</p>

---

## 專案來源

本專案**不是**從零開發的原創 App，而是基於 Meshtastic 社群的開源專案 **[Meshtastic-Apple](https://github.com/meshtastic/Meshtastic-Apple)** 修改而來。

- **上游專案**：<https://github.com/meshtastic/Meshtastic-Apple>
- **Meshtastic 官網**：<https://meshtastic.org>
- **原始版權**：Meshtastic 專案及其貢獻者所有

本分支主要貢獻為繁體中文介面、Personal Team 真機安裝相容調整，以及相關錯誤修正；**核心功能、架構與絕大部分程式碼仍來自上游專案**。

---

## 授權

本專案依照上游專案之 **GNU General Public License v3.0（GPL-3.0）** 授權釋出。

- 請保留根目錄的 [`LICENSE`](LICENSE) 檔案
- 請保留原始版權聲明與 GPL-3.0 條款
- 若您再散布或修改本專案，請遵守 GPL-3.0 之義務（包含提供對應原始碼等）

完整授權條文請見 [`LICENSE`](LICENSE)。

---

## 本版本修改內容

相較於上游 Meshtastic-Apple，本分支主要包含：

- **繁體中文（台灣）介面本地化**：更新 `Localizable.xcstrings` 等字串資源，預設顯示繁體中文
- **用語調整**：依台灣使用者習慣調整部分中文翻譯
- **Personal Team 真機安裝相容**：調整簽章與 Bundle Identifier 相關設定，方便使用免費 Apple ID（Personal Team）自行安裝到 iPhone
- **Siri entitlement 防護**：在沒有 Siri capability（例如 Personal Team）時，避免啟動階段因 Siri 授權檢查而崩潰
- **保留原始 Meshtastic 功能架構**：未重新設計 App 導覽或核心功能

> 翻譯工作仍在持續中，部分畫面可能仍顯示英文。歡迎透過 Issue 或 Pull Request 協助改善。

---

## 免責聲明

- 本專案**不是** Meshtastic 官方發行版本，也**不是** App Store 上的官方 Meshtastic App。
- 本專案由社群成員基於開源專案維護，與 Meshtastic 官方無直接發行關係。
- 如需官方版本、最新功能說明或支援管道，請以 [Meshtastic-Apple 上游專案](https://github.com/meshtastic/Meshtastic-Apple) 或 [Meshtastic 官網](https://meshtastic.org) 為準。
- 使用本專案安裝到手機上的版本，風險與責任由使用者自行承擔。

---

## 官方版本聲明

本專案不是 Meshtastic 官方發行版本，而是基於 Meshtastic-Apple 開源專案建立的繁體中文（台灣）在地化分支。

若您需要官方穩定版本，建議使用：

- Meshtastic 官方 GitHub Repository
- Meshtastic 官方 App Store 發行版本

本專案主要提供繁體中文使用者參考、學習、測試與社群交流使用。

---

## 安裝方式（安裝到自己的 iPhone）

由於 iOS 的安全機制，您**無法**像下載一般檔案一樣直接安裝 `.ipa`。請使用 **Xcode** 自行編譯並安裝到已連接的 iPhone。

### 需求

- macOS 與 [Xcode](https://developer.apple.com/xcode/)（建議使用較新版本）
- 已登入的 **Apple ID**（免費帳號即可使用 Personal Team）
- iPhone 與 USB 傳輸線（或已設定好的無線偵錯）
- 建議 iOS 版本與上游 Meshtastic-Apple 要求相符

### 步驟

1. **下載專案**

   ```sh
   git clone --recursive https://github.com/wlee717727/Meshtastic-TW.git
   cd Meshtastic-TW
   ```

   若已 clone 但未初始化子模組：

   ```sh
   git submodule update --init --recursive
   ```

2. **用 Xcode 開啟專案**

   ```sh
   open Meshtastic.xcworkspace
   ```

   > 請開啟 `Meshtastic.xcworkspace`，不要只開 `.xcodeproj`。

3. **設定簽章（Signing & Capabilities）**

   在 Xcode 左側選擇 **Meshtastic** target（以及需要的 **WidgetsExtension**、**Meshtastic Watch App** 等 target），於 **Signing & Capabilities**：

   - 勾選 **Automatically manage signing**
   - **Team** 選擇您自己的 Apple ID / 開發團隊
   - **請勿使用他人的開發者帳號或憑證**

4. **修改 Bundle Identifier**

   將 Bundle Identifier 改成**您自己擁有、且全域唯一**的名稱，例如：

   - 主 App：`com.yourname.MeshtasticTW`
   - Widget 擴充：`com.yourname.MeshtasticTW.Widgets`
   - Watch App：`com.yourname.MeshtasticTW.watchkitapp`

   各 target 的 Bundle Identifier 需彼此一致、且符合階層關係，否則簽章會失敗。

5. **連接 iPhone 並選擇實機**

   - 用 USB 連接 iPhone 並解鎖
   - 在 Xcode 上方執行目標選單中，選擇您的 iPhone（不要選 Simulator）

6. **Build & Run**

   - 選擇 **Meshtastic** scheme
   - 按 **Run（▶）** 編譯並安裝到手機

7. **首次安裝：信任開發者（若系統提示）**

   若 iPhone 顯示「未受信任的開發者」，請到：

   **設定 → 一般 → VPN 與裝置管理**（或「裝置管理」）

   找到您的 Apple ID / 開發者名稱，點選 **信任**。

8. **（選用）設定 Git Hooks**

   若您要參與開發，可執行：

   ```sh
   ./scripts/setup-hooks.sh
   ```

### Personal Team 注意事項

使用免費 Apple ID（Personal Team）時，部分 Apple 能力（例如 **Siri**）可能無法啟用。本分支已針對此情況做啟動保護，但**不保證**所有上游功能在 Personal Team 下皆可用。若需完整能力，請使用付費 Apple Developer Program 帳號。

---

## 關於 iOS 簽名

Apple 要求所有 iOS App 必須經過簽章才能安裝到實機。因此：

| 方式 | 說明 |
|------|------|
| **自行用 Xcode 編譯安裝** | 最常見的開源 App 使用方式；需自己的 Apple ID |
| **TestFlight / App Store** | 需由具備發行資格的開發者帳號上架 |

本專案：

- **不提供**任何個人的 Apple Developer Team ID
- **不提供**任何簽名憑證、描述檔或 `.ipa` 下載
- **不承諾**代為簽章或代為上架

請一律使用**您自己的 Apple ID** 在 Xcode 中完成簽章與安裝。

---

## Apple 簽名與安裝說明

由於 Apple 的安全機制，iOS App 必須經過 Apple Developer 簽名才能安裝至 iPhone 或 iPad。

因此，本 Repository **不提供**：

- Apple Developer 憑證（Certificates）
- Provisioning Profiles
- Team ID
- 私人簽名檔

若要安裝本專案，請：

1. Clone 或下載本 Repository
2. 使用 Xcode 開啟專案
3. 使用自己的 Apple ID / Apple Developer Team
4. 修改 Bundle Identifier
5. Build & Run 至自己的裝置

本專案僅提供完整原始碼，所有使用者需自行完成 Apple 簽名流程。

---

## 語言與介面

本分支預設強制顯示 **繁體中文（台灣）** 介面，即使 iPhone 系統語言為 English。

目前**尚未**提供 App 內語言切換器；若未來加入，將另行說明。

---

## 貢獻

歡迎透過 [GitHub Issues](https://github.com/wlee717727/Meshtastic-TW/issues) 或 Pull Request：

- 改善繁體中文翻譯
- 回報錯字、用語或漏翻
- 提出 Personal Team / 簽章相關問題

若修改程式碼並再散布，請遵守 **GPL-3.0** 授權義務。

上游專案的一般貢獻規範可參考 [Meshtastic-Apple Contributing](https://github.com/meshtastic/Meshtastic-Apple)。

---

## 相關連結

| 資源 | 連結 |
|------|------|
| 本專案（繁中分支） | <https://github.com/wlee717727/Meshtastic-TW> |
| 上游 Meshtastic-Apple | <https://github.com/meshtastic/Meshtastic-Apple> |
| Meshtastic 使用者文件 | <https://meshtastic.github.io/Meshtastic-Apple/> |
| Meshtastic 官網 | <https://meshtastic.org> |
| GPL-3.0 授權全文 | [`LICENSE`](LICENSE) |

---

## English Summary

This repository is a **Traditional Chinese (Taiwan) localization fork** of the upstream open-source project **[Meshtastic-Apple](https://github.com/meshtastic/Meshtastic-Apple)**. It is **not** an official Meshtastic release and **not** an original app built from scratch.

**License:** GPL-3.0 — see [`LICENSE`](LICENSE). Please retain the license and copyright notices.

**Main changes in this fork:** zh-Hant-TW UI localization, Personal Team signing compatibility, and startup guards when Siri entitlement is unavailable.

**Installation:** Clone the repo (with submodules), open `Meshtastic.xcworkspace` in Xcode, set your own Apple ID team, change Bundle Identifiers, connect your iPhone, then Build & Run. iOS apps cannot be installed like ordinary files; you must sign the app with your own Apple ID. This project does not provide any developer certificates or team IDs.

**Contributions:** Issues and pull requests are welcome, especially for translation improvements.

---

<p align="center">
  基於 <a href="https://github.com/meshtastic/Meshtastic-Apple">Meshtastic-Apple</a> ·
  <a href="https://meshtastic.org">meshtastic.org</a> ·
  <a href="LICENSE">GPL-3.0</a>
</p>
