import datetime

from prac_06.projects import Project

FILENAME = 'projects.txt'
HEADER = 'Name	Start Date	Priority	Cost Estimate	Completion Percentage'
MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date \n- (A)dd new project \n- (U)pdate project \n- (Q)uit"


def main():
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("File to load: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("File to Save: ")
            save_projects(projects, filename)
        elif choice == "D":
            display(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from tab-delimited"""
    projects = []
    with open(FILENAME, 'r', encoding='utf-8') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            # start_date = datetime.datetime.strptime()
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def save_projects(projects, filename):
    """Save projects to tab-delimited text"""
    with open(filename, 'w', encoding="utf-8") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.percent_complete}", file=out_file)


def display(projects):
    """Display in two groups: complete projects and incomplete projects."""
    print("Incomplete Projects: ")
    incomplete_projects = [project for project in projects if projects.is_]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Complete Projects: ")
    complete_projects = [project for project in projects if projects == 100]
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)


if __name__ == '__main__':
    main()
