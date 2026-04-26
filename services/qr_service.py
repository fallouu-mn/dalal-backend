# Service de simulation de QR Code pour le Hackathon
# Pas besoin de la librairie qrcode ou Pillow ici
import base64

def generer_qr(data: str) -> str:
    """
    Simule la génération d'un QR code en retournant une image base64 statique.
    Idéal pour les démonstrations de hackathon sans dépendances lourdes.
    """
    # Un petit QR code minimal en base64 (statique pour la démo)
    # Ce QR code contient juste un lien symbolique
    placeholder_qr = (
        "iVBORw0KGgoAAAANSUhEUgAAAJQAAACUCAYAAAB97nfcAAAACXBIWXMAAAsTAAALEwEAmpwYAAADXElEQVR4nO2dS3LDI"
        "AwF6X+X7mOfIn0MoSRE8LCH76pS8pAIsidW/3AcxwEIsf/9AgBfEVQghKACEIUKQBQpAFGkAEShAhBFCkAUKe7MvT0IBA"
        "L7888mP3v08X+Tfz/m5LMPvK6kAEChAhBFCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3"
        "M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7I"
        "vZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe"
        "7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAU"
        "Ke7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCk"
        "AUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCC"
        "CkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgR"
        "CCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQ"
        "gRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfE"
        "VQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ec"
        "BfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u8lO+vM9v8e+Z9+eyf"
        "2ecBfEVQgRCCCkAUKe7IvZ3M98A+u/u/f0Z9zFfAn78HAgEKhApAFCkAUaQARKEC8C8/pWv6eG6/bAAAAABJRU5ErkJggg=="
    )
    return f"data:image/png;base64,{placeholder_qr}"
