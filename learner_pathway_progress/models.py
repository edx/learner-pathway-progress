# lint-amnesty, pylint: disable=cyclic-import
"""
Database models for learner_pathway_progress.
"""

import json
import logging

from common.djangoapps.student.models import CourseEnrollment
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext as _
from jsonfield.fields import JSONField
from lms.djangoapps.grades.models import PersistentCourseGrade
from model_utils.models import TimeStampedModel
from openedx.core.djangoapps.programs.utils import ProgramProgressMeter
from simple_history.models import HistoricalRecords

from .constants import PathwayCourseStatus, PathwayProgramStatus

log = logging.getLogger(__name__)

User = get_user_model()


class LearnerPathwayProgress(TimeStampedModel):
    """
    Learner pathway progress model.

    .. no_pii:
    """

    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    learner_pathway_uuid = models.UUIDField(
        editable=False, verbose_name=_('LEARNER_PATHWAY_UUID')
    )
    learner_pathway_progress = JSONField(
        blank=True,
        default={},
        help_text=_("The pathway snapshot with progress annotations."),
    )
    history = HistoricalRecords()

    class Meta:
        """
        Learner pathway progress metadata.
        """

        unique_together = ('user', 'learner_pathway_uuid')

    def __str__(self):
        """
        Learner pathway progress string.
        """
        return f"{self.user.id} - {self.learner_pathway_uuid}"

    @staticmethod
    def get_learner_course_status(user, course):
        """
        Get the progress of the learner in the course.
        """
        course_runs = course.get('course_runs') or []
        learner_enrollments = []
        for course_run in course_runs:
            learner_course_grade = PersistentCourseGrade.objects.filter(
                user_id=user.id,
                course_id=course_run['key']
            ).first()
            if learner_course_grade and learner_course_grade.passed_timestamp:
                return PathwayCourseStatus.complete
            else:
                course_enrollment = CourseEnrollment.get_enrollment(user, course_run['key'])
                if course_enrollment:
                    learner_enrollments.append(course_enrollment)
        if learner_enrollments:
            return PathwayCourseStatus.in_progress
        return PathwayCourseStatus.not_started

    @staticmethod
    def get_learner_program_status(user, program):
        """
        Get the progress of the learner in the program.
        """
        site = Site.objects.get_current()
        meter = ProgramProgressMeter(site=site, user=user, include_course_entitlements=False)
        programs_progress = meter.progress()
        for program_progress in programs_progress:
            if (
                program_progress['uuid'] == program['uuid'] and
                program_progress['completed'] and
                not program_progress['in_progress'] and
                not program_progress['not_started']
            ):
                return PathwayProgramStatus.complete
            elif program_progress['uuid'] == program['uuid'] and program_progress['in_progress']:
                return PathwayProgramStatus.in_progress
        return PathwayProgramStatus.not_started

    def update_pathway_progress(self):
        """
        Update the progress for the learner in the pathway.
        """
        # pylint: disable=import-outside-toplevel
        from learner_pathway_progress.utilities import (
            get_learner_enterprises_for_course,
            get_learner_enterprises_for_program,
        )
        pathway_snapshot = json.loads(self.learner_pathway_progress)
        pathway_steps = pathway_snapshot.get('steps') or []
        for step in pathway_steps:
            step_courses = step['courses'] or []
            step_programs = step['programs'] or []
            step_completion_requirement = step['min_requirement'] or 1
            completion_count = 0
            for course in step_courses:
                learner_course_status = self.get_learner_course_status(self.user, course)
                course["status"] = learner_course_status
                course["enterprises"] = json.dumps(
                    get_learner_enterprises_for_course(self.user, course), default=list
                )
                if learner_course_status == PathwayCourseStatus.complete:
                    completion_count += 1
            for program in step_programs:
                learner_program_status = self.get_learner_program_status(self.user, program)
                program["status"] = learner_program_status
                program["enterprises"] = json.dumps(
                    get_learner_enterprises_for_program(self.user, program), default=list
                )
                if learner_program_status == PathwayProgramStatus.complete:
                    completion_count += 1
            step['status'] = completion_count / step_completion_requirement * 100
        self.learner_pathway_progress = json.dumps(pathway_snapshot)
        self.save()


class LearnerEnterprisePathwayMembership(TimeStampedModel):
    """
    Model to store pathway membership of an enterprise learner.

    .. no_pii:
    """

    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    enterprise_customer_uuid = models.UUIDField(
        editable=False,
        db_index=True,
        verbose_name=_('ENTERPRISE_CUSTOMER_UUID'),
        help_text=_("UUID of associated enterprise customer")
    )

    learner_pathway_uuid = models.UUIDField(
        editable=False,
        verbose_name=_('LEARNER_PATHWAY_UUID'),
        help_text=_("UUID of associated pathway"),
    )

    class Meta:
        """
        Learner pathway progress metadata.
        """

        app_label = 'learner_pathway_progress'
        unique_together = ('user', 'learner_pathway_uuid', 'enterprise_customer_uuid')

    def __str__(self):
        """
        Create a human-readable string representation of the object.
        """
        return f'User: {self.user}, Pathway UUID: {self.learner_pathway_uuid},' \
               f' Enterprise UUID: {self.enterprise_customer_uuid}'

    def __repr__(self):
        """
        Return string representation.
        """
        return f'<LearnerEnterprisePathwayMembership user={self.user} pathway_uuid="{self.learner_pathway_uuid}" ' \
               f'Enterprise UUID: {self.enterprise_customer_uuid}>'
