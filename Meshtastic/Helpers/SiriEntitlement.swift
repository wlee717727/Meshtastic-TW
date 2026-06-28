//
//  SiriEntitlement.swift
//  Meshtastic
//

#if os(iOS) && !targetEnvironment(macCatalyst)
import Foundation
import Intents
import OSLog

enum SiriEntitlement {
	private static let entitlementKey = "com.apple.developer.siri"

	/// True when the signed app includes the Siri development entitlement.
	static var isAvailable: Bool {
		guard let provisioningEntitlements = embeddedProvisioningEntitlements() else {
			return false
		}
		return provisioningEntitlements[entitlementKey] != nil
	}

	static func requestAuthorizationIfAvailable() {
		guard isAvailable else {
			Logger.services.info("Skipping Siri authorization — com.apple.developer.siri entitlement not present")
			return
		}
		INPreferences.requestSiriAuthorization { status in
			Logger.services.info("Siri authorization status: \(String(describing: status))")
		}
	}

	static func requestAuthorizationIfAvailable() async {
		guard isAvailable else {
			Logger.services.info("Skipping Siri authorization — com.apple.developer.siri entitlement not present")
			return
		}
		await withCheckedContinuation { continuation in
			INPreferences.requestSiriAuthorization { status in
				switch status {
				case .authorized:
					Logger.services.info("Siri permissions are enabled")
				case .denied:
					Logger.services.info("Siri permissions denied")
				default:
					Logger.services.info("Siri permissions status: \(status.rawValue)")
				}
				continuation.resume()
			}
		}
	}

	private static func embeddedProvisioningEntitlements() -> [String: Any]? {
		guard let url = Bundle.main.url(forResource: "embedded", withExtension: "mobileprovision"),
			  let data = try? Data(contentsOf: url),
			  let raw = String(data: data, encoding: .isoLatin1),
			  let start = raw.range(of: "<?xml"),
			  let end = raw.range(of: "</plist>") else {
			return nil
		}
		let plistString = String(raw[start.lowerBound..<end.upperBound])
		guard let plistData = plistString.data(using: .utf8),
			  let plist = try? PropertyListSerialization.propertyList(from: plistData, options: [], format: nil) as? [String: Any],
			  let entitlements = plist["Entitlements"] as? [String: Any] else {
			return nil
		}
		return entitlements
	}
}
#endif
