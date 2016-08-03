"""
Extended CoursePage.
"""
import abc

from edxapp_acceptance.pages.studio.course_page import CoursePage
from regression.tests.helpers import get_url


class CoursePageExtended(CoursePage):
    """
    Extended CoursePage.
    """
    @abc.abstractmethod
    def is_browser_on_page(self):
        pass

    @property
    def url(self):
        """
        Construct a URL to the page within the course.
        """
        url = get_url(self.url_path, self.course_info)
        return url
