"""Rassemble les exemples d'IGOR et définit son prompt système."""

from igor_bases import BASES
from igor_complements import COMPLEMENTS
from igor_freestyle import DYNAMIQUE, FREESTYLE, TRANSITIONS
from igor_programmes import COMPETITIONS, PROGRAMMES
from igor_reformulations import REFORMULATIONS
from igor_statique import IDENTITE, STATIQUE

SYSTEM_PROMPT = (
    "Tu es IGOR, un coach IA créé par Julien, expert en calisthenics : statique, force, "
    "freestyle, figures, progressions, transitions, combos, compétitions et programmes "
    "d'entraînement. Tu tutoies, tu réponds en français de façon précise, structurée et "
    "motivante. Si tu ne sais pas quelque chose, tu le dis au lieu d'inventer."
)

EXEMPLES = (IDENTITE + BASES + STATIQUE + DYNAMIQUE + FREESTYLE + TRANSITIONS + PROGRAMMES
            + COMPETITIONS + COMPLEMENTS)


def toutes_les_paires():
    """Chaque exemple, ses reformulations, et une variante où l'on s'adresse à IGOR."""
    reponses = dict(EXEMPLES)
    inconnues = set(REFORMULATIONS) - set(reponses)
    if inconnues:
        raise ValueError(f"Reformulations sans question d'origine : {inconnues}")
    paires = []
    for q, r in EXEMPLES:
        paires.append((q, r))
        paires.append(("Igor, " + q[0].lower() + q[1:], r))
        paires.extend((variante, r) for variante in REFORMULATIONS.get(q, []))
    return paires


if __name__ == "__main__":
    print(len(EXEMPLES), "exemples,", len(toutes_les_paires()), "paires d'entraînement")
