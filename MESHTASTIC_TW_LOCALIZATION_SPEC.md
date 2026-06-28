# MESHTASTIC_TW_LOCALIZATION_SPEC.md

# Meshtastic-TW 全專案繁體中文化最終規格

## 任務

你是一位資深 Apple Platform / SwiftUI / Localization Engineer。

請完整分析 **整個
Repository**，完成所有使用者可見文字的繁體中文（台灣）在地化。

不要詢問。 不要分批。 不要停止。 直接完成全部工作。

------------------------------------------------------------------------

## 第一階段：完整掃描（不得修改）

先建立 Repository 索引：

-   所有 Swift
-   所有 Localizable.strings
-   所有 Localizable.xcstrings
-   所有 \*.strings
-   InfoPlist.strings
-   Info.plist 權限說明
-   SwiftUI
-   UIKit
-   Widget
-   watchOS
-   macOS
-   MenuBar
-   Toolbar
-   Alert
-   Sheet
-   ConfirmationDialog
-   ContextMenu
-   Navigation
-   Tab
-   Button
-   Label
-   Text
-   Toggle
-   Picker
-   Placeholder
-   Empty State
-   Search
-   Permission
-   Accessibility
-   Notification
-   Markdown
-   README（僅使用者文件）

建立完成後再開始修改。

------------------------------------------------------------------------

## 第二階段：翻譯

將所有使用者可見英文翻譯為：

**繁體中文（台灣）**

要求：

-   Apple HIG 用語
-   自然
-   專業
-   一致
-   禁止簡體
-   禁止中國用語
-   禁止香港用語

------------------------------------------------------------------------

## 固定翻譯

Node → 節點 Nodes → 節點 Channel → 頻道 Device → 裝置 Devices → 裝置
Region → 地區 Position → 位置 Location → 定位 Waypoint → 路徑點
Traceroute → 路由追蹤 Telemetry → 遙測 Packet → 封包 Signal → 訊號
Connect → 連線 Reconnect → 重新連線 Disconnect → 中斷連線 Connected →
已連線 Disconnected → 未連線 Connecting → 連線中 Import → 匯入 Export →
匯出 Backup → 備份 Restore → 還原 Factory Reset → 回復原廠設定 Settings
→ 設定 About → 關於 Messages → 訊息 Map → 地圖 Search → 搜尋 Filter →
篩選 Save → 儲存 Cancel → 取消 Delete → 刪除 Edit → 編輯 Share → 分享
Reply → 回覆 Loading → 載入中... Unknown → 未知 Enabled → 已啟用
Disabled → 已停用 Offline → 離線 Online → 在線 Firmware → 韌體

------------------------------------------------------------------------

## 不翻譯

Meshtastic LoRa MQTT GPS BLE Bluetooth LE Wi‑Fi iOS macOS watchOS Apple
GitHub UUID API JSON Swift SwiftUI Codable

------------------------------------------------------------------------

## Localizable

優先使用既有：

-   Localizable.xcstrings
-   Localizable.strings
-   NSLocalizedString
-   String(localized:)

不要新增更多硬編碼 UI 字串。

若發現硬編碼且已有本地化架構，請整理進本地化系統。

------------------------------------------------------------------------

## 嚴禁修改

不得修改：

-   功能
-   ViewModel
-   Model
-   Networking
-   BLE
-   MQTT
-   LoRa
-   Database
-   API
-   Protocol
-   Struct
-   Enum
-   Build Settings
-   Bundle Identifier
-   Entitlements
-   Layout
-   Spacing
-   Constraints
-   Animation
-   Colors
-   Icons
-   Navigation Flow

除了翻譯，不得更動任何邏輯。

------------------------------------------------------------------------

## 品質要求

若發現：

-   重複翻譯
-   用詞不一致
-   漏翻
-   本地化遺漏

請直接修正並統一。

------------------------------------------------------------------------

## 完成後

1.  Build 專案並修正翻譯造成的問題。
2.  再次掃描整個 Repository。
3.  確認所有使用者可見英文皆已翻譯。

------------------------------------------------------------------------

## 最終回報

-   修改檔案清單
-   翻譯統計
-   Build 成功
-   功能未修改
-   UI 未修改
-   所有使用者可見文字已完成繁體中文化
