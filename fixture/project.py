from model.project import Project
import string
import random

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_create_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_create_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
            wd.find_element_by_css_selector("input[value = 'Create New Project']").click()

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        # project name
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.project_name)
        # project status
        wd.find_element_by_name("status").click()
       # wd.find_element_by_name("status").clear()
        # inherit global categories
        wd.find_element_by_name("inherit_global").click()
        # project status
        wd.find_element_by_name("view_state").click()
#        wd.select_by_visible_text("public")
#        wd.find_element_by_name("view_state").click()
        # project description
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.project_description)


    def create_project(self, project):
        wd = self.app.wd
        self.open_create_project_page()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value = 'Add Project']").click()


    def delete_project(self, id):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//a[@href='manage_proj_edit_page.php?project_id=" +id + "']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    projects_cache = None

    def get_projects_list(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.projects_cache = []
            for rows in wd.find_elements_by_xpath("//table[3]")[2:]:
                elements = rows.find_elements_by_tag_name("td")
                project_name = elements[0].text
                project_description = elements[4].text
                id = elements[0].get_attribute("value")
                self.projects_cache.append(Project(project_name=project_name, id=id, project_description = project_description))
        return self.projects_cache


