import datetime

from prac_7.project import Project

FILENAME = 'projects.txt'
HEADER = 'Name	Start Date	Priority	Cost Estimate	Completion Percentage'
MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date \n- (A)dd new project \n- (U)pdate project \n- (Q)uit"


def main():
    """Load, manage, and save projects from filename."""
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
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename, 'r', encoding='utf-8') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], int(parts[4]))
            projects.append(project)
    return projects


def save_projects(projects, filename):
    """Save projects to file."""
    with open(filename, 'w', encoding="utf-8") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.percent_complete}", file=out_file)


def display(projects):
    """Display in two groups: complete projects and incomplete projects."""
    print("Incomplete Projects: ")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Complete Projects: ")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)


def add_project(projects):
    """Add new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)


def filter_projects(projects):
    """Filter projects by start date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        project_date = project.start_date
        if project_date > date:
            print(project)


def update_projects(projects):
    """Update project priority and completion percentage."""
    for i, project in enumerate(projects):
        print(i, project)
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    try:
        percent_complete = int(input("New Percentage: "))
        project.percent_complete = percent_complete
    except ValueError:
        pass
    try:
        priority = int(input("New Priority: "))
        project.priority = priority
    except ValueError:
        pass


if __name__ == '__main__':
    main()
