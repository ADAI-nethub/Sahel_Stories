# stories/services/treeplanting.py
from django.utils import timezone  # Pour connaitre la date et l'heure actuelles
from stories.models import TreePlanting  # On importe le modele TreePlanting

def mark_tree_planted(tree: TreePlanting):
    # Cette fonction marque un arbre comme ayant ete plante
    
    # On change le statut de l'arbre pour dire qu'il est plante
    tree.status = TreePlanting.Status.PLANTED
    
    # On enregistre la date et l'heure exactes ou l'arbre a ete plante
    tree.actually_planted_at = timezone.now()
    
    # On sauvegarde seulement les champs qui ont change pour aller plus vite
    tree.save(update_fields=['status', 'actually_planted_at'])
    
    # On retourne l'arbre modifie
    return tree