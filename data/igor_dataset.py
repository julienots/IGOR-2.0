"""Rassemble les exemples d'IGOR et définit son prompt système."""

from igor_bases import BASES
from igor_freestyle import DYNAMIQUE, FREESTYLE, TRANSITIONS
from igor_programmes import COMPETITIONS, PROGRAMMES
from igor_statique import IDENTITE, STATIQUE

SYSTEM_PROMPT = (
    "Tu es IGOR, un coach IA créé par Julien, expert en calisthenics : statique, force, "
    "freestyle, figures, progressions, transitions, combos, compétitions et programmes "
    "d'entraînement. Tu tutoies, tu réponds en français de façon précise, structurée et "
    "motivante. Si tu ne sais pas quelque chose, tu le dis au lieu d'inventer."
)

EXEMPLES = IDENTITE + BASES + STATIQUE + DYNAMIQUE + FREESTYLE + TRANSITIONS + PROGRAMMES + COMPETITIONS


def toutes_les_paires():
    """Chaque exemple, plus une variante où l'on s'adresse directement à IGOR."""
    paires = []
    for q, r in EXEMPLES:
        paires.append((q, r))
        paires.append(("Igor, " + q[0].lower() + q[1:], r))
    return paires


if __name__ == "__main__":
    print(len(EXEMPLES), "exemples,", len(toutes_les_paires()), "après variantes")
