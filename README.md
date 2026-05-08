# 🎮 FPS Display — Fabric Mod for Minecraft 1.21.1

Displays your **current FPS** in the **top-left corner** of the screen.  
Color-coded: 🟢 Green (≥60), 🟡 Yellow (30–59), 🔴 Red (<30).

---

## ✅ Compatibility

| Platform | Status |
|---|---|
| Minecraft 1.21.1 | ✅ |
| Fabric Loader ≥ 0.16.0 | ✅ |
| Fabric API | ✅ Required |
| Java 21 | ✅ Required |
| **PojavLauncher** (Android/iOS) | ✅ Compatible |
| **Zalith Launcher** (Android) | ✅ Compatible |
| Standard PC launcher | ✅ Compatible |

---

## 📦 Installation

1. Install **Fabric Loader** for Minecraft 1.21.1
2. Install **Fabric API**
3. Download the latest `.jar` from [Releases](../../releases)
4. Drop it into `.minecraft/mods/`

### Mobile (Pojav / Zalith)
1. In your launcher settings, select **Java 21** as the runtime
2. Add the mod jar to your mods folder as usual
3. Launch — FPS counter appears top-left, away from mobile touch zones

---

## 🔨 Building from Source

```bash
git clone https://github.com/YourUsername/fpsdisplay.git
cd fpsdisplay
./gradlew build
# Output: build/libs/fpsdisplay-1.0.0.jar
```

Requires **Java 21** on your PATH.

---

## 🤖 Automatic Builds (GitHub Actions)

Every push to `main`/`master` automatically compiles the mod.  
Pushing a tag like `v1.0.0` creates a full GitHub Release with the JAR attached.

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

## ⚙️ How It Works

The mod uses a **Mixin** to inject into `InGameHud#render()`. It reads  
`MinecraftClient#getCurrentFps()` each frame and draws the value with  
`DrawContext#drawTextWithShadow()` — no reflection, no hacks.

---

## 📄 License

MIT — do whatever you want with it.
