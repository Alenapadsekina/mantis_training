from model.project import Project
import string
import random

def test_add_new_project(app, db):
    random_string = string.ascii_letters + string.digits + string.punctuation
    random_index = random.choice(random_string) + random.choice(random_string)+random.choice(random_string)
    project = Project(project_name = "NEW PROJECT "+random_index, project_description = "NEW PROJECT DESCRIPTION")
    old_projects = db.get_projects_list()
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = db.get_projects_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)