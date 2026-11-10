# Hi there, I'm Jorge 👋

<p align="left">
  <strong>Software Engineering Student &amp; Backend Developer</strong> based in Madrid, Spain 🇪🇸<br>
  Passionate about high-performance backend systems, systems programming, and building clean, native, bloatware-free desktop utilities.
</p>

<p align="left">
  <a href="https://github.com/jorjanion"><img src="https://img.shields.io/github/followers/jorjanion?style=flat-square&logo=github&label=Followers&color=24292e" alt="GitHub Followers" /></a>
  <img src="https://img.shields.io/badge/Focus-Backend%20%26%20Systems-blue?style=flat-square" alt="Focus" />
  <img src="https://img.shields.io/badge/Status-Undergraduate%20Software%20Engineer-0078D6?style=flat-square" alt="Status" />
</p>

---

## 💻 About Me

- 🎓 **Studies:** Software Engineering student focusing on software architecture, distributed systems, and low-level system design.
- ⚙️ **Core Focus:** Backend development — building scalable APIs, microservices, and asynchronous services with **Java** and **Python**.
- 🦀 **Systems & Desktop:** Building high-efficiency native tools in **Rust**, **C#**, and **C++**.
- 🌐 **My Ecosystem:**
  - **PC / Desktop:** Dual-driver on **Windows** and **Linux** (KDE Plasma on Wayland).
  - **Mobile & Wearables:** Power user of the Apple ecosystem (**iOS**, **iPadOS**, and **watchOS / Apple Watch**), frequently creating cross-platform bridges to connect Apple devices seamlessly with PC environments.

---

## 🛠️ Languages & Technologies

### 🚀 Core Backend
<p align="left">
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</p>

### ⚡ Systems & Native Desktop
<p align="left">
  <img src="https://img.shields.io/badge/Rust-DEA584?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white" alt="C#" />
  <img src="https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white" alt=".NET" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/Tauri%20v2-FFC131?style=for-the-badge&logo=tauri&logoColor=black" alt="Tauri" />
</p>

### 🖥️ Platforms & Environments
<p align="left">
  <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/KDE%20Plasma-1D99F3?style=for-the-badge&logo=kde&logoColor=white" alt="KDE Plasma" />
  <img src="https://img.shields.io/badge/Wayland-0284C7?style=for-the-badge&logo=wayland&logoColor=white" alt="Wayland" />
  <img src="https://img.shields.io/badge/iOS%20%7C%20iPadOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Apple iOS / iPadOS" />
  <img src="https://img.shields.io/badge/Apple%20Watch%20(watchOS)-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Apple Watch" />
</p>

---

## 🚀 Featured Open Source Projects

*Ordered from highest technical complexity to lightweight utilities:*

---

### 1. 🔑 [WristKey](https://github.com/jorjanion/WristKey)
> **Proximity auto-lock & hands-free unlock for Windows 11 / 10 using Apple Watch via BLE**  
> *Brings the seamless macOS Auto Unlock experience natively to Windows with zero third-party companion apps required on the watch.*

[![Latest Release](https://img.shields.io/github/v/release/jorjanion/WristKey?color=2ea44f&label=Release&style=flat-square)](https://github.com/jorjanion/WristKey/releases)
[![License: MIT / Apache-2.0](https://img.shields.io/badge/License-MIT%20%2F%20Apache--2.0-blue.svg?style=flat-square)](https://github.com/jorjanion/WristKey/blob/main/LICENSE-MIT)
[![Rust](https://img.shields.io/badge/Made%20with-Rust-DEA584?style=flat-square&logo=rust)](https://www.rust-lang.org/)
[![Tauri v2](https://img.shields.io/badge/UI-Tauri%20v2-FFC131?style=flat-square&logo=tauri&logoColor=black)](https://tauri.app/)

* **Technical Highlights & Complexity:**
  - **Cryptographic RPA Resolution:** Resolves Apple Continuity Bluetooth LE Resolvable Private Addresses (RPA) cycling every 15 minutes by computing local cryptographic hash lookups via AES-128 Identity Resolving Keys (IRK).
  - **Hardware Security & DPAPI:** Securely vaults and injects Windows domain credentials through Microsoft Data Protection API (DPAPI) without ever persisting plain text.
  - **Continuous RSSI Tracking:** Dynamic distance-attenuation filtering coupled with optical on-wrist sensor detection to avoid false-positive unlocks.

---

### 2. 📺 [UxPlay Desktop](https://github.com/jorjanion/uxplay-desktop)
> **Ultra-low-latency 60 FPS AirPlay screen mirroring & audio receiver for Windows 10 / 11**  
> *Turns your Windows PC into a high-performance Apple AirPlay display and audio receiver for iPad and iPhone.*

[![Latest Release](https://img.shields.io/github/v/release/jorjanion/uxplay-desktop?color=blue&label=Release&style=flat-square)](https://github.com/jorjanion/uxplay-desktop/releases)
[![License: GPL v3.0](https://img.shields.io/badge/License-GPL%20v3.0-green.svg?style=flat-square)](https://github.com/jorjanion/uxplay-desktop/blob/main/LICENSE)
[![.NET 8](https://img.shields.io/badge/.NET-8.0%20Self--Contained-512BD4?style=flat-square&logo=dotnet)](https://dotnet.microsoft.com/)
[![Direct3D](https://img.shields.io/badge/Render-Direct3D%2011%2F12-orange?style=flat-square)](https://github.com/jorjanion/uxplay-desktop)

* **Technical Highlights & Complexity:**
  - **Direct3D Hardware Acceleration:** High-performance video surface pipeline utilizing Direct3D 11/12 for sub-frame latency and zero-drop 60 FPS mirroring.
  - **Embedded GStreamer Engine:** 100% self-contained portable runtime with embedded H.264 decoding pipelines, eliminating external codec dependencies.
  - **Self-Healing Networking:** Automated Apple Bonjour & mDNS service repair, dynamic network interface binding, and Windows Firewall port provisioning.

---

### 3. 🐍 [Serpanplasma](https://github.com/jorjanion/serpantinum-kde-plasma)
> **Serpantinum desktop aesthetic natively ported to KDE Plasma 6 on Wayland**  
> *Translates modern floating pill bars, translucent styling, and micro-animations to Linux without the overhead of tiling window managers.*

[![GitHub](https://img.shields.io/badge/Repo-serpantinum--kde--plasma-8b5cf6?style=flat-square&logo=github)](https://github.com/jorjanion/serpantinum-kde-plasma)
[![KDE Plasma 6](https://img.shields.io/badge/KDE_Plasma-6.0%2B-38bdf8?style=flat-square&logo=kde&logoColor=white)](https://kde.org/plasma-desktop/)
[![Wayland](https://img.shields.io/badge/Display-Wayland-0284c7?style=flat-square&logo=wayland&logoColor=white)](https://wayland.freedesktop.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-f87171?style=flat-square)](https://github.com/jorjanion/serpantinum-kde-plasma/blob/main/LICENSE)

* **Technical Highlights & Complexity:**
  - **Native QML Plasmoid (`org.serpanplasma.bar`):** Custom desktop widgets utilizing KWin blur effects, rounded geometry, and Wayland floating surface rules.
  - **Sub-millisecond Python Daemon:** Lightweight status daemon running as a `systemd` user service, asynchronously aggregating MPRIS, PipeWire/WirePlumber audio, network throughput (`/proc/net/dev`), and battery power metrics via DBus.
  - **Non-Tiling Workflow:** Retains complete floating window flexibility with standard keyboard shortcuts and multi-monitor support.

---

### 4. 🔋 [BatteryDock](https://github.com/jorjanion/BatteryDock)
> **Ultra-lightweight Windows taskbar dock for peripheral battery levels with custom alerts**  
> *Real-time battery monitoring directly embedded into your taskbar for Bluetooth LE, Logitech, and gaming controllers.*

[![Latest Release](https://img.shields.io/github/v/release/jorjanion/BatteryDock?color=2ea44f&label=Release&style=flat-square)](https://github.com/jorjanion/BatteryDock/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://github.com/jorjanion/BatteryDock/blob/main/LICENSE)
[![Rust](https://img.shields.io/badge/Made%20with-Rust-DEA584?style=flat-square&logo=rust)](https://www.rust-lang.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%2F%2011-0078D6?style=flat-square&logo=windows)](https://github.com/jorjanion/BatteryDock)

* **Technical Highlights & Complexity:**
  - **Low-Level Protocol Parsing:** Direct hardware communication via Bluetooth GATT Battery Service, Logitech HID++ 2.0/4.5 IPC protocols, XInput (Xbox), and raw HID (PlayStation DualSense).
  - **Zero-Bloat Footprint:** Built in Rust with minimal memory consumption (~15 MB RAM, 0% idle CPU) as a clean alternative to heavy manufacturer suites.
  - **Taskbar Dock Integration:** Seamlessly attaches beside the Windows system tray as an acrylic frosted status capsule.

---

### 5. 📄 [SimpleScan](https://github.com/jorjanion/SimpleScan)
> **Fast, native, bloatware-free document scanner for Windows with local OCR**  
> *A clean utility for scanning documents with local OCR and searchable PDF generation without vendor bloat or subscriptions.*

[![Latest Release](https://img.shields.io/github/v/release/jorjanion/SimpleScan?color=512BD4&label=Release&style=flat-square)](https://github.com/jorjanion/SimpleScan/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://github.com/jorjanion/SimpleScan/blob/main/LICENSE)
[![.NET 9](https://img.shields.io/badge/.NET-9.0-512BD4?style=flat-square&logo=dotnet)](https://dotnet.microsoft.com/)
[![Windows](https://img.shields.io/badge/Platform-Windows%2010%20%2F%2011-0078D6?style=flat-square&logo=windows)](https://github.com/jorjanion/SimpleScan)

* **Technical Highlights & Complexity:**
  - **WIA 2.0 & eSCL Driver Auto-Detection:** Direct device discovery and acquisition across HP, Canon, Epson, and Brother scanners over USB and local network.
  - **Hardware-Accelerated Local OCR:** Uses local `Windows.Media.Ocr` engine for 100% private, on-device character recognition and searchable multi-page PDF generation.
  - **Privacy First:** Zero background telemetry, zero registration requirements, instant startup.

---

<p align="center">
  <a href="https://github.com/jorjanion">
    <img src="https://github-readme-stats.vercel.app/api?username=jorjanion&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="Jorge's GitHub Stats" />
  </a>
</p>
