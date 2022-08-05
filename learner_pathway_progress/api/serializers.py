"""
Serializers for Learner Pathway Progress APIs.
"""

from rest_framework import serializers

from learner_pathway_progress.models import LearnerPathwayProgress


class PathwayProgressSerializer(serializers.ModelSerializer):
    """
    Serializer for LearnerPathwayProgress model.
    """
    class Meta:
        model = LearnerPathwayProgress
        fields = ['learner_pathway_progress']
