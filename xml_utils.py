import configs

from xml.etree import ElementTree as decoder

PATTERN = "/*.xml"

# -----------------------------------
# Easy class
class NodeXML:

    JSON = '.json'
    LUA = '.lua'
    CFG = 'configs' + JSON

    PACKAGE = 'Package'
    TRIGGER = 'Trigger'
    TRIGGER_PACKAGE = 'TriggerPackage'
    TRIGGER_GROUP = 'TriggerGroup'
    SCRIPT = 'Script'
    SCRIPT_PACKAGE = 'ScriptPackage'
    SCRIPT_GROUP = 'ScriptGroup'
    ALIAS = 'Alias'
    ALIAS_PACKAGE = 'AliasPackage'
    ALIAS_GROUP = 'AliasGroup'

    NODE_GROUP = [
        TRIGGER,
        TRIGGER_GROUP,
        TRIGGER_PACKAGE,
        SCRIPT,
        SCRIPT_GROUP,
        SCRIPT_PACKAGE,
        ALIAS,
        ALIAS_GROUP,
        ALIAS_PACKAGE]

    TAG = 'tag'
    ATTIBUTES = 'attributes'
    TEXT = 'text'
    CONDITIONS = 'conditions'
    SCRIPT = 'script'

    NAME = 'name'

    IS_FOLDER = 'isFolder'
    YES = 'yes'
    NO = 'no'

    def __init__(self, etree, path):
        self.path = path
        self.etree = etree
        self.structure = {}
        self.childs = []

    def save(self):
        if self.ATTIBUTES in self.structure:
            if self.IS_FOLDER in self.structure[self.ATTIBUTES]:
                if self.structure[self.ATTIBUTES][self.IS_FOLDER] == self.YES:
                    configs.create_dir(self.path)
        else:
            configs.create_dir(self.path)
        if self.CONDITIONS in self.structure:
            if self.SCRIPT in self.structure[self.CONDITIONS]:
                if self.structure[self.CONDITIONS][self.SCRIPT] is not None:
                    script = self.structure[self.CONDITIONS].pop(self.SCRIPT)
                    configs.write_file(self.path + self.LUA, script)
                    path = self.path + self.JSON
                    configs.write_json(path, self.structure)
                    return
        path = self.path + '/' + self.CFG
        configs.write_json(path, self.structure)

    def is_node(self, element):
        if element.tag in self.NODE_GROUP:
            return True
        return False

    def find_name(self, element):
        if self.PACKAGE in element.tag:
            return element.tag
        else:
            return element.find(self.NAME).text

    def map_info(self):
        if self.etree.attrib:
            self.structure[self.ATTIBUTES] = self.etree.attrib
        if '\n' not in self.etree.text:
            self.structure[self.TEXT] = self.etree.text

    def map_elements(self):
        self.structure[self.TAG] = self.etree.tag
        for child in self.etree:
            if self.is_node(child):
                child_name = self.find_name(child)
                child_path = self.path + '/' + child_name
                self.childs.append(NodeXML(child, child_path))
            else:
                if self.CONDITIONS not in self.structure:
                    self.structure[self.CONDITIONS] = {}
                self.structure[self.CONDITIONS][child.tag] = child.text

    def execute_children(self):
        for child in self.childs:
            child.execute()

    def execute(self):
        self.map_info()
        self.map_elements()
        self.save()
        self.execute_children()


# -----------------------------------
# File manipulation
def find_files(path):
    pattern = path + PATTERN
    return configs.find_files(pattern)

# -----------------------------------
# Xml manipulation
def string_to_etree(string):
    return decoder.fromstring(string)


def to_proj(path, proj_path):
    xml_string = configs.read_file(path)
    etree = string_to_etree(xml_string)
    NodeXML(etree, proj_path).execute()
