#!/usr/bin/env python3
"""Apply zh-Hant-TW translations to Localizable.xcstrings for Meshtastic-TW."""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
XCSTRINGS = REPO_ROOT / "Localizable.xcstrings"

# Simplified → Traditional (Taiwan) overrides for zh-Hans fallback
HANS_TO_TW = {
    "蓝牙": "Bluetooth",
    "类别": "類別",
    "回显": "回音",
    "加载中": "載入中",
    "节点核心数据备份": "節點核心資料備份",
    "点": "接腳",
    "pin": "接腳",
    "角色": "角色",
    "将": "將",
    "发送给": "傳送給",
    "传感器": "感測器",
    "系列": "系列",
    "信噪比": "SNR",
}

# Spec glossary + manual translations for missing English strings
TRANSLATIONS: dict[str, str] = {
    "700 bps": "700 bps",
    "700B bps": "700B bps",
    "1200 bps": "1200 bps",
    "1300 bps": "1300 bps",
    "1400 bps": "1400 bps",
    "1600 bps": "1600 bps",
    "2400 bps": "2400 bps",
    "3200 bps": "3200 bps",
    "A status message that is broadcast to the mesh. Other nodes will see this status in the node list.": "廣播至網狀網路的狀態訊息。其他節點會在節點列表中看到此狀態。",
    "Active Database": "使用中資料庫",
    "Address Mode": "位址模式",
    "Air Quality Metrics Enabled": "已啟用空氣品質遙測",
    "Air Quality Sensor Options": "空氣品質感測器選項",
    "An admin key must be set before enabling managed mode.": "啟用管理模式前必須先設定管理員金鑰。",
    "Analyze Current Preset": "分析目前預設值",
    "Analyze only your radio's current preset, seeded with everything already collected — every node heard, per-node message and sensor counts, and RF health including noise floor — so the run starts from your full history rather than an empty scan. Stop anytime to view the summary.": "僅分析您無線電的目前預設值，並以已收集的所有資料為基礎——包含聽到的每個節點、各節點訊息與感測器計數，以及含噪聲底限的 RF 健康狀態——讓掃描從完整歷史記錄開始，而非空白掃描。可隨時停止以檢視摘要。",
    "Application Support": "應用程式支援",
    "Audio": "音訊",
    "Audio Config": "音訊設定",
    "Backup Failed": "備份失敗",
    "Backup Management": "備份管理",
    "Backup Now": "立即備份",
    "Bad Rx": "錯誤接收",
    "Bitrate": "位元率",
    "BLE Threshold": "BLE 閾值",
    "Busy Floor (-85 dBm)": "忙碌底限（-85 dBm）",
    "Canceled": "已取消",
    "Clears all active contact filters.": "清除所有使用中的聯絡人篩選條件。",
    "Clears all active node filters.": "清除所有使用中的節點篩選條件。",
    "Codec2 Enabled": "已啟用 Codec2",
    "Codec2 Settings": "Codec2 設定",
    "Collapsed": "已收合",
    "Community supported Linux device.": "社群支援的 Linux 裝置。",
    "Compass Orientation": "羅盤方向",
    "Count": "計數",
    "Created by": "建立者",
    "Current Preset": "目前預設值",
    "dBm": "dBm",
    "Delete all local stats?": "刪除所有本機統計資料？",
    "Delete Backup?": "刪除備份？",
    "Device Links": "裝置連結",
    "DHCP": "DHCP",
    "Direct Response": "直接回應",
    "DNS": "DNS",
    "Documents": "文件",
    "Double tap to collapse": "點兩下以收合",
    "Double tap to expand": "點兩下以展開",
    "Drop redundant position broadcasts from the same node.": "捨棄來自同一節點的重複位置廣播。",
    "Drop Unknown": "捨棄未知",
    "Dupes": "重複",
    "Enable Codec2 audio encoding/decoding for voice communication over the mesh.": "啟用 Codec2 音訊編解碼，以在網狀網路上進行語音通訊。",
    "Enable dropping of unknown/undecryptable packets.": "啟用捨棄未知／無法解密的封包。",
    "Enable neighbor info broadcasting. Periodically sends information about directly-heard neighbors to help visualize mesh topology.": "啟用鄰居資訊廣播。定期傳送直接聽到的鄰居資訊，以協助視覺化網狀網路拓撲。",
    "Enable per-node rate limiting to throttle chatty nodes.": "啟用各節點速率限制，以節流過於頻繁的節點。",
    "Expanded": "已展開",
    "Gateway": "閘道",
    "GPIO Configuration": "GPIO 設定",
    "Hide node filters": "隱藏節點篩選",
    "Hide password": "隱藏密碼",
    "Hides the node filter options.": "隱藏節點篩選選項。",
    "Hops": "跳數",
    "How often air quality metrics are sent out over the mesh. Default is 30 minutes.": "空氣品質遙測透過網狀網路傳送的頻率。預設為 30 分鐘。",
    "How often to broadcast neighbor info. Default is 4 hours.": "廣播鄰居資訊的頻率。預設為 4 小時。",
    "How to read it": "如何解讀",
    "I want one": "我想要一個",
    "I2S data in pin.": "I2S 資料輸入接腳。",
    "I2S DIN": "I2S DIN",
    "I2S SCK": "I2S SCK",
    "I2S SD": "I2S SD",
    "I2S serial clock pin.": "I2S 序列時鐘接腳。",
    "I2S serial data pin.": "I2S 序列資料接腳。",
    "I2S word select pin.": "I2S 字選接腳。",
    "I2S WS": "I2S WS",
    "Ignore": "忽略",
    "Indicates how to rotate or invert the compass output for accurate display.": "指示如何旋轉或反轉羅盤輸出，以正確顯示。",
    "IP": "IP",
    "Last updated by": "最後更新者",
    "Latest": "最新",
    "Licensed band": "執照頻段",
    "Live": "即時",
    "LIVE": "即時",
    "Live view of mesh packets crossing the network. Overrides the category and level filters below.": "網狀網路封包穿越網路的即時檢視。會覆寫下方的類別與層級篩選。",
    "Local Stats": "本機統計",
    "Local Stats Log": "本機統計記錄",
    "Local Stats Requested": "已要求本機統計",
    "Location": "定位",
    "Lower values usually mean a quieter receiver environment.": "數值較低通常表示接收環境較安靜。",
    "Master enable for the traffic management module.": "流量管理模組的主開關。",
    "Max Hops": "最大跳數",
    "Max Packets": "最大封包數",
    "Max Transmit Power": "最大發射功率",
    "Maximum hop distance from the requestor at which direct NodeInfo responses are served from the local cache.": "從請求者起算，可從本機快取直接回應 NodeInfo 的最大跳數距離。",
    "Maximum packets allowed per node within the rate limit window.": "速率限制時間窗內，每個節點允許的最大封包數。",
    "Maximum unknown/undecryptable packets per rate window before the source is dropped.": "在捨棄來源前，每個速率時間窗內允許的未知／無法解密封包上限。",
    "meshtastic.pool.ntp.org": "meshtastic.pool.ntp.org",
    "Min Interval (s)": "最小間隔（秒）",
    "Minimum interval in seconds between position updates from the same node.": "同一節點位置更新的最小間隔（秒）。",
    "Mute notifications": "靜音通知",
    "Neighbor Info": "鄰居資訊",
    "Neighbor Info Config": "鄰居資訊設定",
    "Network Servers": "網路伺服器",
    "No backups available": "沒有可用的備份",
    "No Local Stats": "沒有本機統計",
    "No Reading": "沒有讀數",
    "Node Backups": "節點備份",
    "NodeInfo Direct Response": "NodeInfo 直接回應",
    "Nodes Online": "在線節點",
    "Noise": "噪聲",
    "Noise Floor": "噪聲底限",
    "Noise Floor Info": "噪聲底限資訊",
    "Noise Floor No Reading": "噪聲底限無讀數",
    "NTP Server": "NTP 伺服器",
    "Open in Maps": "在地圖中開啟",
    "Packet Stream": "封包串流",
    "Packets": "封包",
    "Packets Rx": "接收封包",
    "Packets Tx": "傳送封包",
    "Position Dedup": "位置去重",
    "Position Deduplication": "位置去重",
    "PTT Pin": "PTT 接腳",
    "Push-to-talk GPIO pin number.": "按鍵發話 GPIO 接腳編號。",
    "Rate Limiting": "速率限制",
    "Readings can vary quickly with nearby transmitters, antenna setup, filters, and local interference.": "讀數可能因附近發射器、天線設定、濾波器與本地干擾而快速變化。",
    "Relayed": "已轉發",
    "Request Local Stats": "要求本機統計",
    "Reset contact filters": "重設聯絡人篩選",
    "Reset node database and favorites?": "重設節點資料庫與我的最愛？",
    "Reset node database, preserving favorites?": "重設節點資料庫（保留我的最愛）？",
    "Reset node filters": "重設節點篩選",
    "Resetting…": "重設中…",
    "Respond to NodeInfo requests directly from local cache.": "直接從本機快取回應 NodeInfo 要求。",
    "Restore Failed": "還原失敗",
    "Restoring Backup": "還原備份中",
    "RSSI threshold for BLE device counting. Default is −80 dBm.": "BLE 裝置計數的 RSSI 閾值。預設為 −80 dBm。",
    "RSSI threshold for WiFi device counting. Default is −80 dBm.": "Wi-Fi 裝置計數的 RSSI 閾值。預設為 −80 dBm。",
    "Rsyslog Server": "Rsyslog 伺服器",
    "Scrolls the chart to the newest reading": "將圖表捲動至最新讀數",
    "Seconds": "秒",
    "Server:Port": "伺服器：連接埠",
    "Show node filters": "顯示節點篩選",
    "Show password": "顯示密碼",
    "Shows the node filter options.": "顯示節點篩選選項。",
    "Static": "靜態",
    "Static IPv4 Configuration": "靜態 IPv4 設定",
    "Status Message": "狀態訊息",
    "Status Message Config": "狀態訊息設定",
    "Subnet": "子網路",
    "Switching Radio": "切換無線電",
    "The audio sample rate to use for Codec2. Lower bitrates use less bandwidth but reduce audio quality.": "Codec2 使用的音訊取樣率。較低位元率使用較少頻寬，但會降低音質。",
    "The red reference line marks a busy -85 dBm floor, not a hard failure threshold.": "紅色參考線標示忙碌時的 -85 dBm 底限，並非硬性故障閾值。",
    "Threshold": "閾值",
    "Time window in seconds for rate limiting calculations.": "速率限制計算的時間窗（秒）。",
    "Timestamps": "時間戳記",
    "Total Backup Storage": "備份儲存空間總計",
    "Traffic Management": "流量管理",
    "Traffic Management Config": "流量管理設定",
    "Translate Documentation": "翻譯文件",
    "Transmit over LoRa": "透過 LoRa 傳送",
    "Unknown Packet Handling": "未知封包處理",
    "Unmute": "取消靜音",
    "Using your connected device's position": "使用您已連線裝置的位置",
    "Visible Range": "可見範圍",
    "Waiting for packets…": "等待封包中…",
    "Whether to transmit neighbor info over LoRa in addition to MQTT and PhoneAPI. Not available on channels with default key and name.": "是否除了 MQTT 與 PhoneAPI 外，也透過 LoRa 傳送鄰居資訊。使用預設金鑰與名稱的頻道不適用。",
    "WiFi Threshold": "Wi-Fi 閾值",
    "Window (s)": "時間窗（秒）",
    "Meshtastic® Copyright Meshtastic LLC": "Meshtastic® 版權所有 Meshtastic LLC",
    # Info.plist permission strings
    "We use NFC tags to share node contacts": "我們使用 NFC 標籤來分享節點聯絡人",
    "We use bluetooth to connect to nearby Meshtastic Devices": "我們使用 Bluetooth 連線至附近的 Meshtastic 裝置",
    "Bluetooth is used to connect an iPhone to a user's meshtastic device to allow text messaging and location data for the mesh network.": "Bluetooth 用於將 iPhone 連線至使用者的 Meshtastic 裝置，以在網狀網路上傳送訊息與定位資料。",
    "We use the camera to share channels using a QR Code": "我們使用相機透過 QR Code 分享頻道",
    "We use local networking to connect to network-based nodes.": "我們使用區域網路連線至網路型節點。",
    "Siri and Shortcuts let you control Meshtastic hands-free — send messages, disconnect, restart, or shut down your node with your voice.": "Siri 與捷徑可讓您免持控制 Meshtastic——以語音傳送訊息、中斷連線、重新啟動或關閉節點。",
    "We use your location to display it on the mesh map, show and filter by distance as well as to have GPS coordinates to send to the connected device. Route Recording uses location in the background.": "我們使用您的定位在地圖上顯示位置、依距離顯示與篩選，並將 GPS 座標傳送至已連線裝置。路線記錄會在背景使用定位。",
    "We use your location to display it on the mesh map as well as to have GPS coordinates to send to the connected device.": "我們使用您的定位在地圖上顯示位置，並將 GPS 座標傳送至已連線裝置。",
    "Siri is used for messaging to send and receive Meshtastic messages by voice and through CarPlay.": "Siri 用於以語音及 CarPlay 傳送與接收 Meshtastic 訊息。",
    # Settings.bundle
    "Group": "群組",
    "Name": "名稱",
    "none given": "未提供",
    "Enabled": "已啟用",
    # Widget strings
    "Sent:": "已傳送：",
    "ChUtil:": "頻道使用率：",
    "Airtime:": "空中時間：",
    "Received:": "已接收：",
    "Bad:": "錯誤：",
    "Dupe:": "重複：",
    "Relayed:": "已轉發：",
    "Rly Cancel:": "轉發取消：",
    "UPTIME:": "運作時間：",
    "UPDATED:": "已更新：",
    "Uptime:": "運作時間：",
    "Update in:": "更新倒數：",
    "Not Connected": "未連線",
    "UPDATE IN": "更新倒數",
    # Watch App
    "Phone Connected": "iPhone 已連線",
    "Phone Not Reachable": "無法連線至 iPhone",
    "Open Meshtastic on your iPhone to sync node data.": "在 iPhone 上開啟 Meshtastic 以同步節點資料。",
    "Foxhunt": "獵狐",
    "No nearby nodes": "附近沒有節點",
    "Nodes within ½ mile with a known position will appear here.": "已知位置且位於半英里內的節點會顯示於此。",
    "Open Meshtastic on your iPhone to sync.": "在 iPhone 上開啟 Meshtastic 以同步。",
    "Refresh": "重新整理",
    "cached nodes": "快取節點",
    "nodes": "節點",
    "%@ %llds": "%1$@ %2$lld 秒",
    "%d Hops": "%d 跳",
    "%lld features": "%lld 項功能",
    "%lld Local Stats Readings": "%lld 筆本機統計讀數",
    "%lld nodes discovered": "發現 %lld 個節點",
    "%lld/80 bytes": "%lld/80 位元組",
    "A local stats request has been sent to %@. Responses can take some time.": "已向 %@ 傳送本機統計要求。回應可能需要一些時間。",
    "After %lld Days": "%lld 天後",
    "Canceled: %d": "已取消：%d",
    "Copy %@": "複製 %@",
    "Download the %@ language pack to read the documentation in your language.": "下載 %@ 語言套件，以您的語言閱讀文件。",
    "Dupes: %d": "重複：%d",
    "Node Core Data Backup %@ - %@ - %@": "節點核心資料備份 %1$@ - %2$@ - %3$@",
    "Noise Floor %d dBm": "噪聲底限 %d dBm",
    "Quietest channel: **%@** (%@ dBm noise floor)": "最安靜頻道：**%1$@**（%2$@ dBm 噪聲底限）",
    "Relayed: %d": "已轉發：%d",
    "Showing latest %lld of %lld positions. Export includes all positions.": "顯示最新 %1$lld 筆，共 %2$lld 筆位置。匯出包含所有位置。",
    "This will permanently delete the backup for %@ and free %@ of storage.": "這將永久刪除 %1$@ 的備份，並釋放 %2$@ 儲存空間。",
    "%lld Mesh": "%lld 個網狀網路",
    "1 byte": "1 位元組",
    "Apple Apps": "Apple 應用程式",
    "Level": "層級",
    "WiFi": "Wi-Fi",
}

# Glossary term replacements applied to auto-translated/fallback text
GLOSSARY_REPLACEMENTS = [
    (r"\bNodes\b", "節點"),
    (r"\bNode\b", "節點"),
    (r"\bChannels\b", "頻道"),
    (r"\bChannel\b", "頻道"),
    (r"\bDevices\b", "裝置"),
    (r"\bDevice\b", "裝置"),
    (r"\bSettings\b", "設定"),
    (r"\bConnected\b", "已連線"),
    (r"\bDisconnected\b", "未連線"),
    (r"\bConnecting\b", "連線中"),
    (r"\bConnect\b", "連線"),
    (r"\bDisconnect\b", "中斷連線"),
    (r"\bReconnect\b", "重新連線"),
    (r"\bMessages\b", "訊息"),
    (r"\bMessage\b", "訊息"),
    (r"\bSearch\b", "搜尋"),
    (r"\bFilter\b", "篩選"),
    (r"\bSave\b", "儲存"),
    (r"\bCancel\b", "取消"),
    (r"\bDelete\b", "刪除"),
    (r"\bEdit\b", "編輯"),
    (r"\bShare\b", "分享"),
    (r"\bReply\b", "回覆"),
    (r"\bUnknown\b", "未知"),
    (r"\bLoading\b", "載入中"),
    (r"\bOffline\b", "離線"),
    (r"\bOnline\b", "在線"),
    (r"\bFirmware\b", "韌體"),
    (r"\bTelemetry\b", "遙測"),
    (r"\bWaypoint\b", "路徑點"),
    (r"\bRegion\b", "地區"),
    (r"\bPosition\b", "位置"),
    (r"\bImport\b", "匯入"),
    (r"\bExport\b", "匯出"),
    (r"\bBackup\b", "備份"),
    (r"\bRestore\b", "還原"),
    (r"\bAbout\b", "關於"),
    (r"\bMap\b", "地圖"),
    (r"\bEnabled\b", "已啟用"),
    (r"\bDisabled\b", "已停用"),
    (r"WiFi", "Wi-Fi"),
]


def hans_to_tw(text: str) -> str:
    result = text
    for simp, trad in HANS_TO_TW.items():
        result = result.replace(simp, trad)
    return result


def apply_glossary(text: str) -> str:
    result = text
    for pattern, replacement in GLOSSARY_REPLACEMENTS:
        result = re.sub(pattern, replacement, result)
    return result


def needs_translation(key: str, en_val: str, tw_val: str) -> bool:
    if not tw_val:
        return True
    return tw_val in (en_val, key)


def make_localization(value: str) -> dict:
    return {
        "stringUnit": {
            "state": "translated",
            "value": value,
        }
    }


def translate_key(key: str, en_val: str, locs: dict) -> str | None:
    if key in TRANSLATIONS:
        return TRANSLATIONS[key]

    hans = locs.get("zh-Hans", {}).get("stringUnit", {}).get("value", "")
    zh_hant = locs.get("zh-Hant", {}).get("stringUnit", {}).get("value", "")

    if hans:
        converted = hans_to_tw(hans)
        if converted != hans or not re.search(r"[\u4e00-\u9fff]", en_val):
            return converted

    if zh_hant:
        return zh_hant

    # Format strings, numbers, symbols — keep as-is
    if re.match(r"^[\d\.\s\•\-\+/°%:]+$", key.strip()):
        return key
    if "%" in key and not re.search(r"[A-Za-z]{4,}", key):
        return key

    # Technical tokens unchanged
    if key in {"•", "dBm", "DHCP", "DNS", "IP", "GPIO", "MQTT", "BLE", "LoRa", "GPS", "OK", "mTLS", "TAK", "SSID", "IAQ", "NTP Server"}:
        return key

    return None


def main() -> None:
    with XCSTRINGS.open(encoding="utf-8") as f:
        data = json.load(f)

    strings = data.setdefault("strings", {})
    updated = 0
    skipped: list[str] = []

    for key, val in strings.items():
        if not key:
            continue
        locs = val.setdefault("localizations", {})
        en_val = locs.get("en", {}).get("stringUnit", {}).get("value", key)
        tw_val = locs.get("zh-Hant-TW", {}).get("stringUnit", {}).get("value", "")

        if not needs_translation(key, en_val, tw_val):
            continue

        translated = translate_key(key, en_val, locs)
        if translated is None:
            skipped.append(key)
            continue

        locs["zh-Hant-TW"] = make_localization(translated)
        updated += 1

    with XCSTRINGS.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Updated {updated} zh-Hant-TW entries")
    if skipped:
        print(f"Skipped {len(skipped)} entries (no translation):")
        for s in skipped[:20]:
            print(f"  - {s[:100]}")


if __name__ == "__main__":
    main()
