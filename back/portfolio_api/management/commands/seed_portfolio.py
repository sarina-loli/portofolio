from datetime import date

from django.core.management.base import BaseCommand
from django.db import transaction

from portfolio_api.models import (
    Education,
    Experience,
    Profile,
    Project,
    ProjectTechnology,
    Service,
    Skill,
    Technology,
)


class Command(BaseCommand):
    help = "Seed the database with realistic sample portfolio data."

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Seeding profile...")
        profile, _ = Profile.objects.update_or_create(
            id=1,
            defaults=dict(
                full_name="Sara Getu",
                title="Full-Stack Software Developer",
                tagline="Building modern, responsive, and scalable web applications with React and Django.",
                intro=(
                    "Hi, I'm Sara Getu, a passionate Full-Stack Developer who enjoys building modern, user-friendly, and reliable web applications. I specialize in developing frontend experiences with React and powerful backend systems with Django and Django REST Framework."
                ),
                about=("I am a Full-Stack Developer passionate about turning ideas into practical and engaging web applications. I work with React to create responsive and interactive user interfaces and Django and Django REST Framework to build secure, scalable, and well-structured backend systems.I enjoy working across the entire development process, from designing user interfaces and building REST APIs to connecting databases, implementing authentication, and deploying applications.My goal is to continuously improve my skills, solve real-world problems through technology, and create software that provides a great experience for users"),
                philosophy=(
                    "I believe good software should be simple, useful, maintainable, and built with the user in mind. I focus on writing clean code, learning continuously, and solving problems through practical solutions."
                ),
                specialties=(
                    "React frontend development, Django backend development, REST API development, database integration, authentication, responsive web design, and full-stack application development."
                ),
                career_goals=(
                    "My goal is to grow as a professional Full-Stack Developer, work on meaningful software projects, strengthen my expertise in modern web technologies, and build applications that solve real-world problems."
                ),
                location="Remote / Addis Ababa, ET",
                email="sarina123getu@gmail.com",
                phone="+251993527788",
                github_url="https://github.com/sarina-lol",
                linkedin_url="https://www.linkedin.com/in/sara-getu",
                twitter_url="",
                website_url="",
                years_experience=0,
            ),
        )

        self.stdout.write("Seeding skills...")
        Skill.objects.all().delete()
        skills = [
            ("React", "frontend", 90),
            ("JavaScript", "frontend", 90),
            ("HTML5", "frontend", 95),
            ("CSS3", "frontend", 90),
            ("React Router", "frontend", 85),
            ("Axios", "frontend", 88),
            ("Python", "backend", 92),
            ("Django", "backend", 90),
            ("Django REST Framework", "backend", 90),
            ("REST APIs", "backend", 92),
            ("PostgreSQL", "database", 85),
            ("SQL", "database", 85),
            ("JWT", "security", 82),
            ("Permissions", "security", 80),
            ("CORS", "security", 78),
            ("API Security", "security", 80),
            ("Git", "tools", 92),
            ("GitHub", "tools", 92),
            ("Render", "tools", 75),
            ("VS Code", "tools", 95),
            ("Docker", "tools", 70),
        ]
        for order, (name, category, proficiency) in enumerate(skills):
            Skill.objects.create(name=name, category=category, proficiency=proficiency, order=order)

        self.stdout.write("Seeding technologies + projects...")
        tech_names = {
            "React", "Django", "Django REST Framework", "PostgreSQL", "JWT", "Axios",
            "Python", "React Router", "Docker", "Celery", "Redis",
        }
        tech_map = {}
        for name in tech_names:
            tech_map[name], _ = Technology.objects.get_or_create(name=name)

        Project.objects.all().delete()

        expense_tracker = Project.objects.create(
            title="Expense Tracker",
            summary=(
                "A full-stack personal finance app for managing expenses, income, "
                "budgets, and categories."
            ),
            description=(
                "A full-stack personal finance application that helps users manage "
                "expenses, income, budgets, categories, and financial activity. Built "
                "with a Django REST API backend and a React frontend, it gives users a "
                "clear picture of where their money goes each month."
            ),
            problem=(
                "Most budgeting apps are either too simplistic to be useful or too "
                "complex to stick with. People need a fast way to log transactions and "
                "see trends without a steep learning curve."
            ),
            solution=(
                "A focused expense/income tracker with categories, budgets, and a "
                "dashboard that surfaces monthly trends, all backed by a secure, "
                "per-user REST API."
            ),
            architecture=(
                "React (Vite) talks to a Django REST Framework API over JWT-authenticated "
                "requests. PostgreSQL stores transactions, categories, and budgets, "
                "scoped per user via row-level ownership checks in the API layer."
            ),
            challenges=(
                "Designing budget-vs-actual calculations that stay fast as transaction "
                "history grows, and keeping the dashboard responsive on mobile."
            ),
            lessons_learned=(
                "Investing early in serializer-level validation and pagination paid off "
                "once the sample dataset grew past a few thousand transactions."
            ),
            features=(
                "User authentication\n"
                "Expense CRUD\n"
                "Income management\n"
                "Categories\n"
                "Budgets\n"
                "Search\n"
                "Filtering\n"
                "Pagination\n"
                "Financial dashboard\n"
                "User-specific data"
            ),
            github_url="https://github.com/alexmorgan-dev/expense-tracker",
            live_url="https://expense-tracker.example.com",
            featured=True,
            order=0,
        )
        for name in ["React", "Django", "Django REST Framework", "PostgreSQL", "JWT", "Axios"]:
            ProjectTechnology.objects.create(project=expense_tracker, technology=tech_map[name])

        time_manager = Project.objects.create(
            title="Time Management Application",
            summary="A productivity app for tracking tasks, time, and recurring work.",
            description=(
                "A time management and productivity application with task tracking, "
                "timers, and reporting. Helps users understand where their time actually "
                "goes versus where they planned to spend it."
            ),
            problem=(
                "Task lists alone don't show whether estimates were realistic. People "
                "need actual-vs-estimated time tracking to improve planning over time."
            ),
            solution=(
                "Tasks carry both an estimated and an actual duration, tracked with a "
                "built-in timer, and rolled up into daily/weekly/monthly/yearly reports."
            ),
            architecture=(
                "Django REST Framework exposes tasks, categories, and time entries; "
                "scheduled aggregation queries power the reporting endpoints consumed by "
                "React chart components."
            ),
            challenges="Modeling recurring tasks cleanly without duplicating rows for every occurrence.",
            lessons_learned="Aggregation queries needed careful indexing once reports spanned a full year of data.",
            features=(
                "Task management\n"
                "Task priorities\n"
                "Estimated time\n"
                "Actual time\n"
                "Task timer\n"
                "Daily/weekly/monthly/yearly reports\n"
                "Productivity tracking\n"
                "Recurring tasks\n"
                "Categories"
            ),
            github_url="https://github.com/alexmorgan-dev/time-manager",
            live_url="https://time-manager.example.com",
            featured=True,
            order=1,
        )
        for name in ["React", "Django", "Django REST Framework", "PostgreSQL", "Celery", "Redis"]:
            ProjectTechnology.objects.create(project=time_manager, technology=tech_map[name])

        self.stdout.write("Seeding experience...")
        Experience.objects.all().delete()
        Experience.objects.create(
            position="Full-Stack Developer",
            company="Northwind Software",
            location="Remote",
            description=(
                "Built and maintained customer-facing features across a Django/React "
                "product, working closely with design and product to ship end-to-end."
            ),
            technologies="Django, DRF, React, PostgreSQL, Docker",
            start_date=date(2023, 3, 1),
            end_date=None,
            is_current=True,
            order=0,
        )
        Experience.objects.create(
            position="Backend Developer",
            company="Harborlight Systems",
            location="Addis Ababa, ET",
            description=(
                "Designed REST APIs and data models for an internal operations platform; "
                "introduced JWT auth and automated testing to the codebase."
            ),
            technologies="Python, Django, PostgreSQL, Celery",
            start_date=date(2021, 6, 1),
            end_date=date(2023, 2, 1),
            is_current=False,
            order=1,
        )

        self.stdout.write("Seeding education...")
        Education.objects.all().delete()
        Education.objects.create(
            institution="Addis Ababa University",
            degree="B.Sc. in Computer Science",
            description="Coursework in algorithms, databases, and software engineering.",
            start_date=date(2017, 9, 1),
            end_date=date(2021, 6, 1),
            order=0,
        )

        self.stdout.write("Seeding services...")
        Service.objects.all().delete()
        for order, (title, desc) in enumerate([
            ("Full-Stack Web Development", "End-to-end web apps from database to UI."),
            ("React Frontend Development", "Fast, responsive, accessible interfaces in React."),
            ("Django Backend Development", "Robust APIs and data models with Django."),
            ("REST API Development", "Well-documented, secure REST APIs with DRF."),
            ("PostgreSQL Database Development", "Schema design, migrations, and query tuning."),
            ("Website Deployment", "Production-ready deployment and environment configuration."),
        ]):
            Service.objects.create(title=title, description=desc, order=order)

        self.stdout.write(self.style.SUCCESS("Sample portfolio data seeded successfully."))
