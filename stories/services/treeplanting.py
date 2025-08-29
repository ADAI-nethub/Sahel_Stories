# stories/services/treeplanting.py
from django.utils import timezone
from stories.models import TreePlanting

def mark_tree_planted(tree: TreePlanting):
    tree.status = TreePlanting.Status.PLANTED
    tree.actually_planted_at = timezone.now()
    tree.save(update_fields=['status', 'actually_planted_at'])
    return tree
