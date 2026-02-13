from json import tool
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def index(request):
    projects = Project.objects.all()
    
    # Add a new attribute 'tech_list' to each project
    for project in projects:
        if project.technologies:  # check if not None/empty
            project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
        else:
            project.tech_list = []
    
    context = {
        'candidate': Candidate.objects.first(),
        'about': About.objects.first(),
        'qualifications': Qualification.objects.all(),
        'projects': projects,  # use updated projects with tech_list
        'experience': Experience.objects.all().order_by('-start_date'),
        'contact': Contact.objects.first(),
        'socials': SocialMedia.objects.all(),
        'languages': ProgrammingLanguage.objects.all(),
        'frameworkapis': FrameworkAPI.objects.all(),
        'databases': Database.objects.all(),
        'toolsplatforms': ToolsPlatforms.objects.all(),
        'webtech': WebTechnologies.objects.all(),
        'coreconcepts': CoreConcepts.objects.all(),
    }
    
    return render(request, 'myportfolio/index.html', context)


# Admin Login View
def adminlogin(request):
    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Only staff/admin users can login
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid credentials or not authorized."

    return render(request, 'myportfolio/admin/adminlogin.html', {'error': error})


# Dashboard View (example)
@login_required(login_url='adminlogin')
def dashboard(request):
    
    return render(request, 'myportfolio/admin/dashboard.html')

@login_required(login_url='adminlogin')
def adminlogout(request):
    logout(request)
    return redirect('adminlogin')



def home(request):
     # Get the existing hero if any
    hero = Candidate.objects.first()

    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        intro = request.POST.get('intro')
        image = request.FILES.get('image')

        if hero:  # Update existing hero
            hero.name = name
            hero.title = title
            hero.intro = intro
            if image:
                hero.image = image  # Only update if a new image is uploaded
            hero.save()
        else:  # Create new hero
            hero = Candidate.objects.create(
                name=name,
                title=title,
                intro=intro,
                image=image
            )

        return redirect('home')  # Redirect back to the same page
    
    return render(request, 'myportfolio/admin/home.html', {'hero': hero})

def about(request):
    # Get existing About instance, if any
    about = About.objects.first()

    if request.method == "POST":
        description = request.POST.get('description')
        resume = request.FILES.get('resume')

        if about:  # Update existing About
            about.description = description
            if resume:
                about.resume = resume  # Only update if new resume uploaded
            about.save()
        else:  # Create new About
            about = About.objects.create(
                description=description,
                resume=resume
            )

        return redirect('about')  # Redirect to same page after submit
        
    return render(request, 'myportfolio/admin/about.html', {'about': about})

# Display Qualifications and Add / Edit Form
def qualifications(request, id=None):
    """
    Add / Update Qualification
    """
    qualification = None
    if id:
        qualification = get_object_or_404(Qualification, id=id)

    if request.method == "POST":
        institution = request.POST.get('institution')
        degree = request.POST.get('degree')
        specialization = request.POST.get('specialization')
        period = request.POST.get('period')
        scored = request.POST.get('scored')
        description = request.POST.get('description')

        if qualification:   # Update
            qualification.institution = institution
            qualification.degree = degree
            qualification.specialization = specialization
            qualification.period = period
            qualification.scored = scored
            qualification.description = description
            qualification.save()
        else:          # Create
            Qualification.objects.create(
                institution=institution,
                degree=degree,
                specialization=specialization,
                period=period,
                scored=scored,
                description=description
            )

        return redirect('qualifications')

    qualifications_list = Qualification.objects.all()

    return render(request, 'myportfolio/admin/qualifications.html', {
        'qualifications_list': qualifications_list,
        'qualification': qualification
    })

def delete_qualification(request, id):
    qualification = get_object_or_404(Qualification, id=id)
    qualification.delete()
    return redirect('qualifications')


def languages(request, id=None):
    """
    Add / Update Programming Language
    """
    language = None
    if id:
        language = get_object_or_404(ProgrammingLanguage, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if language:   # Update
            language.name = name
            language.save()
        else:          # Create
            ProgrammingLanguage.objects.create(name=name)

        return redirect('languages')

    planguages = ProgrammingLanguage.objects.all()

    return render(request, 'myportfolio/admin/language.html', {
        'planguages': planguages,
        'language': language
    })


def delete_language(request, pk):
    language = get_object_or_404(ProgrammingLanguage, pk=pk)
    language.delete()
    return redirect('languages')

def frameworkapi(request, id=None):
    """
    Add / Update Framework / API
    """
    frameworkapi = None
    if id:
        frameworkapi = get_object_or_404(FrameworkAPI, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if frameworkapi:   # Update
            frameworkapi.name = name
            frameworkapi.save()
        else:          # Create
            FrameworkAPI.objects.create(name=name)

        return redirect('frameworkapi')

    frameworkapis = FrameworkAPI.objects.all()

    return render(request, 'myportfolio/admin/frameworkapi.html', {
        'frameworkapis': frameworkapis,
        'frameworkapi': frameworkapi
    })


def delete_frameworkapi(request, id):
    frameworkapi = get_object_or_404(FrameworkAPI, id=id)
    frameworkapi.delete()
    return redirect('frameworkapi')



def databases(request, id=None):
    """
    Add / Update Database
    """
    database = None
    if id:
        database = get_object_or_404(Database, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if database:   # Update
            database.name = name
            database.save()
        else:          # Create
            Database.objects.create(name=name)

        return redirect('databases')

    databases_list = Database.objects.all()

    return render(request, 'myportfolio/admin/database.html', {
        'databases': databases_list,
        'database': database
    })


def delete_database(request, id):
    database = get_object_or_404(Database, id=id)
    database.delete()
    return redirect('databases')


def toolsplatforms(request, id=None):
    """
    Add / Update Tools & Platforms
    """
    tool = None
    if id:
        tool = get_object_or_404(ToolsPlatforms, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if tool:   # Update
            tool.name = name
            tool.save()
        else:          # Create
            ToolsPlatforms.objects.create(name=name)

        return redirect('toolsplatforms')

    tools_list = ToolsPlatforms.objects.all()

    return render(request, 'myportfolio/admin/toolsplatforms.html', {
        'tools': tools_list,
        'tool': tool
    })


def delete_tool(request, id):
    tool = get_object_or_404(ToolsPlatforms, id=id)
    tool.delete()
    return redirect('toolsplatforms')


def webtech(request, id=None):
    """
    Add / Update Web Technologies
    """
    web = None
    if id:
        web = get_object_or_404(WebTechnologies, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if web:   # Update
            web.name = name
            web.save()
        else:          # Create
            WebTechnologies.objects.create(name=name)

        return redirect('webtech')

    web_list = WebTechnologies.objects.all()

    return render(request, 'myportfolio/admin/webtech.html', {
        'web_list': web_list,
        'web': web
    })


def delete_webtech(request, id):
    web = get_object_or_404(WebTechnologies, id=id)
    web.delete()
    return redirect('webtech')


# Display Core Concepts and Add / Edit Form

def coreconcept(request, id=None):
    """
    Add / Update Core Concepts
    """
    concept = None
    if id:
        concept = get_object_or_404(CoreConcepts, id=id)

    if request.method == "POST":
        name = request.POST.get('name')

        if concept:   # Update
            concept.name = name
            concept.save()
        else:          # Create
            CoreConcepts.objects.create(name=name)

        return redirect('coreconcepts')

    concepts_list = CoreConcepts.objects.all()

    return render(request, 'myportfolio/admin/coreconcepts.html', {
        'concepts': concepts_list,
        'concept': concept
    })


def delete_coreconcept(request, id):
    concept = get_object_or_404(CoreConcepts, id=id)
    concept.delete()
    return redirect('coreconcepts')


# Display Projects and Add / Edit Form
def projects(request, project_id=None):
    """
    Display all projects, add new project or edit existing project
    """
    # If editing, fetch the project instance
    project = None
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        technologies = request.POST.get('technologies')
        github_link = request.POST.get('github_link')
        live_link = request.POST.get('live_link')
        image = request.FILES.get('image')

        if project:
            # Update existing project
            project.title = title
            project.description = description
            project.technologies = technologies
            project.github_link = github_link
            project.live_link = live_link
            if image:
                project.image = image
            project.save()
            messages.success(request, "Project updated successfully!")
        else:
            # Create new project
            Project.objects.create(
                title=title,
                description=description,
                technologies=technologies,
                github_link=github_link,
                live_link=live_link,
                image=image
            )
            messages.success(request, "Project added successfully!")

        return redirect('projects')  # Redirect back to project admin page

    # Get all projects to display in table
    all_projects = Project.objects.all()

    context = {
        'project': project,
        'all_projects': all_projects,
    }
    return render(request, 'myportfolio/admin/projects.html', context)


# Delete Project
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, "Project deleted successfully!")
    return redirect('projects')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Experience

def experience(request, exp_id=None):
    """
    Handles both adding a new experience and editing an existing one.
    If exp_id is provided, updates that experience. Otherwise, creates new.
    """
    experience = None
    if exp_id:
        experience = get_object_or_404(Experience, id=exp_id)

    if request.method == "POST":
        role = request.POST.get('role')
        company = request.POST.get('company')
        location = request.POST.get('location')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')

        if experience:  # Update existing experience
            experience.role = role
            experience.company = company
            experience.location = location
            experience.start_date = start_date
            experience.end_date = end_date
            experience.description = description
            experience.save()
        else:  # Add new experience
            Experience.objects.create(
                role=role,
                company=company,
                location=location,
                start_date=start_date,
                end_date=end_date,
                description=description
            )
        return redirect('experience')  # Redirect back to list page

    # List all experiences
    all_experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'myportfolio/admin/experience.html', {
        'all_experiences': all_experiences,
        'experience': experience
    })


def delete_experience(request, exp_id):
    experience = get_object_or_404(Experience, id=exp_id)
    experience.delete()
    return redirect('experience')


def contact(request):
    """
    Handles adding or editing the contact info.
    Only one contact instance is used.
    """
    # Get existing contact if any
    contact = Contact.objects.first()  # Assuming only one contact entry

    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')

        if contact:  # Update existing contact
            contact.email = email
            contact.phone = phone
            contact.location = location
            contact.save()
        else:  # Create new contact
            Contact.objects.create(
                email=email,
                phone=phone,
                location=location
            )
        return redirect('contact')  # Redirect back to same page

    return render(request, 'myportfolio/admin/contact.html', {
        'contact': contact
    })



def social_media(request, id=None):
    """
    Add / Update Social Media
    """
    social = None
    if id:
        social = get_object_or_404(SocialMedia, id=id)

    if request.method == "POST":
        platform = request.POST.get('platform')
        url = request.POST.get('url')

        if social:   # Update
            social.platform = platform
            social.url = url
            social.save()
        else:        # Create
            SocialMedia.objects.create(platform=platform, url=url)

        return redirect('socialmedia')

    socials = SocialMedia.objects.all()

    return render(request, 'myportfolio/admin/socialmedia.html', {
        'social': social,
        'socials': socials
    })


def delete_social_media(request, pk):
    social = get_object_or_404(SocialMedia, pk=pk)
    social.delete()
    return redirect('socialmedia')