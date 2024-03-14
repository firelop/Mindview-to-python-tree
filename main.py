import zipfile, os
from bs4 import BeautifulSoup


# Configuration
is_list_representation = False # False: Représentation sous forme de dictionnaire, True: Représentation sous forme de liste






class Node:
    def __init__(self, bsElement, isListRepresentation):
        self.bsElement = bsElement
        self.isListRepresentation = isListRepresentation
        self.text = bsElement.find("branchcontent.list") \
                            .find("branchtext") \
                            .find("properties.list") \
                            .find("p", attrs={"n": "branchtext.text"}).attrs["v"]
                            
                                      
        self.children = self.get_children()
        
    def is_leaf(self):
        return len(self.children) == 0
    
    
    def get_dictionary_representation(self, dictionary={}):
        dictionary[self.text] = tuple(int(child.text) if child.text.isdecimal() else child.text for child in self.children)
        for child in self.children:
            dictionary = child.get_dictionary_representation(dictionary)
        return dictionary

    def __repr__(self):
        if self.isListRepresentation:
            if self.is_leaf():
                return f"{self.text}" if self.text.isdecimal() else f"\"{self.text}\""
            else:
                return f"[{self.text}, {self.children}]" if self.text.isdecimal() else f"[\"{self.text}\", {self.children}]"
        
        else:
            return f"{self.get_dictionary_representation()}"
    
    def get_children(self):
        children = []
        subbranches = self.bsElement.find("subbranches.list")
        if not subbranches:
            return children
        
        for child in subbranches.find_all("branch", recursive=False):
            children.append(Node(child, self.isListRepresentation))
        return children


def get_project_file_path():
    project_file = ""
    for foldername, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.mvdx'):
                project_file = os.path.abspath(os.path.join(foldername, filename))
                break
        if project_file:
            break
    return project_file



soup = None
with zipfile.ZipFile(get_project_file_path(), "r") as z:
    with z.open("MindViewData") as f:
        soup = BeautifulSoup(f.read(), "xml")


root = soup.find("MWDocument3").find("document").find("docnode").find("subbranches.list")
root = Node(root, is_list_representation)

f = open("output.py", "w")
f.write(str(root))
f.close()
