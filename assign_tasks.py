from asana_methods import AsanaMethods
import re
from src import AsanaData


SECTION_ID_WITH_TASK = AsanaData.PROJECTS.value['Plan IM test']['sections']['TC']
LIST_TASKS = AsanaMethods().get_list_tasks(section_gid=SECTION_ID_WITH_TASK)
PROJECTS = AsanaData.PROJECTS.value


class AssignTask:
    """
    There are we filter|extract branch from tasks name.
    If confirmed conditions - assign task to specify project.
    """

    # def __init__(self):
    #     self.section_id_with_task =
    #     self.list_tasks =
    #     self.projects =

    @staticmethod
    def choice_project_by_branch_name(branch_name):
        """To check if a given branch_name exists in the PROJECTS dictionary."""
        for project_name, project_info in PROJECTS.items():
            if branch_name in project_info['branches']:
                return project_name
        return None

    @staticmethod
    def extract_parentheses(value) -> str:
        """If string begins of the text in parentheses need to return
        this part of the text in parentheses."""
        match = re.match(r'^\((.*?)\)', value)
        return match.group(1) if match else None

    @staticmethod
    def assign_task_to_project(task_id, proj_id):
        AsanaMethods().add_already_created_task_to_addition_project(task_id, proj_id)

    @staticmethod
    def assign_tasks(tasks):
        """Parse tasks and assign task to other project if the condition is met."""
        for task in tasks:
            print('=================')
            print(f"Task name: {task['name']}")
            print(f"Branch: {AssignTask().extract_parentheses(task['name'])}")
            print(f"Project: {AssignTask().choice_project_by_branch_name(AssignTask().extract_parentheses(task['name']))}")
            if AssignTask().choice_project_by_branch_name(AssignTask().extract_parentheses(task['name'])):
                print("Done")
                proj_name = AssignTask().choice_project_by_branch_name(AssignTask().extract_parentheses(task['name']))
                proj_id = PROJECTS[proj_name]['gid']
                # AssignTask().assign_task_to_project(task['gid'], proj_id)
            else:
                print("Skipped")


if __name__ == '__main__':
    # print(list_tasks)
    # print(section_id_with_task)
    AssignTask().assign_tasks(LIST_TASKS)

    # print(choice_project_by_branch_name("dev/match3"))
    # print(choice_project_by_branch_name("dev/match"))
    # print(choice_project_by_branch_name("dev/"))
    # print(choice_project_by_branch_name("vfx/match3"))
    # print(choice_project_by_branch_name("123"))
    # print(choice_project_by_branch_name("main"))
    # print(choice_project_by_branch_name("dev/room_design"))
    # print(choice_project_by_branch_name("vso/room_design"))
