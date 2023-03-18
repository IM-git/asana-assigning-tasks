from assign_tasks import AssignTask
from asana_methods import AsanaMethods
from src import AsanaData


if __name__ == '__main__':
    section_id_with_task = AsanaData.PROJECTS.value['Plan IM test']['sections']['TC']
    list_tasks = AsanaMethods().get_list_tasks(section_gid=section_id_with_task)
    projects = AsanaData.PROJECTS.value
    AssignTask()
