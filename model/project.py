from sys import maxsize
class Project:
    def __init__(self, id = None, project_name = None, project_status = None, inherit_global_categories = None, view_status = None,
                 project_description = None):
        self.id = id
        self.project_name = project_name
        self.project_status = project_status
        self.inherit_global_categories = inherit_global_categories
        self.view_status = view_status
        self.project_description = project_description


    def __repr__(self):
        return "%s:%s %s" % (self.id, self.project_name, self.project_description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.project_name == other.project_name and self.project_description == other.project_description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
