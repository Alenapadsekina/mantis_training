import random
from model.project import Project

def test_delete_project(app, db):
    if len(db.get_projects_list()) == 0:
        app.project.create_project(Project(project_name="NEW NAME", project_description='DESCR'))
    old_projects = db.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    old_projects.remove(project)
    new_projects = db.get_projects_list()
    assert old_projects == new_projects
#    if check_ui:
#        assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_projects_list(), key=Project.id_or_max)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_projects_list(), key=Project.id_or_max)