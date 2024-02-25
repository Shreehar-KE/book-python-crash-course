from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Page to list all topics"""
    topics = Topic.objects.order_by('date_added')

    public_topics = []
    private_topics = []
    owner_topics = []

    for topic in topics:
        if request.user.is_authenticated:
            if topic.owner == request.user:
                if topic.visibility == False:
                    private_topics.append(topic)
                else:
                    owner_topics.append(topic)
            else:
                if topic.visibility == True:
                    public_topics.append(topic)
        else:
            if topic.visibility == True:
                public_topics.append(topic)

    context = {'public_topics': public_topics,
               'private_topics': private_topics, 'owner_topics': owner_topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Display all the entries in a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    if topic.visibility == False:
        check_topic_owner(request.user, topic.owner)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """adds a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """adds a new entry"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request.user, topic.owner)  # Ex_19-4
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request.user, topic.owner)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def edit_topic(request, topic_id):
    """edit an existing topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request.user, topic.owner)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_topic.html', context)


def check_topic_owner(user, owner):  # Ex_19-3
    """checks whether the topic matches the currently logged-in user"""
    if owner != user:
        raise Http404
