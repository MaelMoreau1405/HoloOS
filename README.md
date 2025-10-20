# 🪩 HoloOS — Gesture‑Controlled Desktop Interface
**Created by Multiverse Inc.**

![Interface preview](https://raw.githubusercontent.com/MaelMoreau1405/HoloOS/refs/heads/master/templates/preview.png)

---

## 🧭 Description

**HoloOS** est un mini‑système d’exploitation gestuel complet :  
il combine la **détection de la main** en temps réel et une **interface web** interactive, pilotée totalement **sans périphérique physique**.

Inspiré des interfaces holographiques de science‑fiction, l’utilisateur contrôle le bureau par simples mouvements :
ouvrir ou déplacer des fenêtres, activer de la musique, consulter l’heure, la météo…  
le tout **depuis la paume de la main** 🤚

---

## 🚀 Fonctionnalités

- 🖐 Détection de main avec **MediaPipe** (ouverte / fermée)  
- 🌈 **Curseur holographique** en temps réel  
- ⏳ **Clic par maintien** : si la main reste 3 s sur un bouton → clic validé  
- 🪟 **Déplacement gestuel (drag)** : saisir une fenêtre main fermée  
- 🧱 **Dock inférieur** : raccourcis pour ouvrir les applis
- 🕑 **Horloge temps réel**  
- 💻 **Moniteur système** : CPU / RAM / IP  
- 🌤 **Météo** : API Open‑Meteo (ville : Marseille)  
- 📝 **Bloc‑notes** déplaçable  
- 🎵 **Musique intégrée** : lecture/pause via geste  
- 👾 **Double splash screen** :  
  1 → _HoloOS_ 2 → _By Multiverse Inc._ avant l’ouverture du bureau  

---

## ⚙️ Installation

> Requiert **Python 3.9+** et une webcam fonctionnelle.

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/<ton-user>/HoloOS.git
   cd HoloOS
2. **Installer les dépendances**
   ```bash
   pip install flask flask-socketio opencv-python mediapipe psutil

---

**Geste	Action**

✋ Main ouverte maintenue 3 s	Clic / ouverture (remplissage du cercle)
✊ Main fermée sur une fenêtre	Saisir / déplacer
🙌 Relâcher (main ouverte)	Lâcher la fenêtre

---

*© 2025 — Created by Multiverse Inc. All rights reserved.*
