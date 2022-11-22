# Define Day Class
class Day:
    # Constructor
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.instructions = self.get_instruction_file_content()
        self.input = self.get_input_file_content()
        self.input_filename = ('static/input/day'+str(self.id)+'_input')

    def print_day(self):
        print("Day ", self.id, ": ", " - ", self.title)
        print("Select what you would like to view: ")

    # Get Input File Content from File Name
    def get_input_file_content(self):
        with open(f"static/input/day{self.id}_input") as f:
            file_content = f.read()
        return file_content

    # Get Instruction File Content from File Name
    def get_instruction_file_content(self):
        with open(f"static/instructions/day{self.id}_instructions", "r") as f:
            file_content = f.read()
        return file_content